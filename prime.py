
def findPrimeNumber(number):
    if number > 1 :
        for i in range(2,number):
            if number%i == 0 :
                return 0
    return 1

def main():
    number = int(input("Enter a Number:"))

    isPrime = findPrimeNumber(number)

    if isPrime:
        print("Prime Number!!!")
    else:
        print("Not Prime Number!!!")

if __name__ == "__main__":
    main()