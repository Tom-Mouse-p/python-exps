import sys

a = int(sys.argv[1])
b = int(sys.argv[2])

a = a + b
b = a - b
a = a - b
print("swapped number ", a, b)

if a > 0:
    print("Positive")
elif a < 0:
    print("Negative")
else:
    print("Zero")

