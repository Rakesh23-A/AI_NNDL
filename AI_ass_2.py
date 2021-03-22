
from sympy import*
x=symbols('x')
y=symbols('y')
f=x**2+y**2+10
u=diff(f,x)
v=diff(f,y)
#print("df/dx = ",u)
#print("df/dy = ",v)
X=1
Y=1
itr=1
n=0.1
epoch =10**-4
max_itr =100
delta_x =1
delta_y =1
while ( delta_x > epoch and delta_y > epoch ) and itr < max_itr :
    Gx=u.subs(x,X)
    Gy=v.subs(y,Y)
    #print(f"differentiation of f({x})=",Gx)
    #print(f"differentiation of f({y})=",Gy)
    delta_x =n*Gx
    delta_y =n*Gy
    #print("delta of x =",delta_x)
    #print("delta of y =",delta_y)
    X =X-delta_x
    Y =Y-delta_y
    #print("new x = ",X)
    #print("new y = ",Y)
    itr +=1
    #print('itr =',itr)
print("the local minimum occurs at x = ",X)
print("the local minimum occurs at y = ",Y)
print("Minimum value of f(x,y) = ",f.subs([(x,X),(y,Y)]))
