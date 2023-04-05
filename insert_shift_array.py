final_arr=[]
import array
import math
def insertShiftArray(arr,number):
    for i in range(math.ceil(len(arr)/2)+1):
        if(i== math.ceil(len(arr)/2) ):
            final_arr.append(number)
            
        else:
            final_arr.append(arr[i])
        
    for j in range(math.ceil(len(arr)/2)+1,len(arr)+1):
        final_arr.append(arr[j-1])
    return final_arr

arr=[1,2,3,4,5,6]
result=insertShiftArray(arr,10)
print(result)

