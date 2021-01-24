f = open("writefile.txt",'a')
f.write("This is the First line...\n")
f.close()

#g = open("writefile.txt","rt")
#data = g.readlines()
#print(data)
#for line in g:
#    print(line)
#g.close()


with open("writefile.txt","rt") as g:
    for line in g:
        print(line)