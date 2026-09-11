import numpy as np, trimesh
from matplotlib.textpath import TextPath
from matplotlib.font_manager import FontProperties
from shapely.geometry import Polygon
from geolib import classify, build_panel, letter_of, P

R=305.0; Vf=4
t_web=P['t_web']; t_rim=P['t_rim']; rim_w=P['rim_w']
FONT=FontProperties(family='DejaVu Sans', weight='bold')
DEPTH=0.6; PROUD=0.3

def text_prism(s, size, depth=DEPTH, proud=PROUD):
    """Return a trimesh prism of the text, centered at origin in xy, z in [-proud, +depth]."""
    tp=TextPath((0,0), s, size=size, prop=FONT)
    polys=[p for p in tp.to_polygons() if len(p)>=3]
    geom=None
    for pts in polys:
        poly=Polygon(pts)
        if not poly.is_valid: poly=poly.buffer(0)
        geom = poly if geom is None else geom.symmetric_difference(poly)  # even-odd -> holes
    parts=[]
    gg=[geom] if geom.geom_type=='Polygon' else list(geom.geoms)
    h=depth+proud
    for g in gg:
        if g.area<1e-6: continue
        m=trimesh.creation.extrude_polygon(g, height=h)
        parts.append(m)
    prism=trimesh.util.concatenate(parts)
    # center in xy, shift z so it spans [-proud, +depth]
    b=prism.bounds; cx=(b[0,0]+b[1,0])/2; cy=(b[0,1]+b[1,1])/2
    prism.apply_translation([-cx,-cy,-proud])
    return prism

def frame_to_world(prism, anchor, ex, ey, ez):
    Rm=np.column_stack([ex,ey,ez])
    Tm=np.eye(4); Tm[:3,:3]=Rm; Tm[:3,3]=anchor
    m=prism.copy(); m.apply_transform(Tm); return m

def label_panel(name, tri, panel):
    o=tri.mean(0)
    nrm=np.cross(tri[1]-tri[0],tri[2]-tri[0]); nrm/=np.linalg.norm(nrm)
    if nrm@o<0: nrm=-nrm                       # outward
    cuts=[]
    # ---- shape name at the web centre, baseline along the LONGEST edge, upright toward apex ----
    elen=[np.linalg.norm(tri[(i+1)%3]-tri[i]) for i in range(3)]
    e=int(np.argmax(elen)); Va,Vb,Vc=tri[e],tri[(e+1)%3],tri[(e+2)%3]
    ex=(Vb-Va); ex-=nrm*(ex@nrm); ex/=np.linalg.norm(ex)
    ey=np.cross(nrm,ex); ey/=np.linalg.norm(ey)
    if ey@(Vc-o)<0: ex=-ex; ey=np.cross(nrm,ex); ey/=np.linalg.norm(ey)   # up = toward apex
    anchor=o - nrm*t_web
    disp={'T3L':'T3L','T3R':'T3R'}.get(name,name)
    cuts.append(frame_to_world(text_prism(disp, 8.0), anchor, -ex, ey, nrm))  # -ex: read correct from inner side
    # ---- chord letter on each edge's rim band (inner rim surface at M - nrm*t_rim) ----
    for e in range(3):
        Va,Vb=tri[e],tri[(e+1)%3]; M=(Va+Vb)/2
        L=letter_of(np.linalg.norm(Vb-Va),R)
        edir=(Vb-Va)/np.linalg.norm(Vb-Va); edir-=nrm*(edir@nrm); edir/=np.linalg.norm(edir)
        ey2=np.cross(nrm,edir); ey2/=np.linalg.norm(ey2)          # up (perp to edge, in plane)
        if ey2@(o-M)<0: edir=-edir; ey2=np.cross(nrm,edir); ey2/=np.linalg.norm(ey2)  # up = toward centroid
        pos=M + (o-M)/np.linalg.norm(o-M)*(rim_w/2)              # centered ON the rim band (2.5mm inboard)
        anchor2=pos - nrm*t_rim
        cuts.append(frame_to_world(text_prism(L, 4.5, depth=0.8), anchor2, -edir, ey2, nrm))  # bigger+deeper for legibility; -edir reads from inner side
    cut=trimesh.util.concatenate(cuts)
    try:
        out=panel.difference(cut, engine='manifold')      # robust engine -> clean 2-manifold result
    except Exception:
        out=panel.difference(cut)
    return out

def build_all(export_dir):
    import os; os.makedirs(export_dir,exist_ok=True)
    pts,tris,lab,uniq,seq,crot,shp=classify(Vf,R)
    world=lambda t: np.array([pts[t[0]],pts[t[1]],pts[t[2]]])
    reps={}
    for t in tris:
        ck=crot(seq(t)); sk=shp(seq(t))
        nm={('A','A','C'):'T1',('B','B','C'):'T2',('E','E','F'):'T4',('F','F','F'):'T5'}.get(sk)
        if nm is None and sk==('B','D','E'): nm='T3L' if ck==('B','D','E') else 'T3R'
        if nm and nm not in reps: reps[nm]=t
    res={}
    for nm in ['T1','T2','T3L','T3R','T4','T5']:
        tri=world(reps[nm]); panel,_=build_panel(tri,sockets=True)
        lp=label_panel(nm,tri,panel)
        lp.export(f'{export_dir}/{nm}.stl')
        res[nm]=(tri,lp)
        print(f'{nm}: wt={lp.is_watertight} vol={lp.volume/1000:.2f} ext={np.round(lp.extents,1)}')
    return res

if __name__=='__main__':
    build_all('kit_labeled')
