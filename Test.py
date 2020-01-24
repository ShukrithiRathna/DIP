import numpy as np
import cv2

import matplotlib.pyplot as plt
import skimage

img = cv2.imread("lena.jpg", 0)
'''
Mat noise = Mat(im.size(), CV_8U)
Scalar a(0);
Scalar b(20) ;
randn(noise,a,b);
imshow("noise",noise);
imshow("add",im + noise);
waitKey();'''
m = (50,50,50) 
s = (50,50,50)
cv2.randn(img,m,s)
cv2.imshow(img)