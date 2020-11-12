# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 10:22:23 2016

@author: Tom
"""

def f(x):
    from math import sin
    return x+sin(2*x)

def falling(h,v0=0):
    from math import sqrt
    g=9.8
    time = -v0/g + sqrt(v0**2/g**2+2*h/g)
    velo = sqrt(v0**2+2*g*h)
    return time,velo

