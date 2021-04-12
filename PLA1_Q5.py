# Ques5:
# To create a program that ask the user for a number and determine whether the number is prime or not.

def Prime(num):
    if num > 1:  
        for i in range(2,num//2):  
            if (num % i) == 0:  
                print(num,"is not a prime number")  
                print(i,"times",num//i,"is",num) 
                break
        else:  
            print(num,"is a prime number")  
    else:
        print("number should be greater than 1")

num = int(input('Enter a number : '))
Prime(int(num))


