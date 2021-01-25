from random import randrange


def main():
    number = randrange(100)
    print(number)
    while True:
        try:
            guess = int(input("? "))
        except ValueError:
            continue
        if guess == number:
            print("You win!")
            break


if __name__ == "__main__":
    main()