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
# Ftemp=np.fft.fft2(l)
print(Ftemp.shape)
LP = [] 
LM = []

LP=np.angle(Ftemp)
LM=np.abs(Ftemp)
plt.imshow(LP,cmap='gray')
plt.show()

plt.imshow(LM,cmap='gray')
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

# Ftemp=np.fft.fft2(d)
DP = [] 
DM = []

DP=np.angle(Ftemp)
DM=np.abs(Ftemp)
plt.imshow(DP,cmap='gray')
plt.show()

plt.imshow(DM,cmap='gray')
plt.show()

combined=np.real(np.multiply(LM,np.exp(1j*DP)))

plt.imshow(np.real(np.fft.ifft2(combined)),cmap='gray')
plt.show()