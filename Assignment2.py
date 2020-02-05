
import cv2
import numpy as np
from skimage.util import random_noise

img = cv2.imread('lena.jpeg')
cv2.imshow('ena',img)

img_gray = cv2.imread('lena.jpeg',0)
cv2.imshow('Lena_Gray',img_gray)
cv2.waitKey(0)

for x in range(6):
    temp = 0
    for y in range(5 * (x + 1)):
        noise_img = random_noise(img,mode='gaussian',mean=0,var=0.01)
        temp += noise_img
    cv2.imshow('Lena_Gray ' + str(x),temp/(5*(x + 1)))
cv2.waitKey(0)
cv2.destroyAllWindows()

for x in range(6):
    temp = 0
    for y in range(5 * (x + 1)):
        noise_img = random_noise(img,mode='s&p',amount=0.1)
        temp += noise_img
    cv2.imshow('Lena_Gray ' + str(x),temp/(5*(x + 1)))
cv2.waitKey(0)
cv2.destroyAllWindows()

for x in range(6):
    temp = 0
    for y in range(5 * (x + 1)):
        noise_img = random_noise(img,mode='speckle',mean=0,var=0.01)
        temp += noise_img 
    cv2.imshow('Lena_Gray ' + str(x),temp/(5*(x + 1)))
cv2.waitKey(0)
cv2.destroyAllWindows()

