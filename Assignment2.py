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

def plotnoise(lena_gray, mode, row, col, i):
    plt.subplot(row,col,i)
    if mode is not None:
        gimg = skimage.util.random_noise(lena_gray, mode=mode)
        plt.imshow(gimg)
    else:
        plt.imshow(lena_gray)
    plt.title(mode)
    plt.axis("off")

plt.figure(figsize=(30,40))
row=3
col=2
plotnoise(lena_gray, None, row,col,1)
plotnoise(lena_gray, "gaussian", row,col,2)
plotnoise(lena_gray, "salt", row,col,3)
plotnoise(lena_gray, "pepper", row,col,4)
plotnoise(lena_gray, "s&p", row,col,5)
plotnoise(lena_gray, "speckle", row,col,6)
plt.show()