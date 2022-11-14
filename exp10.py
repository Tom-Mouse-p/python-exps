a = int(input("Any number A > "))
b = int(input("Any number B > "))
c = int(input("Any Number C > "))
d = 0
e = 0
try:
    d = a / b
    e = a * c
    assert c != 0
    print(d, e)
except ZeroDivisionError:
    print("Cannot divide by zero")
except AssertionError:
    print("C cannot be 0, because E will turn 0")
finally:
    print("Bye!")


