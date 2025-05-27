number = int(input("Enter the number: "))
def factorial(number):
    if number<2:
        return 1
    else:
        return number * (factorial(number-1))
result = factorial(number)
print("Factorial of", number, "is", result)