import numpy as np
import cv2


import matplotlib.pyplot as plt
import skimage

# Load in grayscale mode
lena = cv2.imread('lena.jpeg', 0)

#print matrix
print(lena)

plt.gray()
plt.imshow(lena)
plt.show()

def plotnoise(lena, mode, r, c, i):
    plt.subplot(r,c,i)
    if mode is not None:
        gimg = skimage.util.random_noise(lena, mode=mode)
        plt.imshow(gimg)
    else:
        plt.imshow(lena)
    plt.title(mode)
    plt.axis("off")

plt.figure(figsize=(30,40))
r=3
c=2
plotnoise(lena, None, r,c,1)
plotnoise(lena, "gaussian", r,c,2)
plotnoise(lena, "salt", r,c,3)
plotnoise(lena, "pepper", r,c,4)
plotnoise(lena, "s&p", r,c,5)
plotnoise(lena, "speckle", r,c,6)
plt.show()