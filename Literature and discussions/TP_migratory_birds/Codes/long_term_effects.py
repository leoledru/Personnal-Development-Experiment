#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np 
import matplotlib.pyplot as plt 
import copy  

from fonctions import* 

# dict for default param values  
paramsD = {"xopt":50, "sigma":10, "r0":2.5, "a":0, "p":0.2, "K":5}


# Environmental change: 1st case -> optimum shift
new_x_opt = paramsD["xopt"] - 8 # 50 -> 42 
new_paramsD = copy.deepcopy(paramsD) 
new_paramsD["xopt"] = new_x_opt 

# 3 cases of hm: 
a1 = 0 # no hm 
a2 = 0.5 # low hm 
a3 = 1 # high hm 

# a1 --------------------------------------------

x_eq_ini = paramsD["xopt"] - a1*paramsD["sigma"] 
n_ini = get_neq(x_eq_ini,paramsD) 

new_x_eq = new_x_opt - a1*paramsD["sigma"] 
n_post = get_neq(new_x_eq,new_paramsD) 

# Note: here n_ini & n_post are equal since n_eq does not depend on xopt (this is not the case for sigma changes) 
# But how n_eq changes along the transition to the new ESS, i.e. from x_eq_ini to new_x_eq ? 

xL = np.linspace(x_eq_ini,new_x_eq,100)
n_transiL = list()
n_transiL.append(n_ini) 
n_transiL.append(n_ini) 

for elt in xL: 
	n_transiL.append(get_neq(elt,new_paramsD))

plt.subplot(131) 
plt.semilogx(n_transiL, label='no hm')


# a2 --------------------------------------------

x_eq_ini = paramsD["xopt"] - a2*paramsD["sigma"] 
n_ini = get_neq(x_eq_ini,paramsD) 

new_x_eq = new_x_opt - a2*paramsD["sigma"] 
n_post = get_neq(new_x_eq,new_paramsD) 

xL = np.linspace(x_eq_ini,new_x_eq,100)
n_transiL = list()
n_transiL.append(n_ini) 
n_transiL.append(n_ini) 

for elt in xL: 
	n_transiL.append(get_neq(elt,new_paramsD))

plt.semilogx(n_transiL, label='low hm')

# a3 --------------------------------------------

x_eq_ini = paramsD["xopt"] - a3*paramsD["sigma"] 
n_ini = get_neq(x_eq_ini,paramsD) 

new_x_eq = new_x_opt - a3*paramsD["sigma"] 
n_post = get_neq(new_x_eq,new_paramsD) 

xL = np.linspace(x_eq_ini,new_x_eq,100)
n_transiL = list()
n_transiL.append(n_ini) 
n_transiL.append(n_ini) 

for elt in xL: 
	n_transiL.append(get_neq(elt,new_paramsD))

plt.semilogx(n_transiL,label='high hm')

# show graphics 
plt.xlabel('log time')
plt.ylabel('n eq')
plt.title('Optimum shift')
legend = plt.legend(loc='lower center', shadow=True, fontsize='x-large')

# Environmental change: 2nd case -> season length

# A) Larger season length (warming) 
new_sigma = paramsD["sigma"] + 2 # 10 -> 12 
new_paramsD = copy.deepcopy(paramsD) 
new_paramsD["sigma"] = new_sigma 

# a1 --------------------------------------------

x_eq_ini = paramsD["xopt"] - a1*paramsD["sigma"] 
n_ini = get_neq(x_eq_ini,paramsD) 

new_x_eq =  paramsD["xopt"] - a1*new_paramsD["sigma"] 
n_post = get_neq(new_x_eq,new_paramsD) 

xL = np.linspace(x_eq_ini,new_x_eq,100)
n_transiL = list()
n_transiL.append(n_ini) 
n_transiL.append(n_ini) 

for elt in xL: 
	n_transiL.append(get_neq(elt,new_paramsD))

