# Ques2:
# To create a program that prints out all the elements of the given list 
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] 
# that are less than a number given by the user in a single line of code.

actual_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
user_list = []
num = int(input('Enter a number : '))
for item in actual_list:
    if item < num:
        user_list.append(item)
print ('Numbers smaller than %s are'  % (num))
print(user_list)

#Writing above in one line of code
actual_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
num = int(input('Enter a number : '))
new_list = []
[new_list.append(i) for i in actual_list if i < num]
print(new_list)

