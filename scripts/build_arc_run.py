import numpy as np, trimesh, importlib
import geolib, hoop5; importlib.reload(geolib); importlib.reload(hoop5)
from geolib import P, KEY, letter_of, revolve_channel
from hoop5 import ring, N, R, owner
from labels import text_prism, frame_to_world
from shapely.geometry import Polygon, LineString
ring=np.array(ring); up=np.array([0,0,1.]); t_rim=P['t_rim']; rim_w=P['rim_w']; t_web=P['t_web']; r_ball=P['d_ball']/2
socket_r=P['socket_d']/2; win_r=P['window_d']/2; slide_r=P['slide_d']/2; barrel_r=P['barrel_d']/2
slide_past=P['slide_past']; WD=np.sqrt(socket_r**2-win_r**2); FLOOR2=-105.0
def facet_n(a,b):
    n=np.cross(b-a,up); n/=np.linalg.norm(n); m=(a+b)/2
    if n@np.array([m[0],m[1],0.])<0: n=-n
    return n
fn=[facet_n(ring[i],ring[(i+1)%N]) for i in range(N)]
def seam_n(vi):
    m=fn[(vi-1)%N]+fn[vi%N]; nn=np.cross(m,up); return nn/np.linalg.norm(nn)
def keepc(mesh,O,Nn,ref):
    nn=Nn if (ref-O)@Nn>0 else -Nn
    out=mesh.slice_plane(O,nn,cap=True); return out if out is not None and out.volume>1 else mesh
def wall(i):
    # body == the panels' radial frustum (hoop5.wall_seg): outer on sphere(R), inner scaled to R-t_rim.
    # This bevels the top edge (chord R -> chord R-t_rim) exactly like a panel edge -- no hand-rolled top cut.
    a=ring[i]; b=ring[(i+1)%N]; n=fn[i]; fin=(R-t_rim)/R
    top=np.array([a,b,b*fin,a*fin]); foot=np.array([[p[0],p[1],FLOOR2] for p in top])
    w=trimesh.convex.convex_hull(np.vstack([top,foot]))
    ref=np.array([(a[0]+b[0])/2,(a[1]+b[1])/2,((a[2]+b[2])/2+FLOOR2)/2])-n*(t_rim/2)
    w=keepc(w,a,seam_n(i),ref); w=keepc(w,b,seam_n((i+1)%N),ref)   # seam miters only
    return w,ref
def channelA(Fb,gdir,d_perim,throat_r):
    d_start=-socket_r+WD+0.02; d_barrel=WD+0.8; d_dn=WD+1.1; d_up=d_dn+0.3; slide_end=d_perim+slide_past
    def _sph(d): return np.sqrt(max(socket_r**2-(d-WD)**2,1e-4))
    prof=[(d,_sph(d)) for d in np.linspace(d_start,0.25,5)]+[(0.5,barrel_r),(d_barrel,barrel_r)]
    prof+=[(d_dn,throat_r),(d_up,slide_r),(slide_end,slide_r)]
    return revolve_channel(Fb,gdir,prof)
def align(mesh,g):
    nn=g/np.linalg.norm(g); tgt=np.array([0,0,-1.]); v=np.cross(nn,tgt); s=np.linalg.norm(v); c=nn@tgt
    K=np.array([[0,-v[2],v[1]],[v[2],0,-v[0]],[-v[1],v[0],0]]); Rm=np.eye(3)+K+K@K*((1-c)/max(s**2,1e-12))
    T=np.eye(4); T[:3,:3]=Rm; mesh.apply_transform(T)
