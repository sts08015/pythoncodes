def find_nearest(arr,n):
    x = []
    k = 0x7fffffff
    for i in range(len(arr)):
        x.append(abs(arr[i] - n))
    for i in range(len(arr)):
        if k>x[i]:
            k = x[i]
    for i in range(len(arr)):
        if x[i] == k:
            print("%d" %arr[i],end=" ")    

    
n = int(input("total applicant="))
applicant = [154,735,632,657,432,634,546,150,324]
find_nearest(applicant,n)
