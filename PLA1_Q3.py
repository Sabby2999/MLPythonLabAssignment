# Ques3:
# To create a program that asks the user how many Fibonacci numbers
# to generate and then generates them.

def fibonacci(num):
    a = 1
    b = 1
    if (num < 1):
        return
    print (a, end=" ")
    for i in range(1, num):
        print (b, end=" ")
        c = a + b
        a = b
        b = c
num = int(input("How many fibnocci numbers to generate ? : "))    
fibonacci(num)


