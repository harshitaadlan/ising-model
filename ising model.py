#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 10:54:03 2021

@author: harshita
"""


#%%
import numpy as np
import random
import math
import matplotlib.pyplot as plt
n=int(input('enter number:'))

def reversesign(x):
        r_ind = random.randint(0,len(x)-1)
        z = x[r_ind]*(-1)
        x[r_ind]=z
        return(x)
J=float(input('enter value of J:'))
t=float(input('enter temperature:'))
energy=1
energy_list=[]
mm=0
mg=1
cv=0
e,e2,e3,e4=0,0,0,0
e_l,e2_l,e3_l,e4_l=[],[],[],[]
while energy!=0 and mg!=0:
    x=[]
    for i in range (n):
        y=random.choice([-1,1])
        x.append(y)
    print(x)
    z=0
    m=0
    for i in range(len(x)):
        if i<len(x)-1:
            z+=x[i]*(x[i+1])*J
            m+=x[i]
        if i==len(x):
            m+=x[i]
            z+=x[len(x)]*J
    
    print('energy (initial) :',z)
    x2=reversesign(x)
    z2=0
    m2=0
    for i in range(len(x)):
        if i<len(x)-1:
            m2+=x[i]
            z2+=x[i]*(x[i+1])*J
        if i==len(x):
            m2+=x[i]
            z2+=x[len(x)]*J
    print('energy (on sign change:)',z2)
    energy = z2-z
    energy_list.append(energy)
    #for <E>/N
    e+=energy/(n**2)
    e_l.append(e)
    #for <E**2>
    e2+=(energy**2)/n
    e2_l.append(e2)
    #for <E>**2
    e3+=(energy/n)**2
    e3_l.append(e3)
    #for <delta(E)**2>
    e4+=e2-e3
    e4_l.append(e4)
    cv+=e4/(t**2)
    mg=m2-m
    mm+=mg/(n**2)
    r=random.uniform(0,1)
    print('r:',r)
    
    if z2> z:
        e_diff= math.exp((z-z2)/t)
        print(e_diff)
        if e_diff>=r:
            x2=x
            print('acceptable')
            av_z2=z2/n
            av_m2=m2/n
        else:
            print('not acceptable')
    else:
        x2=x
        print('acceptable')
    print('for <E>/N',e_l)
    print('for <E**2>',e2_l)
    print('for <E>**2',e3_l)
    print('for < delta_(E)**2>',e4_l)
    print('heat capacity:',cv)
print(energy_list)
plt.plot(energy_list)
plt.show()