arr = [9,8,3,4,7]

print("array:",arr)

for i in range(1,len(arr)):
        j = i-1
        key = arr[i]
        while j>=0 and  arr[j]>key:
                arr[j+1] = arr[j]
                j-=1
        arr[j+1] = key
        print("%d step : " %i, arr)

print(arr)
                
