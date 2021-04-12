# Ques4:
# To create a program that takes a list and returns a new list that contains all the elements 
# of the first list minus all the duplicates. Write two different functions to do this - one 
# using a loop and constructing a list, and another using sets.

#using for loop & lists 
orig_list = ['Hello', 'Hiii', 'Okay', 'Byee', 'Hey!', 'See yaa!', 'Hello', 'Byee', 'Hey']
new_list =[]
def doing_Something(orig_list):
    for i in orig_list:
        if i not in new_list:
            new_list.append(i)
    return new_list
print("\nUsing for loop & lists")
print(doing_Something(orig_list))

#using sets 
orig_list = ['Hello', 'Hiii', 'Okay', 'Byee', 'Hey!', 'See yaa!', 'Hello', 'Byee', 'Hey']
print("\nUsing sets")
print(list(set(orig_list)))

