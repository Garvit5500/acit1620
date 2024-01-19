"""
to run a file in vs code for python using the terminal
1. create your file in vs cosde 
2. right-click on the tab for the tab for that file, select and copy path
3. paste the file in the terminal and remove the filename from it 
4. to run the file now add filename.py




if you are in the pyhton repl
you should see this prompt: 
>>>
exit out using >>> exit()
"""


"""

type() returns the current data type of the variable in the brackets
data types
int (whole numbers)
float (decimal numbers)
str(string)- any sequence of characters inside of single or double qoutes
bool (boolean) - true/false
none (null/empty)
isdigit() returns wheather a string can be converted into a numeric value or not 
"""



"""
strings (sequence type)
think of string as a list of individual charachters
len()-to get the length of thhe string

"""
"""
print(len (course))# should print 9 "space is also considered a character"
print(f'the length of the string "ACIT 1515" is {len(course)}.')
print(course[1]) # prints C (0 i sthe first character, 1 is the second character)
print(course[-1]) # prints 5 (-1 for the last character, -2 for the second last)
print("CIT" in course) # print true
print("fswd" not in course)# prints true

"""
"""

counter = 0

counter += 1 # work same as the command given counter = counter+1
print(counter) # equivvalent to counter = counter * 2
counter *= 2
print(counter)

print(counter ==2)# prints true
course = "ACIT 1515"
coursenumber = 1515
print(coursenumber, type(coursenumber)) # 1515 is <class int>

# print(int("BCIT")) # does not work raise ValueError which crashes the script (pyhton cannot convert bcit into a number) 

print("BCIT".isdigit()) # false
print("5".isdigit()) # true

isTuesday = True

"""
"""
f-string a way that includes the variables in the print commanad

"""

today = "Tuesday"
time= "morning"
"""
conditional (if) statements

"""
"""
if today == "Tuesday":
    print('yeah it is Tuesday')
    # anything indented the if statement is part of the block
    print('still inside the if block')
"""
# if len(today) > 6 :

# if today.isdigit:

# if today == "":
    
# print("after the block")


response = input('please enter your password: ' )
print(f"your response was {response}")
response = input("please enter the year: ") # input is always returns a string,if we need to subtract a value from it, frist convert it into an int
# it has been x years since the pyhton was first used
if response.isdigit():
    response = int(response)

    print(f"it has been {response - 1989} years since python was first used")
else:
    print("you must enter an integer")

print("end of the script")
