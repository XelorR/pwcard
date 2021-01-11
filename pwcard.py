import string
import random

random.seed(input("Please enter master password: "))
s = string.digits + string.ascii_letters + string.punctuation

print("\nHere is your password card\n")
print(" ", string.digits + string.ascii_lowercase)
for i in range(10):
    print(i, "".join(s[random.randint(0, len(s) - 1)] for _ in range(36)))
print()
