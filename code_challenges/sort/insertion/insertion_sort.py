def insertion_sort(arr):
    for i in range(len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key
    return arr

arr2=[2,3,5,7,13,11]
arr1=insertion_sort(arr2)
print(arr1)