import numpy as np, trimesh
from itertools import combinations
from math import isclose
from shapely.geometry import Polygon

# ---- shared geodesic + panel-building library ----
phi=(1+5**0.5)/2
_raw=[]
for a in(1,-1):
    for b in(1,-1):
        _raw+=[(0,a,b*phi),(a,b*phi,0),(a*phi,0,b)]
_raw=np.array(sorted(set(_raw)),float); _raw/=np.linalg.norm(_raw[0])
_edge=min(np.linalg.norm(_raw[i]-_raw[j]) for i,j in combinations(range(12),2))
FACES=[f for f in combinations(range(12),3)
       if all(isclose(np.linalg.norm(_raw[a]-_raw[b]),_edge,rel_tol=1e-6) for a,b in combinations(f,2))]

def face_points(face,Vf,R):
    A,B,C=_raw[list(face)]
    pts={}
    for i in range(Vf+1):
        for j in range(Vf+1-i):
            k=Vf-i-j; p=(i*A+j*B+k*C)/Vf; pts[(i,j,k)]=p/np.linalg.norm(p)*R
    return pts

def small_triangles(Vf):
    T=[]
    for i in range(Vf):
        for j in range(Vf-i):
            k=Vf-i-j; T.append(((i+1,j,k-1),(i,j+1,k-1),(i,j,k)))
    for i in range(Vf):
        for j in range(Vf-i-1):
            k=Vf-i-j; T.append(((i+1,j,k-1),(i,j+1,k-1),(i+1,j+1,k-2)))
    return T

def frustum_channel(p0,r0,p1,r1,n=32):
    """Tapered (conical) channel from a circle of radius r0 at p0 to radius r1 at p1.
    A frustum is convex, so a convex hull of the two end-circles is exact. Used for the
    slide->throat taper so the horizontal magnet channel prints OPEN instead of bridging shut."""
    p0=np.asarray(p0,float); p1=np.asarray(p1,float)
    ax=p1-p0; L=np.linalg.norm(ax); ax=ax/L
    tmp=np.array([1,0,0.]) if abs(ax[0])<0.9 else np.array([0,1,0.])
    u=np.cross(ax,tmp); u/=np.linalg.norm(u); w=np.cross(ax,u)
    ang=np.linspace(0,2*np.pi,n,endpoint=False)
    c0=np.array([p0+r0*(np.cos(a)*u+np.sin(a)*w) for a in ang])
    c1=np.array([p1+r1*(np.cos(a)*u+np.sin(a)*w) for a in ang])
    return trimesh.convex.convex_hull(np.vstack([c0,c1]))

def revolve_channel(base,axis,profile,n=48):
    """One clean surface-of-revolution tube along `axis` from a (distance, radius) profile.
    Built as a single watertight mesh so there are NO boolean-junction coincident faces (which
    is what wrecks a channel assembled from separate cones/cylinders)."""
    base=np.asarray(base,float); axis=np.asarray(axis,float); axis=axis/np.linalg.norm(axis)
    tmp=np.array([1,0,0.]) if abs(axis[0])<0.9 else np.array([0,1,0.])
    u=np.cross(axis,tmp); u/=np.linalg.norm(u); w=np.cross(axis,u)
    ang=np.linspace(0,2*np.pi,n,endpoint=False); cs=np.cos(ang); sn=np.sin(ang)
    rings=[(base+axis*d)[None,:]+r*(np.outer(cs,u)+np.outer(sn,w)) for d,r in profile]
    V=np.vstack(rings); F=[]
    for k in range(len(profile)-1):
        a0=k*n; a1=(k+1)*n
        for i in range(n):
            j=(i+1)%n; F.append([a0+i,a0+j,a1+j]); F.append([a0+i,a1+j,a1+i])
    c0=len(V); V=np.vstack([V,base+axis*profile[0][0]])
    for i in range(n): F.append([c0,(i+1)%n,i])
    c1=len(V); V=np.vstack([V,base+axis*profile[-1][0]]); off=(len(profile)-1)*n
    for i in range(n): F.append([c1,off+i,off+(i+1)%n])
    m=trimesh.Trimesh(vertices=V,faces=np.array(F)); m.merge_vertices(); m.fix_normals(); return m