def build(i,label,top_thr=3.0,seam_thr=3.1):
    piece,ref=wall(i); a=ring[i]; b=ring[(i+1)%N]; n=fn[i]
    u=(b-a)/np.linalg.norm(b-a); w=np.cross(n,u); w/=np.linalg.norm(w); o=piece.centroid
    def to2d(p): return (float((p-o)@u),float((p-o)@w))
    Lc=letter_of(np.linalg.norm(b-a),R); off=KEY[Lc]
    # PROVEN arc_run_* channel geometry (restored). This is the version that prints with a healthy ~0.68mm
    # outer skin. The later "per-face window" rework tilted the seam channels and cut the outer skin through
    # (~0.09mm) at the arc ends -- reverted. Only the deboss TEXT is changed vs the proven parts.
    mags=[]
    for t in (0.5-off,0.5+off):
        E=(1-t)*a+t*b; mags.append((E*((R-t_rim/2)/R),(b-a),top_thr))
    for vtx in (a,b):
        rad=np.array([vtx[0],vtx[1],0.]); rad/=np.linalg.norm(rad); H=vtx[2]-FLOOR2
        for hf in (6.0/H,(H-7.0)/H):
            z=vtx[2]-hf*H; sp=np.array([vtx[0],vtx[1],z]); mags.append((sp-rad*(t_rim/2),np.array([0,0,1.]),seam_thr))
    poly=Polygon([to2d(v) for v in piece.vertices]).convex_hull; ins=poly.buffer(-rim_w,join_style=2)
    cuts=[]
    for Fb,edir,thr in mags:
        edir=edir/np.linalg.norm(edir); g=np.cross(edir,n); g/=np.linalg.norm(g)
        if g@(Fb-o)<0: g=-g
        gdir=-g; Fb2=np.array(to2d(Fb)); gd2=np.array([gdir@u,gdir@w])
        if np.linalg.norm(gd2)>1e-9: gd2/=np.linalg.norm(gd2)
        d_perim=rim_w
        try:
            it=LineString([tuple(Fb2),tuple(Fb2+gd2*80)]).intersection(ins.exterior)
            if not it.is_empty:
                pp=[it] if it.geom_type=='Point' else list(it.geoms)
                d_perim=min(np.hypot(*(np.array(q.coords[0])-Fb2)) for q in pp)
        except Exception: pass
        cuts.append(channelA(Fb,gdir,d_perim,thr/2))
    base_out=o+n*((a-o)@n)
    ipts=np.array([base_out+x*u+y*w for x,y in np.array(ins.exterior.coords)[:-1]])
    pk=trimesh.convex.convex_hull(np.vstack([ipts-n*t_web,ipts-n*(t_rim+8)]))
    piece=piece.difference(pk,engine='manifold').difference(trimesh.util.concatenate(cuts),engine='manifold')
    # deboss the type name on the INNER WEB centre (away from the perimeter edges that blur letters);
    # proven channels above are unchanged, so the outer skin stays ~0.68mm. Reads from the inner side.
    wu=w if w[2]>0 else -w
    anchor=base_out - n*t_web
    dl=frame_to_world(text_prism(label,6.0,depth=0.8), anchor, -u, wu, n)
    piece=piece.difference(dl, engine='manifold')
    align(piece,n)                               # outer facet == fn plane now (no wedge), reliable coarse
    for _ in range(3):
        fnf=piece.face_normals; fc=piece.triangles_center; z0=piece.bounds[0,2]
        m=(fnf[:,2]<-0.99)&(fc[:,2]<z0+0.8)
        if m.sum()<3: break
        Vs=piece.vertices[np.unique(piece.faces[m])]; A=np.c_[Vs[:,0],Vs[:,1],np.ones(len(Vs))]
        (aa,bb,cc),*_=np.linalg.lstsq(A,Vs[:,2],rcond=None)
        if abs(aa)<1e-5 and abs(bb)<1e-5: break
        align(piece,np.array([aa,bb,-1.]))
    piece.apply_translation([0,0,-piece.bounds[0,2]])
    zc=piece.triangles_center[:,2]; zmax=piece.bounds[1,2]
    if (zc>zmax-1).sum()<(zc<piece.bounds[0,2]+1).sum():
        align(piece,np.array([0,0,1.])); piece.apply_translation([0,0,-piece.bounds[0,2]])
    fnf=piece.face_normals; zc=piece.triangles_center[:,2]; z0=piece.bounds[0,2]
    sh=(fnf[:,2]<-0.9)&(zc<z0+1.0); Vv=piece.vertices[np.unique(piece.faces[sh])]
    span=Vv[:,2].max()-Vv[:,2].min(); tch=100*np.mean(Vv[:,2]<Vv[:,2].min()+0.2)
    return piece,span,tch
lab={0:'T3L',1:'T5',2:'T3R',3:'T2'}; pieces={}   # arcs named by the TRIANGLE they meet (BL→T3L, F→T5, BR→T3R, C→T2)
for i in (0,1,2,3):
    p,span,tch=build(i,lab[i]); pieces[i]=p
    p.export(f'arc_run_{lab[i]}.stl')
    print(f"{lab[i]:2s} (e{i}): wt={p.is_watertight} vol={p.volume/1000:.2f}cm3 ext={np.round(p.extents,1)} span={span:.4f} touch={tch:.0f}%")
# plate 2x2 to fit P1S
def fx(m): m=m.copy(); m.apply_translation([-m.bounds[0,0],-m.bounds[0,1],-m.bounds[0,2]]); return m
order=[0,1,2,3]; ms=[fx(pieces[i]) for i in order]; G=12
colw=max(ms[0].extents[0],ms[2].extents[0]); rowh=max(ms[0].extents[1],ms[1].extents[1])
pos=[(0,rowh+G),(colw+G,rowh+G),(0,0),(colw+G,0)]
parts=[]
for m,(dx,dy) in zip(ms,pos): m.apply_translation([dx,dy,0]); parts.append(m)
plate=trimesh.util.concatenate(parts); plate.export('arc_run_plate.stl')
print('plate ext',np.round(plate.extents,1),'bodies',len(plate.split()),'-> fits P1S' if plate.extents[0]<256 and plate.extents[1]<256 else 'TOO BIG')
