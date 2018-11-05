a = input("input file name: ")
infile = open("C:\\Users\\sts08\\Desktop\\%s" %a,"r")
cnt = 0
for line in infile:
    line = line.rstrip()
    w_list = line.split()
    for c in w_list:
        cnt+=len(c)
infile.close()

print("There are %d letters" %cnt)
