print("1. Check if string is palindrome")
print("2. Find a factorial of a number")
choice = int(input("Enter a choice : "))
if choice == 1:
    string = input("Enter a string: ")
    revStr = string[-1::-1]
    if revStr == string:
        print("String is palindrome")
    else:
        print("Not Palindrome")
elif choice == 2:
    num = int(input("Enter a number: "))
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    print("factorial :", fact)



