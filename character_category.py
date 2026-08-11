text = input("Enter text: ")

uppercase = 0
lowercase = 0
digits = 0
spaces = 0
others = 0

for ch in text:
    if ch.isupper():
        uppercase += 1
    elif ch.islower():
        lowercase += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1
    else:
        others += 1

print("\nUppercase Letters:", uppercase)
print("Lowercase Letters:", lowercase)
print("Digits:", digits)
print("Spaces:", spaces)
print("Other Characters:", others)