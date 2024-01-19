current_year = input("please enter the current year: ")
if len(current_year)>0:
    
    current_year= int(current_year)
responded = False



birth_year = input("please enter your birth year: ")
if len(birth_year)>0:
    responded = True


    

if birth_year.isdigit():
    birth_year= int(birth_year)
    print(f"you are {current_year-birth_year} years old")
print("")    

fave = input("please enter your favorite number: ")


if len(fave)>0:
    responded = True

if fave.isdigit():
    fave= int(fave)
    print(f"your favorite number is {fave}")
    fave=int(fave)
    print(f"your favorite number devided by 2 is {fave/2}")
    if fave%2==0:
        print(f"your favorite number is even")
    else:
        print("your favorite number is odd")
        
print("")

name = input("please enter your name: ")
if len(name)>0:
    responded= True
    print(f"your name is {len(name)} characters long")

print("")

n= len(name)

i=0
letter = input("please enter a letter: ")
if len(letter)>0:
    responded = True
if len(letter)>0 and len(letter)<2:
  if letter in name:
    print(f"your name has the leter {letter}")
  else:
    print(f"your name doesnot have letter {letter}")

if responded:
    print("thank you for responding")


print("end of the script")