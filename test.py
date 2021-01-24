def function(y):
    print(id(y))
    y=10


def testlist(mylist):
    print(id(mylist))
    mylist[0]=1
    

x=5
print(x)
print(id(x))
function(x)
print(x)
print("------------------")

items = [2,4,6]
print(items)
print(id(items))
testlist(items)
print(items)


x = (1,2)
print(x)

val = "HaHaHa"
print(f"The val is {val}")

l = [4,21,1]
print(id(l))
l.sort()
print(id(l))