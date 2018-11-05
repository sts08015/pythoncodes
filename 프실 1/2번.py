n = int(input())
dap = 0

for i in range(n+1):
    k = i
    while(k>0):
       dap += k%10
       k //= 10

print("숫자의 각 자리수의 합계= %d" %dap)
