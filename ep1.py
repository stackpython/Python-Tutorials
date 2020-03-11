# Topic: Python Grade Calculation
# Author: Sonny StackPython
# Date Created: March 10, 2020
# Facebook Page: StackPython

"""
Line 19: Define variable called "guide_message" to store value "Welcome:..."
Line 20: Print navigation message "Please type your name:"
Line 21: Define variable called "inp_name" to get an input name from keyboard
Line 22: Print out your name
Line 23: Define variable called "notice_message" to finally show grade you got
Line 26: store grade letter grade into list
Line 27: Print "Please type..."
Line 29: Input score(your score)
Line 30: Input score(score that is converted from str(default) to be int)
Line 32 - 48: Simple If-Else statements. Pay your attention to this!!
The final line: if your score is out of scope e.g. more than 100; print "your sc..."
"""

guide_message = "Welcome:"
print("Please type your name:")
inp_name = input()
print(guide_message, inp_name)

notice_message = "You got:"
result = ['A', 'B', 'C', 'D', 'F']
print("Please type your score here:")

raw_score = input()
score = int(raw_score)

if 0 == score < 50:
    print(notice_message, result[4])

elif 50 == score < 55:
    print(notice_message, result[3])

elif 54 < score < 65:
    print(notice_message, result[2])

elif 64 < score < 75:
    print(notice_message, result[1])

elif 74 < score < 101:
    print(notice_message, result[0])

else:
    print("your score is out of the scope")
















