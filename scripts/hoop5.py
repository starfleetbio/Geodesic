import numpy as np, trimesh, importlib
import geolib; importlib.reload(geolib)
from geolib import small_triangles, FACES, P, KEY, letter_of

R=305.0; Vf=4; CUT=-84.3; FOOT=-100.0     # 5/8 truncation, shallow zig-zag
d_ball=P['d_ball']; r_ball=d_ball/2; t_rim=P['t_rim']
socket_r=P['socket_d']/2; neck_r=P['neck_d']/2; slide_r=P['slide_d']/2; neck_len=P['neck_len']

_raw=geolib._raw
vtx=_raw[0]/np.linalg.norm(_raw[0]); z=np.array([0,0,1.])
ax=np.cross(vtx,z); s=np.linalg.norm(ax); c=vtx@z
ax/=s; K=np.array([[0,-ax[2],ax[1]],[ax[2],0,-ax[0]],[-ax[1],ax[0],0]])
ROT=np.eye(3)+s*K+(1-c)*K@K; rawv=(ROT@_raw.T).T
def fp(face):
    A,B,C=rawv[list(face)]; d={}
    for i in range(Vf+1):
        for j in range(Vf+1-i):
            k=Vf-i-j; p=(i*A+j*B+k*C)/Vf; d[(i,j,k)]=p/np.linalg.norm(p)*R
    return d
def ptype(tri):
    L=[letter_of(np.linalg.norm(tri[i]-tri[(i+1)%3]),R) for i in range(3)]
    shp=min([tuple(L[i:]+L[:i]) for i in range(3)]+[tuple(L[::-1][i:]+L[::-1][:i]) for i in range(3)])
    m={('A','A','C'):'T1',('B','B','C'):'T2',('E','E','F'):'T4',('F','F','F'):'T5'}
    return m.get(shp,'T3')
def key(p): return tuple(np.round(p,2))
kept=[]
for face in FACES:
    d=fp(face)
    for t in small_triangles(Vf):
        tri=np.array([d[t[0]],d[t[1]],d[t[2]]])
        if tri[:,2].min()>=CUT-0.3: kept.append(tri)
from collections import Counter
ec=Counter(); ep={}
for tri in kept:
    for e in range(3):
        a,b=tri[e],tri[(e+1)%3]; k=tuple(sorted([key(a),key(b)])); ec[k]+=1; ep[k]=(a,b)
bnd={k for k,n in ec.items() if n==1}
verts={}
for k in bnd:
    a,b=ep[k]; verts[key(a)]=a; verts[key(b)]=b
ring=sorted(verts.values(),key=lambda p:np.arctan2(p[1],p[0])); N=len(ring)

def owner(a,b):
    ka,kb=key(a),key(b)
    for tri in kept:
        ks=[key(v) for v in tri]
        if ka in ks and kb in ks:
            o=tri.mean(0); nrm=np.cross(tri[1]-tri[0],tri[2]-tri[0]); nrm/=np.linalg.norm(nrm)
            if nrm@o<0: nrm=-nrm
            nf=np.cross(a,b); nf/=np.linalg.norm(nf)
            if nf@((a+b)/2-o)<0: nf=-nf
            return ptype(tri),letter_of(np.linalg.norm(b-a),R),nrm,nf
    raise RuntimeError
edgeseq=[owner(np.array(ring[i]),np.array(ring[(i+1)%N]))[:2] for i in range(N)]  # (type,chord) per edge

def cyl(r,p0,p1): return trimesh.creation.cylinder(radius=r,sections=24,segment=np.array([p0,p1],float))
def ico(r,ctr):
    m=trimesh.creation.icosphere(subdivisions=3,radius=r); m.apply_translation(ctr); return m
def wall_seg(a,b):
    fin=(R-t_rim)/R
    top=[a,b,b*fin,a*fin]; foot=[[p[0],p[1],FOOT] for p in top]
    return trimesh.convex.convex_hull(np.vstack([top,foot]))

def build_arc(i0):
    """2-edge arc starting at ring[i0]. splice: 3 magnets at the tall (z>-80, T2|T3) joints, 2 at short."""
    e1=(np.array(ring[i0]),np.array(ring[(i0+1)%N])); e2=(np.array(ring[(i0+1)%N]),np.array(ring[(i0+2)%N]))
    body=wall_seg(*e1).union(wall_seg(*e2))
    cuts=[]; seat=[]; spl=[]
    for (a,b) in (e1,e2):
        ty,L,nrm,nf=owner(a,b); off=KEY[L]
        rin=-np.array([(a+b)[0],(a+b)[1],0]); rin/=np.linalg.norm(rin)
        for t in (0.5-off,0.5+off):
            Epc=(1-t)*a+t*b
            Ch=Epc + rin*(t_rim*0.5) - np.array([0,0,r_ball*0.6])
            cuts.append(ico(socket_r,Ch))
            x,y,zc=Ch; d1=np.sqrt(max(socket_r**2-neck_r**2,1e-6))
            cuts.append(cyl(neck_r,[x,y,zc-d1],[x,y,zc-d1-neck_len]))
            cuts.append(cyl(slide_r,[x,y,zc-d1-neck_len],[x,y,FOOT-3]))
            seat.append((Ch,L))
    for endpt in (np.array(ring[i0]),np.array(ring[(i0+2)%N])):
        npk=3 if endpt[2]>-80 else 2                    # tall T2|T3 joint (z=-76.6) -> 3, short T5|T3 (z=-84.3) -> 2
        tang=(np.array(ring[(i0+1)%N])-endpt); tang/=np.linalg.norm(tang)
        rout=np.array([endpt[0],endpt[1],0]); rout/=np.linalg.norm(rout); rin=-rout
        ztop=endpt[2]-3; zbot=FOOT+3
        for zz in np.linspace(zbot,ztop,npk):
            base=endpt*((R-t_rim*0.5)/R)
            Cs=np.array([base[0],base[1],zz])+tang*1.2
            cuts.append(ico(socket_r,Cs))
            exitp=Cs+tang*10.0+rin*8.0
            g=(exitp-Cs); g/=np.linalg.norm(g); d1=np.sqrt(max(socket_r**2-neck_r**2,1e-6))
            cuts.append(cyl(neck_r,Cs+g*d1,Cs+g*(d1+neck_len)))
            cuts.append(cyl(slide_r,Cs+g*(d1+neck_len),Cs+g*(d1+neck_len+16)))
            spl.append((Cs,npk))
    body=body.difference(trimesh.util.concatenate(cuts))
    big=[cc for cc in body.split(only_watertight=False) if cc.volume/1000>0.05]
    body=big[0] if len(big)==1 else trimesh.util.concatenate(big)
    return body,seat,spl

def find_arc(pair):
    """return i0 whose two edges' types == pair (order-insensitive)."""
    for i in range(N):
        pr=(edgeseq[i][0],edgeseq[(i+1)%N][0])
        if set(pr)==set(pair): return i
    return None

if __name__=='__main__':
    import os; os.makedirs('parts',exist_ok=True)
    for nm,pair in [('T2T3',('T2','T3')),('T5T3',('T5','T3'))]:
        i0=find_arc(pair); arc,seat,spl=build_arc(i0)
        arc.export(f'parts/rim58_{nm}.stl')
        seats=[l for _,l in seat]; sc=[n for _,n in spl]
        print(f"rim58_{nm}: i0={i0} wt={arc.is_watertight} body={arc.body_count} vol={arc.volume/1000:.1f}cm3 "
              f"ext={np.round(arc.extents,1)} seat_edges={seats} splice_counts={sorted(set(sc))}")
