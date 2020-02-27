import numpy as np
import cv2
import cmath
import matplotlib.pyplot as plt

lena = cv2.imread("lena.jpeg",0)
l = np.array(lena)
dog = cv2.imread("dog.png",0)
d = np.array(dog)

def FFT(x):
    F=[]
    #x = np.asarray(x, dtype=float)
    N = x.shape[0]
    for U in range(0,N):
        sum=0
        for y in range(0,N):
            sum=sum+(x[y]*(np.exp(-2j * np.pi * U * y / N)))
        F.append(sum)
    return(F)

temp=[]
Ftemp = np.zeros((l.shape[0],l.shape[1]),dtype=complex)

M = l.shape[0]

for i in range(0,M):
    temp.append(FFT(l[i]))

temp = np.array(temp)

N = l.shape[1]
for i in range(0,N):
    Ftemp[:,i] = FFT(temp[:,i])

lena_phase = [] 
lena_mag = []

lena_phase=np.angle(Ftemp)
lena_mag=20*np.log(np.abs(Ftemp))
plt.title('Lena phase')
plt.imshow(lena_phase,cmap='gray')
plt.show()
plt.title('Lena Mag')
plt.imshow(lena_mag,cmap='gray')
plt.show()

temp=[]
Ftemp = np.zeros((d.shape[0],d.shape[1]),dtype=complex)

M = d.shape[0]
print(d.shape)
for i in range(0,M):
    temp.append(FFT(d[i]))

temp = np.array(temp)

N = d.shape[1]
for i in range(0,N):
    Ftemp[:,i] = FFT(temp[:,i])

dog_phase = [] 
dog_mag = []

dog_phase=np.angle(Ftemp)
dog_mag=20*np.log(np.abs(Ftemp))
plt.title('Dog phase')
plt.imshow(,dog_phase,cmap='gray')
plt.show()
plt.title('Dog Mag')
plt.imshow('Dog Mag',dog_mag,cmap='gray')
plt.show()

