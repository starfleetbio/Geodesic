import numpy as np, matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Patch
from itertools import combinations
from math import isclose, sqrt
from pathlib import Path
import importlib, geolib; importlib.reload(geolib)
V=4; R=305.0; CUT=-84.3
raw=geolib._raw
vtx=raw[0]/np.linalg.norm(raw[0]); z=np.array([0,0,1.])
axr=np.cross(vtx,z); s=np.linalg.norm(axr); c=vtx@z; axr/=s
K=np.array([[0,-axr[2],axr[1]],[axr[2],0,-axr[0]],[-axr[1],axr[0],0]])
ROT=np.eye(3)+s*K+(1-c)*K@K; rv=(ROT@raw.T).T
edge=min(np.linalg.norm(raw[i]-raw[j]) for i,j in combinations(range(12),2))
FACES=[f for f in combinations(range(12),3)
       if all(isclose(np.linalg.norm(raw[a]-raw[b]),edge,rel_tol=1e-6) for a,b in combinations(f,2))]
A,B,C=raw[FACES[0][0]],raw[FACES[0][1]],raw[FACES[0][2]]
pts={}
for i in range(V+1):
    for j in range(V+1-i):
        k=V-i-j; p=(i*A+j*B+k*C)/V; pts[(i,j,k)]=p/np.linalg.norm(p)
def chord(a,b): return np.linalg.norm(pts[a]-pts[b])
def small_triangles(V):
    T=[]
    for i in range(V):
        for j in range(V-i):
            k=V-i-j; T.append(((i+1,j,k-1),(i,j+1,k-1),(i,j,k)))
    for i in range(V):
        for j in range(V-i-1):
            k=V-i-j; T.append(((i+1,j,k-1),(i,j+1,k-1),(i+1,j+1,k-2)))
    return T
tris=small_triangles(V)
uniqL=sorted(set(round(chord(t[a],t[b]),6) for t in tris for a,b in[(0,1),(1,2),(2,0)]))
labels={L:chr(ord('A')+i) for i,L in enumerate(uniqL)}
def shape_LR(t):
    seq=[labels[round(chord(t[0],t[1]),6)],labels[round(chord(t[1],t[2]),6)],labels[round(chord(t[2],t[0]),6)]]
    crot=min(tuple(seq[i:]+seq[:i]) for i in range(3))
    refl=min(tuple(seq[::-1][i:]+seq[::-1][:i]) for i in range(3))
    key=min(crot,refl)
    base={('A','A','C'):'T1',('B','B','C'):'T2',('B','D','E'):'T3',('E','E','F'):'T4',('F','F','F'):'T5'}[key]
    if base=='T3': return 'T3L' if crot==('B','D','E') else 'T3R'
    return base
GREY={'T1':'#FFFFFF','T2':'#D1D3D5','T3':'#A6A9AA','T4':'#8E9089','T5':'#545454'}
BASECHORD={'T1':'C','T2':'C','T3L':'E','T3R':'E','T4':'F'}
def col_of(nm): return GREY['T3'] if nm.startswith('T3') else GREY[nm]
def bary2d(i,j,k,P0,P1,P2): return (i*np.array(P0)+j*np.array(P1)+k*np.array(P2))/V
def lum(hx): hx=hx.lstrip('#'); r,g,b=[int(hx[i:i+2],16)/255 for i in(0,2,4)]; return .299*r+.587*g+.114*b
zc=rv[:,2]; order=np.argsort(zc); top=order[-1]; bot=order[0]
upper=set(order[-6:-1]); lower=set(order[1:6])
def ftype(f):
    if top in f: return 'topcap'
    if bot in f: return 'botcap'
    return 'upband' if len(set(f)&upper)==1 else 'downband'
def pick(tp):
    for f in FACES:
        if ftype(f)==tp: return f
def smask(vP0,vP1,vP2):
    keep=set()
    for t in tris:
        zs=[]
        for (i,j,k) in t:
            p=(i*vP0+j*vP1+k*vP2)/V; p=p/np.linalg.norm(p)*R; zs.append(p[2])
        if min(zs)>=CUT-0.3: keep.add(t)
    return keep
fu=pick('upband'); lo=[v for v in fu if v in lower]; hi=[v for v in fu if v in upper][0]
MU=smask(rv[lo[0]],rv[lo[1]],rv[hi])
fd=pick('downband'); u2=[v for v in fd if v in upper]; l1=[v for v in fd if v in lower][0]
MD=smask(rv[u2[0]],rv[u2[1]],rv[l1]); MF=set(tris)
h=sqrt(3)/2
def up(x,y0):   return [np.array([x,y0]),np.array([x+1,y0]),np.array([x+0.5,y0+h])]
def down(x,y0): return [np.array([x+1,y0+h]),np.array([x,y0+h]),np.array([x+0.5,y0])]
def lbl_angle(poly,letts,nm,face):
    if nm=='T5': return 0.0 if face=='up' else 180.0     # FFF: horizontal up / upside-down down
    bc=BASECHORD[nm]; ei=[i for i in range(3) if letts[i]==bc][0]
    Va=poly[ei]; Vb=poly[(ei+1)%3]; Vc=poly[(ei+2)%3]
    u=np.array(Vb)-np.array(Va); mid=(np.array(Va)+np.array(Vb))/2; perp=np.array([-u[1],u[0]])
    if perp@(np.array(Vc)-mid)<0: u=-u
    return np.degrees(np.arctan2(u[1],u[0]))
