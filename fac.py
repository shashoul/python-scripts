import sys

def fac(num):
    fac=1
    if type(num) != int:
        return -1
    for i in range(1,num+1):
        fac*=i
    return fac

def facc(num):
    if not isinstance(num,int):
        return -1
    fac=num
    for n in range(num-1,0,-1):
        fac*=n
    return fac

def main():
    print(fac(int(sys.argv[1])))
    print(facc(int(sys.argv[1])))

if __name__ == "__main__":
    main()