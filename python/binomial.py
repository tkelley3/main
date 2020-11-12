# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 12:21:30 2018

@author: Tom K
"""
from numpy import zeros


def test(n):
    return pascal(n)

def factorial(n):
    f=1;
    for k in range(1,int(n+1)):
        f *=k
    return f

def binomial(n,k):
    bi = factorial(n)/(factorial(k)*factorial(n-k))
    return int(bi)

def pascal(n):
    
    p=zeros(n+1)
    for k in range(0,n+1):
        p[k] = binomial(n,k)
    print(p)
    #return p
    
def pascaltriangle(n):
    k=range(1,int(n+1))
    for j in k:
        pascal(j) 
        
def dice(n,k):
    prob = binomial(n,k)/2**n
    return prob

def totaldice(n,k):
    
    l=range(0,n-k+1)
    p = zeros(n-k+1)
    for r in l:
        p[r] = dice(n,r)
    return sum(p)