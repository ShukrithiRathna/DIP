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

def IFFT(x):
    F=[]
    #x = np.asarray(x, dtype=float)
    N = x.shape[0]
    for U in range(0,N):
        sum=0
        for y in range(0,N):
            sum=sum+(x[y]*(np.exp(2j * np.pi * U * y / N)))
        F.append(sum/N)
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
lena_phase = [] 
lena_mag = []

lena_phase=np.angle(Ftemp)
lena_mag=np.abs(Ftemp)
plt.imshow(lena_phase,cmap='gray')
# plt.show()

plt.imshow(lena_mag,cmap='gray')
# plt.show()

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
dog_phase = [] 
dog_mag = []

dog_phase=np.angle(Ftemp)
dog_mag=np.abs(Ftemp)
plt.imshow(dog_phase,cmap='gray')
# plt.show()

plt.imshow(dog_mag,cmap='gray')
# plt.show()

combined=np.multiply(lena_mag,np.exp(1j*dog_phase))
check = combined
M = combined.shape[0]
temp=[]
Ftemp = np.zeros((combined.shape[0],combined.shape[1]),dtype=complex)
for i in range(0,M):
    temp.append(IFFT(combined[i]))

Ftemp = np.array(temp)
FFtemp = np.zeros((combined.shape[0],combined.shape[1]),dtype=complex)

N = combined.shape[1]
for i in range(0,N):
    FFtemp[:,i] = IFFT(Ftemp[:,i])
combined=np.asarray(FFtemp)

plt.title('Lena mag + Dog Phase')
plt.imshow( np.real(combined),cmap='gray')
plt.show()