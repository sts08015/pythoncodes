v = float(input("속도를 입력하시오(c빼고) : " ))
c = 2.998*(10**8)
v = v*c
r = 1/((1-(v/c)**2)**0.5)
print(r)
