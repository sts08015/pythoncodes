arr = [9,8,3,4,7]
print("array: ",arr)

for i in range(len(arr)):
    indexMin = i
    for j in range(i,len(arr)):
        if arr[indexMin] > arr[j]:
            indexMin = j
    arr[i],arr[indexMin] = arr[indexMin],arr[i]
    print("%d step : " %(i+1), arr)
