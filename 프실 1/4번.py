arr=['black','brown','red','orange','yellow','green','blue','violet','grey','white']
x,y,z=input().split()
k = len(arr)
for i in range(k):
    if arr[i][:2] == x[:2]:
        result = i
result *= 10
for i in range(k):
    if arr[i][:2] == y[:2]:
        result += i
for i in range(k):
    if arr[i][:2] == z[:2]:
        result *= (10**i)

print(result)
