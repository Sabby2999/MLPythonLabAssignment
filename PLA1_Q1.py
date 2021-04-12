# Ques1:
# To create a program that asks the user to enter their name and their age 
# and prints out a message addressed to them that tells them the year that 
# they will turn 100 years old. Additionally, the program asks the user for 
# another number and prints out that many copies of the previous message on 
# separate lines.

from datetime import datetime
name = input('Enter your name : ')
age = int(input('Enter your age : '))
year = int((100-age) + datetime.now().year)
copies = int(input('How many copies of the above message do you want? : '))
msg = name + " will turn 100 years old in " + str(year) + "\n" 
print(msg * copies)
