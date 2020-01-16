
'''def most_frequent(List): 
    counter = 0
    num = List[0] 
      
    for i in List: 
        curr_frequency = List.count(i) 
        if(curr_frequency> counter): 
            counter = curr_frequency 
            num = i 
  
    return(num)'''
import random

def CountFrequency(my_list): 
    global mode
    # Creating an empty dictionary  
    freq = {} 
    for item in my_list: 
        if (item in freq): 
            freq[item] += 1
        else: 
            freq[item] = 1
    temp_max=0
    for key, value in freq.items(): 
        print ("% d : % d"%(key, value)) 
        if value>=temp_max:
            temp_max=value
            mode=key
    #print(freq)

  
mat=[]
arr=[]
num=int(input("Enter size of matrix: "))
for i in range(0,num):
    lst=[]
    for j in range(0,num):
       
        item=random.randint(0,30)
        lst.append(item)
        lst.sort()
        arr.append(item)
    mat.append(lst)
mat.sort()
arr.sort()

Sum=0
Max=0
for row in mat:
    if(max(row)>Max):
        Max=max(row)
    Sum+=sum(row)
mean=Sum/5
median=arr[13]

#mode=most_frequent(arr)

Mean = Sum/len(arr)
SSE = 0
for i in range(len(arr)):
    SSE = (arr[i]-Mean)**2
StdDev = (SSE/len(arr)-1)**(1/2)
mode=0

print(mat)
print("Sum:", Sum,"Max:",Max)
print("Mean:",mean,"Median:",median)
print("Standard Deviation:",StdDev)
print("Frequency distribution:")
CountFrequency(arr)
print("Mode:",mode) 


