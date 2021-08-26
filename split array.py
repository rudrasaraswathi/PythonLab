def split(arr,k):
    arr = arr[k:] + arr[:k]
    return arr
k=2
arr = [10,12,15,18,20]
print("output array is:",split(arr,k))
