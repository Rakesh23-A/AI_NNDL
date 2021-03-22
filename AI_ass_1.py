
'''
     find the global minimum point and value for the
    
         function  f(x) = x^4 + 3x^2 + 10
'''


x=1
eta =0.01
epochs =10**-6
delta_x =1
max_ite =100
iteration =0

def derivative(x):
    derivative = 4*(x**3)+6*x
    return derivative


while abs(delta_x) > epochs and iteration < max_ite :
    old_x =x
    delta_x = -eta*derivative(old_x)
    x =x + delta_x
    iteration +=1
    
print("the local minimum occurs at x = ",x)
print("the local minimum value is y = ", x**4 + 3*x**2 + 10)