plt.subplot(132) 
plt.semilogx(n_transiL, label='no hm')


# a2 --------------------------------------------

x_eq_ini = paramsD["xopt"] - a2*paramsD["sigma"] 
n_ini = get_neq(x_eq_ini,paramsD) 

new_x_eq =  paramsD["xopt"] - a2*new_paramsD["sigma"] 
n_post = get_neq(new_x_eq,new_paramsD) 

xL = np.linspace(x_eq_ini,new_x_eq,100)
n_transiL = list()
n_transiL.append(n_ini) 
n_transiL.append(n_ini) 

for elt in xL: 
	n_transiL.append(get_neq(elt,new_paramsD))

plt.semilogx(n_transiL, label='low hm')

# a3 --------------------------------------------

x_eq_ini = paramsD["xopt"] - a3*paramsD["sigma"] 
n_ini = get_neq(x_eq_ini,paramsD) 

new_x_eq =  paramsD["xopt"] - a3*new_paramsD["sigma"] 
n_post = get_neq(new_x_eq,new_paramsD) 

xL = np.linspace(x_eq_ini,new_x_eq,100)
n_transiL = list()
n_transiL.append(n_ini) 
n_transiL.append(n_ini) 

for elt in xL: 
	n_transiL.append(get_neq(elt,new_paramsD))

plt.semilogx(n_transiL,label='high hm')

# show graphics 
plt.xlabel('log time')
plt.ylabel('n eq')
plt.title('Increase of the season length')
legend = plt.legend(loc='center right', shadow=True, fontsize='x-large')


# B) Shorter season length 
new_sigma = paramsD["sigma"] - 2 # 10 -> 12 
new_paramsD = copy.deepcopy(paramsD) 
new_paramsD["sigma"] = new_sigma 

# a1 --------------------------------------------

x_eq_ini = paramsD["xopt"] - a1*paramsD["sigma"] 
n_ini = get_neq(x_eq_ini,paramsD) 

new_x_eq =  paramsD["xopt"] - a1*new_paramsD["sigma"] 
n_post = get_neq(new_x_eq,new_paramsD) 

xL = np.linspace(x_eq_ini,new_x_eq,100)
n_transiL = list()
n_transiL.append(n_ini) 
n_transiL.append(n_ini) 

for elt in xL: 
	n_transiL.append(get_neq(elt,new_paramsD))

plt.subplot(133) 
plt.semilogx(n_transiL, label='no hm')


# a2 --------------------------------------------

x_eq_ini = paramsD["xopt"] - a2*paramsD["sigma"] 
n_ini = get_neq(x_eq_ini,paramsD) 

new_x_eq =  paramsD["xopt"] - a2*new_paramsD["sigma"] 
n_post = get_neq(new_x_eq,new_paramsD) 

xL = np.linspace(x_eq_ini,new_x_eq,100)
n_transiL = list()
n_transiL.append(n_ini) 
n_transiL.append(n_ini) 

for elt in xL: 
	n_transiL.append(get_neq(elt,new_paramsD))

plt.semilogx(n_transiL, label='low hm')

# a3 --------------------------------------------

x_eq_ini = paramsD["xopt"] - a3*paramsD["sigma"] 
n_ini = get_neq(x_eq_ini,paramsD) 

new_x_eq =  paramsD["xopt"] - a3*new_paramsD["sigma"] 
n_post = get_neq(new_x_eq,new_paramsD) 

xL = np.linspace(x_eq_ini,new_x_eq,100)
n_transiL = list()
n_transiL.append(n_ini) 
n_transiL.append(n_ini) 

for elt in xL: 
	n_transiL.append(get_neq(elt,new_paramsD))

plt.semilogx(n_transiL,label='high hm')


plt.xlabel('log time')
plt.ylabel('n eq')
plt.title('Decrease of the season length')
legend = plt.legend(loc='center right', shadow=True, fontsize='x-large')


# show graphics 
plt.show()


