import numpy as np
import cv2
import cmath
import matplotlib.pyplot as plt

lena = cv2.imread("lena.jpeg",0)
l = np.array(lena)

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

LP = [] 
LM = []

# for i in range(0,M): 
#     T = [] 
#     A = [] 
#     for j in range(0,N): 
#         T.append(cmath.phase(Ftemp[i])) 
#         A.append(abs(Ftemp[i])) 
#         LP.append(T)
#         LM.append(A)
LP=np.angle(Ftemp)
LM=20*np.log(np.abs(Ftemp))
plt.imshow(LP)
plt.show()

plt.imshow(LM)
plt.show()
