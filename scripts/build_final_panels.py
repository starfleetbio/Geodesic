import os, numpy as np, trimesh, importlib
from pathlib import Path
import geolib; importlib.reload(geolib)
from geolib import P, classify, build_panel, letter_of, revolve_channel
from labels import text_prism, frame_to_world
STL_DIR = Path(os.environ.get('STL_DIR') or Path(__file__).resolve().parent.parent / 'stl')
R=305.0; Vf=4
t_web=P['t_web']; t_rim=P['t_rim']; rim_w=P['rim_w']
socket_r=P['socket_d']/2; win_r=P['window_d']/2; barrel_r=P['barrel_d']/2; slide_r=P['slide_d']/2
WD=np.sqrt(socket_r**2-win_r**2)
prm=dict(P); prm['throat_d']=3.0
pts,tris,lab,uniq,seq,crot,shp=classify(Vf,R)
world=lambda t: np.array([pts[t[0]],pts[t[1]],pts[t[2]]])
reps={}
for t in tris:
    ck=crot(seq(t)); sk=shp(seq(t))
    nm={('A','A','C'):'T1',('B','B','C'):'T2',('E','E','F'):'T4',('F','F','F'):'T5'}.get(sk)
    if nm is None and sk==('B','D','E'): nm='T3L' if ck==('B','D','E') else 'T3R'
    if nm and nm not in reps: reps[nm]=t
def align(mesh,g):
    nn=g/np.linalg.norm(g); tgt=np.array([0,0,-1.]); v=np.cross(nn,tgt); s=np.linalg.norm(v); c=nn@tgt
    if s<1e-9:
        if c<0: return
        T=np.eye(4); T[:3,:3]=trimesh.transformations.rotation_matrix(np.pi,[1,0,0])[:3,:3]; mesh.apply_transform(T); return
    K=np.array([[0,-v[2],v[1]],[v[2],0,-v[0]],[-v[1],v[0],0]]); Rm=np.eye(3)+K+K@K*((1-c)/s**2)
    T=np.eye(4); T[:3,:3]=Rm; mesh.apply_transform(T)
def label_web(nm,tri,panel):
    o=tri.mean(0); nrm=np.cross(tri[1]-tri[0],tri[2]-tri[0]); nrm/=np.linalg.norm(nrm)
    if nrm@o<0: nrm=-nrm
    cuts=[]
    elen=[np.linalg.norm(tri[(i+1)%3]-tri[i]) for i in range(3)]
    e=int(np.argmax(elen)); Va,Vb,Vc=tri[e],tri[(e+1)%3],tri[(e+2)%3]
    ex=(Vb-Va); ex-=nrm*(ex@nrm); ex/=np.linalg.norm(ex); ey=np.cross(nrm,ex); ey/=np.linalg.norm(ey)
    if ey@(Vc-o)<0: ex=-ex; ey=np.cross(nrm,ex); ey/=np.linalg.norm(ey)
    cuts.append(frame_to_world(text_prism(nm,8.0), o-nrm*t_web, -ex, ey, nrm))   # T-name @ web centre
    for e in range(3):                                                            # chord letters -> inner web
        Va,Vb=tri[e],tri[(e+1)%3]; M=(Va+Vb)/2
        L=letter_of(np.linalg.norm(Vb-Va),R)
        inw=(o-M); inw-=nrm*(inw@nrm); inw/=np.linalg.norm(inw)
        edir=(Vb-Va)/np.linalg.norm(Vb-Va); edir-=nrm*(edir@nrm); edir/=np.linalg.norm(edir)
        ey2=np.cross(nrm,edir); ey2/=np.linalg.norm(ey2)
        if ey2@inw<0: edir=-edir; ey2=np.cross(nrm,edir); ey2/=np.linalg.norm(ey2)
        pos=M+inw*(rim_w+3.0)
        cuts.append(frame_to_world(text_prism(L,4.5,depth=0.8), pos-nrm*t_web, -edir, ey2, nrm))
    return panel.difference(trimesh.util.concatenate(cuts),engine='manifold')
