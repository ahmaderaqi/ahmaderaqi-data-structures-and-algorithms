import math
def reverseArray(arr):
    for i in range(math.ceil(len(arr)/2)):
        temp=arr[i]
        arr[i]=arr[len(arr)-1-i]
        arr[len(arr)-1-i]=temp
    print(arr)

ahmad=[1,2,3,4,5,6,7]
reverseArray(ahmad)