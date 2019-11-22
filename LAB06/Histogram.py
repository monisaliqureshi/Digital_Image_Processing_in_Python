# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 20:53:18 2019

@author: Monis Ali
"""
import cv2
import matplotlib.pyplot as plt #importing matplotlib

# load an image in grayscale mode
img = cv2.imread('ex.png',0)
# calculate frequency of pixels in range 0-255
histr = cv2.calcHist([img],[0],None,[256],[0,256])

#show the plotting graph of an image
plt.plot(histr)
plt.show()


# import Numpy
import numpy as np
# read a image using imread
img = cv2.imread('do_nawab.png', 0)
# creating a Histograms Equalization
# of a image using cv2.equalizeHist()
equ = cv2.equalizeHist(img)
# stacking images side-by-side
res = np.hstack((img, equ))
# show image input vs output
cv2.imshow('image', res) 
cv2.waitKey(0)
cv2.destroyAllWindows()


image = cv2.imread('do_nawab.png', 0)

#manual histogram
def histogram(image):
    histog = []
    x=[]
    for i in range((image.max()+1)): 
        occ = (image==i).sum()
        histog = np.append(histog,occ)
        x = np.append(x,i)
    
    plt.stem(histog)
    plt.show()    
    return

histogram(img)
    
    
    
    
    
    
    
    