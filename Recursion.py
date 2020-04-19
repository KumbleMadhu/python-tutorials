def factorial(n):
    # Function to find factorial #

    if n == 1:
        return 1
    else:
        return (n * factorial(n - 1))


print("15!= ", factorial(15))
