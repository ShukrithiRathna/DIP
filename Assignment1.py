import random

#Input size of the matrix 
rows = int(input("Enter number of rows"))
cols = int(input("Enter number of columns"))
size = (rows*cols)

#Define range of matrix elements here
start = 0
end = 10

#Populate the matrix with random values
matrix = [[random.randint(start,end) for r in range(rows)] for c in range(cols)]

#Convert the matrix to sorted list
matrix_arr = []
for r in matrix:
    for item in r:
        matrix_arr.append(item)
matrix_arr.sort()

#Sum of all the elements 
Sum = sum(matrix_arr)

#Average of the matrix
Mean = Sum/size

#50% of the matrix
if(size%2==0):
    Median = (matrix_arr[size//2] + matrix_arr[(size//2-1)])/2
else:
    Median = matrix_arr[size//2]
    
#Maximum value of a sorted list
Max = matrix_arr[size-1]

#Finding the frequency count using a dictionary
max_count = 0
freq_count = {}
for item in matrix_arr:
    if item in freq_count:
        freq_count[item]+=1
    else:
        freq_count[item]=1
    if freq_count[item] > max_count:
        max_count = freq_count[item]
        
#Capturing multiple modes if it exists
Mode = []
for key,value in freq_count.items():
    if value == max_count:
        Mode.append(key)
        
#Deviation from mean 
variance = 0
for item in matrix_arr:
    variance += (item-Mean)**2
variance = variance/size

#OUTPUT
print("MATRIX")
for item in matrix:
    print(*item,sep=' ') 
print("Sum of the matrix :",Sum)
print("Maximum element in the matrix :",Max)
print("Mean of the matrix :", Mean)
print("Median of the matrix :",Median)
print("Mode of the matrix :",*Mode)
print("Frequency count of the Matrix :")
for key,value in freq_count.items():
    print(key," : ",value)
print("Variance of the Matrix :",variance)