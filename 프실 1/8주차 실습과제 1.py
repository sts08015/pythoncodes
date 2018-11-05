import random as r
outfile = open("C:\\Users\\sts08\\Desktop\\test.txt","w")
for i in range(10):
    a = r.randint(1,100)
    outfile.write("%d " %a)
outfile.close()

infile = open("C:\\Users\\sts08\\Desktop\\test.txt","r")
for line in infile:
    print(line,end = " ")

infile.close()

        
