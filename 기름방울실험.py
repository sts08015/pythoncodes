while True:
    eta = float(input())
    a = ((8.22*0.001/(2*101.3*1000))**2 + (9*1.841*0.00001)*eta*0.00001/(2*9.81*886))**0.5
    a -= ((8.22*0.001)/(2*101.3*1000))
    print(a)
