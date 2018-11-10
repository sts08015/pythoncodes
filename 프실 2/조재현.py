a = input()
tmp = a[0]
ans = []
for i in range(1,len(a)):
    if a[i]>'A' and a[i]<'Z':
        ans.append(tmp)
        tmp = a[i]
    else:
        tmp+=a[i]

ans.append(tmp)
print(ans)
    
    
