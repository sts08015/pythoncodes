arr = [9,8,3,4,7]
print("array: ",arr)

for i in range(len(arr)):
    for j in range(len(arr)-i-1):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
        print("step %d : " %(i+1),arr)
