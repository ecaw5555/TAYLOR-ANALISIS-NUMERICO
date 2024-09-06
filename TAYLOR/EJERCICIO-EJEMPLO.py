import numpy as np
from math import factorial
x0 = 0.5  
x1 = 0.8 
h = x1 - x0  
def f(x):
    return np.sin(x)

def f_prime(x):
    return np.cos(x)

def f_double_prime(x):
    return -np.sin(x)

def f_triple_prime(x):
    return -np.cos(x)

def f_fourth_prime(x):
    return np.sin(x)
def taylor_series_sin(x0, h):
    series = f(x0) 
    series += f_prime(x0) * h / factorial(1)  
    series += f_double_prime(x0) * h**2 / factorial(2)  
    series += f_triple_prime(x0) * h**3 / factorial(3) 
    series += f_fourth_prime(x0) * h**4 / factorial(4)  
    return series

taylor_approx = taylor_series_sin(x0, h)

print(f"Aproximación de Taylor para sin({x1}) = {taylor_approx}")
print(f"Valor real de sin({x1}) = {np.sin(x1)}")
