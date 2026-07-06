def are(*args):
    e=input("Enter data for 1D array (seperated by spaces): ")
    re=e.split()
    for r in re:
        slist.append(int(r))
    return args

def aver():
    suum=sum(slist)
    leen=len(slist)
    ave=suum/leen
    return ave

def multipled():
    minv=min(slist)
    maxv=max(slist)
    suum=sum(slist)
    l=len(slist)
    aav=sum(slist)/l
    return {"minv":minv,"maxv":maxv,"suum":suum,"aav":aav}

def facto(n):
    if n<=1:
        return 1
    return n*facto(n-1)

slist=[]

while 1<2:
    print("""
Welcome to the Data Analyzer and Transformer Program

Main Menu:
1. Input Data
2. Display Data Summary
3. Calculate Factorial
4. Filter Data by Threshold
5. Sort Data
6. Display Dataset Statistics
7. Exit Program
""")
    a=int(input("Enter your choice: "))
    if a==7:
        print("\nThank You for Using Data Analyzer and Transformer Program !")
        break
    elif a==1:
        are()
        print("\nData has been stored successfully!")
    elif a==2:
        print("Data Summary:")
        print(f"- Total elements: {len(slist)}")
        print(f"- Minimum Value: {min(slist)}")
        print(f"- Maximum Value: {max(slist)}")
        print(f"- Sum of all Values: {sum(slist)}")
        result=aver()
        print(f"- Average value: {result}")
    elif a==3:
        a=int(input("Enter number to find its factorial: "))
        print(f"\nFactorial of {a} is: {facto(a)}")
    elif a==4:
        b=int(input("Enter a threshold to filter out data above this value: "))
        tlist=[]
        for s in slist:
            if s>=b:
                tlist.append(s)
        print(f"Filtered Data (values >= {b})")
        print(tlist)
    elif a==5:
        print("Choose sorting options:")
        print("1. Ascending")
        print("2. descending")
        p=int(input("Enter your choice: "))
        if p==1:
            slist.sort()
            print("Sorted data in Ascending Order:")
            print(slist)
        elif p==2:
            slist.sort(reverse=True)
            print("Sorted data in Descending Order:")
            print(slist)
        else:
            print("Enter 1 or 2 only !!")
    elif a==6:
        print("Data Statictics:")
        mul=multipled()
        print(f"- Minimum Value: {mul["minv"]}")
        print(f"- Maximum Value: {mul["maxv"]}")
        print(f"- Sum of all Values: {mul["suum"]}")
        print(f"- Average of Values: {mul["aav"]}")