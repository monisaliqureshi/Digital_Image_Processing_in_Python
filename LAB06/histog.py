# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 12:32:44 2019

@author: Monis Ali
"""
import numpy as np
import matplotlib.pyplot as plt #importing matplotlib

def histogram(image,levels):
    histog = []
    x=[]
    for i in range(levels): 
        occ = (image==i).sum()
        histog = np.append(histog,occ)
        x = np.append(x,i)
    
    plt.stem(x,histog)
    plt.show()    
    return