import pandas as pd
from sympy import*
d1=[[0.2,3.4,],[0.4,3.8],[0.6,4.2],[0.8,4.6]]
print(d1)
d2 =pd.DataFrame(d1,columns=("x","y"))
print(d2)
m=1
c=-1
n=0.5
epochs=10
x=symbols("x")
y=symbols("y")
l=len(d2)

for i in range(epochs):
    
    for j in range(l):
        
        gm =-(y-m*x-c)*x
        gc =-(y-m*x-c)
        
        X =d2.iloc[j,0]
        Y =d2.iloc[j,1]
        
        Gm =gm.subs([(x,X),(y,Y)])
        Gc =gc.subs([(x,X),(y,Y)])
        
        delta_m =-n*Gm
        delta_c =-n*Gc
        
        m =m+delta_m
        c =c+delta_c
        
        #print(m,c)
        
print("final m value =",m)
print("final c value =",c)

