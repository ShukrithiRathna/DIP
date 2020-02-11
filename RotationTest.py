import cv2
import math
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread("Pisa.jpeg",0)
cv2.imshow('Original',img)
cv2.waitKey(0)

print(img.shape)
for angle  in range(3,15,3):
    Radians=(angle*math.pi/180)
    hgt=img.shape[0]
    wdt=img.shape[1]

    #print(img.shape)
    new=np.zeros([224,225],dtype=np.uint8)
    rotated=np.zeros([224,225],dtype=np.uint8)
    # cv2.imshow('original',img)
    # cv2.waitKey(0)

    for i in range(224):
        for j in range(201):
            x_cord=int(i*math.cos(Radians)-j*math.sin(Radians))
            y_cord=int((i*math.sin(Radians)+j*math.cos(Radians)))
            if(x_cord<224 and y_cord<225 and x_cord>0 and y_cord>0):
                new[x_cord][y_cord] = img[i][j];
                #rotated[x_cord][y_cord] = img[i][j];

    #cv2.imshow('Rotated w/o interpolation',rotated) #rotated image without bilinear interpolation
    cv2.waitKey(0)
    # cv2.destroyAllWindows()

    
    cv2.imshow('Rotated by '+str(angle) + '',new)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
