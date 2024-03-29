#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import numpy as np
from math import factorial
from scipy.integrate import quad
from scipy.special import hermite
import matplotlib.pyplot as plt

# Define physical parameters
n_p = 0.9
n_b = 0.2
v_b = 4.5
v_t = 0.5


def f(v):
    # Descibe the function to be expanded
    
    #return (n_p/np.sqrt(2*np.pi))*np.exp(-0.5*v**2)
    
    return (n_p/np.sqrt(2*np.pi))*np.exp(-0.5*v**2) + (n_b/np.sqrt(2*np.pi))*np.exp(-0.5*(v-v_b)**2/v_t**2)    

def integrand(v):
    # Setup the integrand
    return f(v)*hermite(s)(v)*np.exp(-v**2)

def coefficient(s):
    # Evaluate the coefficients of the expansion
    return (np.sqrt(np.pi)*2**s*factorial(s))**(-1)*quad(integrand, -np.inf, np.inf)[0]

# v space 
v = np.linspace(-2*np.pi, 2*np.pi, 1000)

# Sum of the expansion terms
f_exp = 0

# Error store
epsilon = []

# Number of polynomials used (degree of maximum polynomial)
n = 60

for i in range(n+1):
    s = i
    
    f_exp += coefficient(s) * hermite(s)(v)
    epsilon.append(np.linalg.norm(f_exp-f(v))/np.linalg.norm(f_exp))

# Plot of Function and its Hermite decompistion
plt.plot(v, f_exp, label='Hermite', color='red')
plt.plot(v, f(v), label='$f(x)$', linestyle='--', color='black')
plt.legend()
plt.show()

# Plotting of error
plt.plot(range(n+1), epsilon)
plt.xlabel('Number of Hermite functions')
plt.ylabel('$\epsilon$')
plt.show()