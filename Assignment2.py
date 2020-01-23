import numpy as np
import cv2


import matplotlib.pyplot as plt
import skimage

# Load in grayscale mode
lena = cv2.imread('lena.jpeg')

#print matrix
print("Lena:",lena)
plt.imshow(lena)
plt.show()

lena_gray=cv2.imread('lena.jpeg',0)
print(lena_gray)
plt.gray()
plt.imshow(lena_gray)
plt.show()

def plotnoise(lena_gray, mode, r, c, i):
    plt.subplot(r,c,i)
    if mode is not None:
        gimg = skimage.util.random_noise(lena_gray, mode=mode)
        plt.imshow(gimg)
    else:
        plt.imshow(lena_gray)
    plt.title(mode)
    plt.axis("off")

plt.figure(figsize=(30,40))
r=3
c=2
plotnoise(lena_gray, None, r,c,1)
plotnoise(lena_gray, "gaussian", r,c,2)
plotnoise(lena_gray, "salt", r,c,3)
plotnoise(lena_gray, "pepper", r,c,4)
plotnoise(lena_gray, "s&p", r,c,5)
plotnoise(lena_gray, "speckle", r,c,6)
plt.show()