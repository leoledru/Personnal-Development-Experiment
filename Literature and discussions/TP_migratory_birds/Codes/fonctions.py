#!/usr/bin/env python
# -*- coding: utf-8 -*-

def rx_f(x,r0,x_opt,sigma):
	"""reproductive success function

	:x: arrival date  
	:r0: reproductive factor 
	:x_opt: optimal date 
	:sigma: length of the reproductive period 
	:returns: R(x)

	"""
	import numpy as np 
	return r0*np.exp(-(x-x_opt)**2/sigma**2)


def get_neq(x,par):
	"""get n* 

	:x (real): arrival date  
	:par (dict): dict of params: "xopt" "sigma" "r0" "a" "p" "K" ...  
	:returns: n* 

	"""
	
	return par["K"]*rx_f(x,par["r0"],par["xopt"],par["sigma"])/(1-par["p"]) 



