print()
print("welcome to the interactive personal data collector by ajay!😇")
print()

name = str(input("please enter your name:"))
age = int(input("please enter your age:"))
height = int(input("please enter your height in meters:"))
favnum =int( input("please enter your favourite number:"))
print()

print("thank you! here is the information we collected:😊")

print()

print("name:",name,('type:',type(name),"memory address:",id(name)))
print("age:",age,('type:',type(age),"memory address:",id(age)))
print("heigh:",height,('type:',type(height),"memory address:",id(height)))
print("favourite number:",favnum,('type:',type(favnum),"memory address:",id(favnum)))
print()

a =(2025 - age)

print("your birthday year is approximately:",a,"(based on your age of)",age)
print()

print("thank you for using the personal data collector by ajay.Goodbye!👋")

