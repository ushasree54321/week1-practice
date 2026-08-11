n = int(input("Enter number: "))

even_count = 0
odd_count = 0

for i in range(1, 11):
    result = n * i

    if result % 2 == 0:
        print(f"{n} x {i} = {result} - Even")
        even_count += 1
    else:
        print(f"{n} x {i} = {result} - Odd")
        odd_count += 1

print("Even Results:", even_count)
print("Odd Results:", odd_count)