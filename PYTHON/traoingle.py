#RIGHT ANGLED TRIANGLE

rows = int(input("Enter the raight angle traingle of rows: "))
for i in range(1, rows + 1):
    print("*" * i)


#LEFT ANGLED TRIANGLE

rows = int(input("Enter the left angle traingle of rows: "))
for i in range(1, rows + 1):
    spaces = rows - i
    stars = i
    print(" " * spaces + "*" * stars)

#INVERTED RIGHT ANGLED TRIANGL

rows = int(input("Enter the inverted right angle traingle of rows: "))
for i in range(rows, 0, -1):
    print("*" * i)

#INVERTED LEFT ANGLED TRIANGL

rows = int(input("Enter the inverted left angle traingle  of rows: "))
for i in range(rows, 0, -1):
    spaces = rows - i
    stars = i
    print(" " * spaces + "*" * stars)