def win_ap(tri,e):
    o=tri.mean(0); nrm=np.cross(tri[1]-tri[0],tri[2]-tri[0]); nrm/=np.linalg.norm(nrm)
    if nrm@o<0: nrm=-nrm
    from geolib import KEY
    Va,Vb=tri[e],tri[(e+1)%3]; edir=(Vb-Va)/np.linalg.norm(Vb-Va)
    g=np.cross(edir,nrm); g/=np.linalg.norm(g)
    if g@((Va+Vb)/2-o)<0: g=-g
    gdir=-g; off=KEY[letter_of(np.linalg.norm(Vb-Va),R)]; t=0.5-off
    E=(1-t)*Va+t*Vb; Fb=E*((R-t_rim/2)/R)
    ds=-socket_r+WD+0.02
    prof=[(d,np.sqrt(max(socket_r**2-(d-WD)**2,1e-4))) for d in np.linspace(ds,0.25,5)]+[(0.5,barrel_r),(WD+0.8,barrel_r),(WD+1.1,3.0/2),(WD+1.4,slide_r),(8.0,slide_r)]
    cut=revolve_channel(Fb,gdir,prof)
    Vai=Va/np.linalg.norm(Va)*(R-t_rim); bf=np.cross(Vb-Va,Vai-Va); bf/=np.linalg.norm(bf)
    if bf@((Va+Vb)/2-o)<0: bf=-bf
    sec=cut.section(plane_origin=Fb,plane_normal=bf)
    if sec is None: return None
    Pl,_=sec.to_planar(); ex=sorted(Pl.vertices.max(0)-Pl.vertices.min(0),reverse=True); return round(ex[0],2)
print(f"{'part':5s} {'wt':3s} {'bodies':6s} {'span':7s} {'contact':7s} {'height':6s} {'windows Ø(mm)':22s} {'perf?':5s}")
for nm in ['T1','T2','T3L','T3R','T4','T5']:
    tri=world(reps[nm]); o=tri.mean(0)
    nrm=np.cross(tri[1]-tri[0],tri[2]-tri[0]); nrm/=np.linalg.norm(nrm)
    if nrm@o<0: nrm=-nrm
    aps=[win_ap(tri,e) for e in range(3)]
    panel,_=build_panel(tri,sockets=True,prm=prm)
    lp=label_web(nm,tri,panel)
    align(lp,nrm)
    for _ in range(3):
        fnf=lp.face_normals; fc=lp.triangles_center; z0=lp.bounds[0,2]
        m=(fnf[:,2]<-0.99)&(fc[:,2]<z0+0.8)
        if m.sum()<3: break
        Vs=lp.vertices[np.unique(lp.faces[m])]; A=np.c_[Vs[:,0],Vs[:,1],np.ones(len(Vs))]
        (aa,bb,cc),*_=np.linalg.lstsq(A,Vs[:,2],rcond=None)
        if abs(aa)<1e-6 and abs(bb)<1e-6: break
        align(lp,np.array([aa,bb,-1.]))
    lp.apply_translation([-lp.centroid[0],-lp.centroid[1],-lp.bounds[0,2]])
    fnf=lp.face_normals; zc=lp.triangles_center[:,2]; z0=lp.bounds[0,2]
    sh=(fnf[:,2]<-0.9)&(zc<z0+1.0); Vv=lp.vertices[np.unique(lp.faces[sh])]
    span=Vv[:,2].max()-Vv[:,2].min(); tch=100*np.mean(Vv[:,2]<Vv[:,2].min()+0.2)
    bodies=len(lp.split(only_watertight=False))
    # perforation check: any deboss vertex within 0.5mm of show face? show face at z~0; label lives high (web up)
    perf = (lp.vertices[:,2].min() < -0.01)   # nothing below plate
    lp.merge_vertices(); lp.update_faces(lp.nondegenerate_faces()); lp.update_faces(lp.unique_faces())
    lp.export(str(STL_DIR / f'{nm}.stl'))
    print(f"{nm:5s} {str(lp.is_watertight):3s} {bodies:6d} {span:7.4f} {tch:6.0f}% {lp.bounds[1,2]:6.2f} {str(aps):22s} {'BAD' if perf else 'ok':5s}")