# default design parameters (mm) -- magnets are ABSOLUTE size
P=dict(d_ball=3.175, t_web=2.2, t_rim=5.2, rim_w=5.0, per_edge=2, insert='neck',
       socket_d=3.45, neck_d=3.10, slide_d=3.60, neck_len=0.8, window_d=1.4, slide_past=3.6,
       throat_d=3.2, barrel_d=3.6, seat='sphere_shallow')
# CHANNEL "A" (locked by coupon-2 magnet test): window Ø1.4 (flush datum, unchanged) -> shallow spherical
#   lead (cradles the ball forward for retention) -> OPEN barrel Ø3.6 (0.21mm/side equator gap -> ball SPINS
#   to self-align polarity) -> short chamfered throat Ø3.2 -> slide Ø3.60. Replaces the old full spherical cup
#   (Ø3.45, throat 3.1) which gripped the ball and would not rotate. Coupon-2 result: A & B (shallow seat) spun
#   AND retained; D (cone seat) lost retention; F (old full cup) too tight. A chosen: rotates, best retention
#   margin, 0.80mm wall over the magnet. Window/ball/bevel unchanged => kiss position identical, mates with all
#   previously printed parts. throat 3.1 is the fallback lever if a future spool/nozzle prints retention marginal.
# throat_d 3.1 : the channel now TAPERS from slide Ø3.60 (pocket) down to a Ø3.1 throat at the socket, instead
#   of a stepped neck. A cone has no abrupt overhang, so the horizontal channel prints OPEN (the old stepped
#   3.10 neck bridged shut). 3.1 is a hair under the 3.175 ball -> light mechanical capture that holds in ANY
#   orientation (panels horizontal, arc seats vertical), so gravity can't drop the ball. Final value TBD by magnet test.
# slide_past 3.6 : the slide runs out to the perimeter (inner rim wall) then this much FURTHER into the
#   pocket -- measured from the perimeter, not the socket. Just enough to drop the ball in and start a
#   tamper rod straight; the rod pushes the ball through the neck into the socket. (neck 3.1 vs 3.2 TBD by test.)
# window_d 1.4 : the socket, sunk so it is truncated by the mating bevel to a 1.4mm opening, leaves the
#   magnet FLUSH at the bevel (peeking through a 1.4 hole, retained because 1.4 < 3.175). Same on every magnet.
# POST-print insertion (printer off -> no magnet/hotend hazard).
#   socket_d 3.45  : sphere ~0.14 bigger than the 3.175 magnet -> ball rolls to set polarity
#   slide_d  3.60  : wide entry channel from the pocket; ball slides in with no force
#   neck_d   3.10  : a short pinch (0.075 under the ball) the ball just passes; gravity (~1.3 mN) can't
#                    push it back through, so it's captured; the neighbour magnet does the real holding
#   neck_len 0.8   : length of that pinch = the retention/insertion feel (TBD from the coupon test)
# t_rim 5.2 -> ~1mm skin over the magnet on both faces (hidden; shows only at the bevel window).
CF={'A':0.25318,'B':0.29453,'C':0.29524,'D':0.29859,'E':0.31287,'F':0.32492}
# keyed magnet offsets (fraction from edge midpoint) -- SYMMETRIC (so mating works) but DISTINCT per chord
KEY={'A':0.14,'B':0.19,'C':0.24,'D':0.29,'E':0.34,'F':0.39}
def letter_of(Lmm,R):
    f=Lmm/R
    return min(CF,key=lambda k:abs(CF[k]-f))

