#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np 

import matplotlib.pyplot as plt 
# https://matplotlib.org/3.1.1/index.html
# legend: https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.legend.html

import copy # pour copier un dict de façon complètement indépendante 
# https://www.science-emergence.com/Articles/Copier-un-dictionnaire-sous-python/

from fonctions import* 

# dict for default param values  
# xopt: optimal arrival date for maximizing reproductive succes 
# sigma: length of the reproductive period 
# r0: maximal reproductive output 
# a: competition intesity 
# p: probability or survival to the next year 
# K: number of territories 
paramsD = {"xopt":50, "sigma":10, "r0":2.5, "a":0, "p":0.2, "K":5}

# different values of hm for different x_eq / n_eq values 
aA = np.linspace(0,2,100)
hmL = list()
x_eqL = list() 
nL = [] 
ndisturb_xoptL = [] 
ndisturb_sigmaL = [] 

for elt in range(len(aA)): 
	hmL.append(aA[elt]*paramsD["sigma"]) 
	x_eqL.append(paramsD["xopt"]-hmL[elt]) 	
	
	paramsD["a"] = aA[elt] 
	nL.append(get_neq(x_eqL[elt],paramsD)) 
	
	# not clean but functional 
	params_tempD = copy.deepcopy(paramsD) 	
	params_tempD["xopt"] = paramsD["xopt"] - 5  
	ndisturb_xoptL.append(get_neq(x_eqL[elt],params_tempD)) 

	# idem for sigma  
	params_tempD = copy.deepcopy(paramsD)	
	params_tempD["sigma"] = paramsD["sigma"] + 5 
	ndisturb_sigmaL.append(get_neq(x_eqL[elt],params_tempD)) 




# graphics outputs



plt.subplot(131) 
plt.plot(hmL,nL)
plt.xlabel('Historical mismatch')
plt.ylabel('n eq') 


plt.subplot(132)
plt.plot(hmL,nL, label='non disturbed') 
plt.plot(hmL,ndisturb_xoptL, label='disturbed')
plt.xlabel('Historical mismatch')
plt.ylabel('n eq') 
legend = plt.legend(loc='lower left', shadow=True, fontsize='x-large')

plt.subplot(133)
plt.plot(hmL,nL, label='non disturbed')
plt.plot(hmL,ndisturb_sigmaL, label='disturbed')
plt.xlabel('Historical mismatch')
plt.ylabel('n eq') 
legend = plt.legend(loc='lower left', shadow=True, fontsize='x-large')


plt.savefig('figure_immediate_effects.png',dpi=100)
#plt.show()