ARC_PATTERN=['T3R','T5','T3L','T2']    # user-specified rotational start; repeats 5× around the ring
ARC_COLOR='#000000'
def draw_arc_row(ax,x_min,x_max,y_top,arc_h=0.28):
    """20 black rim arcs (4-shape pattern × 5) laid out below the panel array,
    each labeled with the panel it seats (inner-face label)."""
    n=len(ARC_PATTERN)*5; w=(x_max-x_min)/n; y_bot=y_top-arc_h
    for i in range(n):
        shape=ARC_PATTERN[i%len(ARC_PATTERN)]; x0=x_min+i*w
        rect=[(x0,y_top),(x0+w,y_top),(x0+w,y_bot),(x0,y_bot)]
        ax.add_patch(Polygon(rect,closed=True,facecolor=ARC_COLOR,edgecolor='white',lw=0.6,zorder=4))
        ax.text(x0+w/2,(y_top+y_bot)/2,shape,ha='center',va='center',
                fontsize=4.0,color='white',fontweight='bold',zorder=6)
def draw(placements,outfile):
    fig,ax=plt.subplots(figsize=(16,7)); bg='#9aa0aa'; ax.set_facecolor(bg); fig.patch.set_facecolor(bg)
    edgemids={}
    for P,mask,face in placements:
        kept=[t for t in tris if t in mask]
        for t in kept:
            poly=[bary2d(*v,P[0],P[1],P[2]) for v in t]; nm=shape_LR(t); col=col_of(nm)
            ax.add_patch(Polygon(poly,closed=True,facecolor=col,edgecolor='white',lw=0.6))
            letts=[labels[round(chord(t[0],t[1]),6)],labels[round(chord(t[1],t[2]),6)],labels[round(chord(t[2],t[0]),6)]]
            ang=lbl_angle(poly,letts,nm,face); ctr=np.mean(poly,axis=0)
            tc='white' if lum(col)<0.5 else '#1a1a1a'
            ax.text(ctr[0],ctr[1],nm,ha='center',va='center',fontsize=4.0,color=tc,fontweight='bold',
                    rotation=ang,rotation_mode='anchor',zorder=5)
            for a,b in [(t[0],t[1]),(t[1],t[2]),(t[2],t[0])]:
                m=(bary2d(*a,P[0],P[1],P[2])+bary2d(*b,P[0],P[1],P[2]))/2
                key=(round(m[0],3),round(m[1],3))
                if key not in edgemids: edgemids[key]=(m,labels[round(chord(a,b),6)])
        from collections import Counter
        if mask is MF: ax.plot(*zip(P[0],P[1],P[2],P[0]),color='#2b2e34',lw=1.3,zorder=4)
        else:
            ec=Counter(); ep={}
            for t in kept:
                pw=[tuple(np.round(bary2d(*v,P[0],P[1],P[2]),4)) for v in t]
                for a,b in [(pw[0],pw[1]),(pw[1],pw[2]),(pw[2],pw[0])]:
                    kk=frozenset([a,b]); ec[kk]+=1; ep[kk]=(a,b)
            for kk,n in ec.items():
                if n==1: a,b=ep[kk]; ax.plot([a[0],b[0]],[a[1],b[1]],color='#2b2e34',lw=1.3,zorder=4)
    for (m,lab) in edgemids.values():
        ax.text(m[0],m[1],lab,ha='center',va='center',fontsize=4.0,color='#111',fontweight='bold',zorder=6,
                bbox=dict(boxstyle='circle,pad=0.06',fc='white',ec='#888',lw=0.3))
    # Arc row: 20 black rim arcs (T3R·T5·T3L·T2 × 5) just under the panel array.
    xs=[v[0] for P,_,_ in placements for v in P]
    draw_arc_row(ax,min(xs),max(xs),y_top=min(v[1] for P,_,_ in placements for v in P)-0.05)
    ax.set_aspect('equal'); ax.axis('off')
    ax.set_title('5/8 truncation net (inside view)',fontsize=12,color='#15181d')
    panel_leg=[Patch(fc=GREY[k],ec='#555',label=l) for k,l in
         [('T1','T1 A·A·C'),('T2','T2 B·B·C'),('T3','T3L D·B·E'),('T3','T3R B·D·E'),('T4','T4 E·E·F'),('T5','T5 F·F·F')]]
    arc_leg=[Patch(fc=ARC_COLOR,ec='#555',label=f'arc→{s}') for s in ARC_PATTERN]
    lg1=ax.legend(handles=panel_leg,title='Panels',loc='lower left',bbox_to_anchor=(0.02,-0.12),
                  fontsize=8,frameon=False,ncol=6,labelcolor='#15181d',title_fontsize=8)
    lg1.get_title().set_color('#15181d')
    ax.add_artist(lg1)
    lg2=ax.legend(handles=arc_leg,title='Arcs (× 5 repeats = 20 total)',loc='lower right',
                  bbox_to_anchor=(0.98,-0.12),fontsize=8,frameon=False,ncol=4,
                  labelcolor='#15181d',title_fontsize=8)
    lg2.get_title().set_color('#15181d')
    plt.tight_layout(); plt.savefig(outfile,dpi=200,bbox_inches='tight',facecolor=bg); plt.close(); print('saved',outfile)
tr=[]
for f in range(10):
    tr.append((up(f*0.5,0),MU,'up') if f%2==0 else (down(f*0.5,0),MD,'down'))
for x in [0.5,1.5,2.5,3.5,4.5]: tr.append((up(x,h),MF,'up'))
out=Path(__file__).resolve().parent.parent/'images'/'7) net58_labeled.png'
draw(tr,str(out))
