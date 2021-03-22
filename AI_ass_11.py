import pandas as pd
from sympy import*
d1=[[0.2,3.4],[0.4,3.8],[0.6,4.2],[0.8,4.6]]
d2=pd.DataFrame(d1,columns=("X","Y"))
print(d2)
m=1
c=-1
N=0.1
G=0.9
VM=0
VC=0
epochs=2
x=symbols("x")
y=symbols("y")
g=symbols("g")
n=symbols("n")
vm=symbols("vm")
gm1=symbols("gm1")
vc=symbols("vc")
gc1=symbols("gc1")
gm=-(y-(m+g*vm)*x-(c+g+vc))*x
gc=-(y-(m+g*vm)*x-(c+g*vc))
vm1=g*vm-n*gm1
vc1=g*vc-n*gc1
l=len(d2)
for i in range(epochs):
    for j in range(l):
        x1=d2.iloc[j,0]
        y1=d2.iloc[j,1]
        gm2=gm.subs([(x,x1),(y,y1),(m,m),(c,c),(g,G),(vm,VM),(vc,VC)])
        gc2=gc.subs([(x,x1),(y,y1),(m,m),(c,c),(g,G),(vm,VM),(vc,VC)])
        vm2=vm1.subs([(g,G),(vm,VM),(n,N),(n,N),(gm1,gm2)])
        vc2=vc1.subs([(g,G),(vc,VC),(n,N),(n,N),(gc1,gc2)])
        newm=m+vm2
        newc=c+vc2
        m=newm
        c=newc
        print("m =",m,"c =",c)
print("final m value =",m)
print("final c value =",c)
