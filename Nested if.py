def main():
    a = 70
    b = 2 + 3j

    if a > b.real:
        print(a)
    elif b > a:
        print(b)

    elif a == b:
        print("Both numbers are equal")
    else:
        print("Something went wrong. Please try again after sometime")


if __name__ == '__main__':
    main()
