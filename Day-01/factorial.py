num = int(input("Enter a number : "))

def fact(num):
    fact=1
    while num != 0:
        fact = fact * num
        num = num - 1
    return fact

print("The factorial of a number : ",fact(num))