def build_panel(tri, sockets=True, prm=P):
    """tri: 3x3 world coords on the sphere (radius R from origin). Returns (panel, magnets)."""
    r_ball=prm['d_ball']/2; t_web=prm['t_web']; t_rim=prm['t_rim']; rim_w=prm['rim_w']
    socket_r=prm.get('socket_d',3.45)/2; neck_r=prm.get('neck_d',3.10)/2
    slide_r=prm.get('slide_d',3.60)/2; neck_len=prm.get('neck_len',0.8)
    tri=np.asarray(tri,float); o=tri.mean(0)
    Rlocal=np.linalg.norm(tri[0])
    def frustum(vs,rt,rb):
        top=np.array([v/np.linalg.norm(v)*rt for v in vs]); bot=np.array([v/np.linalg.norm(v)*rb for v in vs])
        return trimesh.convex.convex_hull(np.vstack([top,bot]))
    panel=frustum(tri,Rlocal,Rlocal-t_rim)
    # web pocket
    u=tri[0]-o; u/=np.linalg.norm(u)
    nrm=np.cross(tri[1]-tri[0],tri[2]-tri[0]); nrm/=np.linalg.norm(nrm)
    if nrm@o<0: nrm=-nrm            # ensure OUTWARD (away from sphere centre)
    vv=np.cross(nrm,u)
    poly=Polygon([(np.dot(p-o,u),np.dot(p-o,vv)) for p in tri])
    ins=poly.buffer(-rim_w,join_style=2)
    if not ins.is_empty and ins.area>1:
        ipts=np.array([o+x*u+y*vv for x,y in np.array(ins.exterior.coords)[:-1]])
        # web measured perpendicular from the FLAT outer face (not the sphere radius)
        top=ipts - nrm*t_web; bot=ipts - nrm*(t_rim+8)
        pk=trimesh.convex.convex_hull(np.vstack([top,bot]))
        panel=panel.difference(pk)
    if not sockets:
        return panel, None
    Rmid=Rlocal-t_rim/2
    key=prm.get('key',KEY); insert=prm.get('insert','inplane')
    cuts=[]; mags=[]; _ci=0; _throats=prm.get('throats')
    _barrels=prm.get('barrels'); _seats=prm.get('seats')      # per-channel barrel Ø and seat type (coupon sweep)
    for e in range(3):
        Va,Vb=tri[e],tri[(e+1)%3]
        edir=(Vb-Va)/np.linalg.norm(Vb-Va)
        nf=np.cross(Va,Vb); nf/=np.linalg.norm(nf)
        if np.dot(nf,(Va+Vb)/2-o)<0: nf=-nf
        # in-plane outward normal of this edge (from centroid toward edge, in the panel plane)
        g=np.cross(edir,nrm); g/=np.linalg.norm(g)
        if np.dot(g,(Va+Vb)/2-o)<0: g=-g
        off=key[letter_of(np.linalg.norm(Vb-Va),Rlocal)]
        for t in (0.5-off, 0.5+off):
            ch=_ci; _ci+=1
            win_r=prm.get('window_d',1.4)/2
            throat_r=(_throats[ch] if _throats else prm.get('throat_d',3.2))/2
            E=(1-t)*Va+t*Vb                       # point on the outer edge, keyed along the chord
            Fb=E*((Rlocal-t_rim/2)/Rlocal)        # mid-thickness point ON the bevel plane (window centre)
            gdir=-g                                # load axis: straight IN toward the pocket (~5deg off the bevel normal)
            # ---- window (Ø1.4, flush datum) -> SEAT -> open BARREL -> short chamfered throat -> slide ----
            # The Ø1.4 window is the forward datum: the ball floats forward to it and the mating bevels set the
            # final flush kiss, so opening the seat/barrel behind the window does NOT change inter-panel mating.
            # seat = how the ball is cradled just behind the window; barrel = the equator clearance that lets it SPIN.
            WD=np.sqrt(max(socket_r**2-win_r**2,1e-6))       # sphere sink: gives Ø(2*win_r) window at the bevel + ball flush
            barrel_r=(_barrels[ch]/2 if _barrels else prm.get('barrel_d',3.6)/2)   # open cylinder at the ball's equator (rotational space)
            seat=(_seats[ch] if _seats else prm.get('seat','sphere_shallow'))
            d_start=-socket_r+WD+0.02                                # start slightly proud of the bevel for a clean cut
            d_barrel=WD+0.8; d_dn=WD+1.1; d_up=d_dn+0.3             # barrel end · throat V (short chamfer) · slide
            # distance from the bevel to the perimeter (pocket inner wall) along gdir, in-plane
            Fb2=np.array([np.dot(Fb-o,u), np.dot(Fb-o,vv)])
            gd2=np.array([np.dot(gdir,u), np.dot(gdir,vv)])
            if np.linalg.norm(gd2)>1e-9: gd2/=np.linalg.norm(gd2)
            d_perim=rim_w
            try:
                from shapely.geometry import LineString
                inter=LineString([tuple(Fb2),tuple(Fb2+gd2*60)]).intersection(ins.exterior)
                if not inter.is_empty:
                    pp=[inter] if inter.geom_type=='Point' else list(inter.geoms)
                    d_perim=min(np.hypot(*(np.array(q.coords[0])-Fb2)) for q in pp)
            except Exception: pass
            slide_end=d_perim+prm.get('slide_past',3.6)
            def _sph(d): return np.sqrt(max(socket_r**2-(d-WD)**2,1e-4))
            if seat=='sphere_full':                                 # current design: full conformal cup (control)
                prof=[(d,_sph(d)) for d in np.linspace(d_start,WD,9)]+[(d_barrel,barrel_r)]
            elif seat=='sphere_shallow':                            # short spherical lead near the window, then open
                prof=[(d,_sph(d)) for d in np.linspace(d_start,0.25,5)]+[(0.5,barrel_r),(d_barrel,barrel_r)]
            elif seat=='cone':                                      # ~43deg conical lead: line (circle) contact, tangent to the ball
                slope=0.9325; d_cone=(barrel_r-win_r)/slope
                prof=[(d_start,win_r+slope*d_start),(d_cone,barrel_r),(d_barrel,barrel_r)]
            else:                                                   # 'window': bare Ø1.4 window ring straight into the barrel
                prof=[(d_start,win_r+0.9325*d_start),(0.15,barrel_r),(d_barrel,barrel_r)]
            prof+=[(d_dn,throat_r),(d_up,slide_r),(slide_end,slide_r)]                                 # throat V (short chamfer) · slide
            cuts.append(revolve_channel(Fb, gdir, prof))                                               # ONE clean tube (no junction faces)
            Cc=Fb+gdir*WD                                                                              # ball nominal centre (flush); floats forward in service
            mg=trimesh.creation.icosphere(subdivisions=3,radius=r_ball); mg.apply_translation(Cc); mags.append(mg)
    cutter=trimesh.util.concatenate(cuts)
    try:
        panel=panel.difference(cutter, engine='manifold')     # clean panel - clean revolve tubes -> clean 2-manifold
    except Exception:
        panel=panel.difference(cutter)
    return panel, trimesh.util.concatenate(mags)

def classify(Vf,R):
    pts=face_points(FACES[0],Vf,R)
    tris=small_triangles(Vf)
    def chord(a,b): return round(np.linalg.norm(pts[a]-pts[b])/R,6)
    uniq=sorted(set(chord(t[x],t[y]) for t in tris for x,y in [(0,1),(1,2),(2,0)]))
    lab={L:chr(ord('A')+i) for i,L in enumerate(uniq)}
    def seq(t): return [lab[chord(t[0],t[1])],lab[chord(t[1],t[2])],lab[chord(t[2],t[0])]]
    def crot(s): return min(tuple(s[i:]+s[:i]) for i in range(3))
    def shp(s): return min([tuple(s[i:]+s[:i]) for i in range(3)]+[tuple(s[::-1][i:]+s[::-1][:i]) for i in range(3)])
    return pts,tris,lab,uniq,seq,crot,shp
