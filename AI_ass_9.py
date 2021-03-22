import pandas as pd
from sympy import*
d1=[[0.2,3.4],[0.4,3.8],[0.6,4.2],[0.8,4.6]]
d2=pd.DataFrame(d1,columns=("X","Y"))
print(d2)
m=1
c=1

n=0.3
g=0.8

Vm=0
Vc=0

epochs=100

x= symbols("x")
y= symbols("y")


vm=symbols("vm")
gm=symbols("gm")
vc=symbols("vc")
gc=symbols("gc")


l=len(d2)
for i in range(epochs):
    for j in range(l):

        gm1=-(y-m*x-c)*x
        gc1=-(y-m*x-c)

        vm1 =(g*vm)-(n*gm)
        vc1 =(g*vc)-(n*gc)
        
        X =d2.iloc[j,0]
        Y =d2.iloc[j,1]
        
        Gm =gm1.subs([(x,X),(y,Y)])
        Gc =gc1.subs([(x,X),(y,Y)])
        
        Vm =vm1.subs([(vm,Vm),(gm,Gm)])
        Vc =vc1.subs([(vc,Vc),(gc,Gc)])
        
        m =m+Vm
        c =c+Vc
        
        #print("m =",m,"c =",c)
print("final m value =",m)
print("final c value =",c)
