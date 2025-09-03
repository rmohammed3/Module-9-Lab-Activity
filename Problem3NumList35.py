# Raheemuddin Mohammed
# 9/2/2025
# Problem 3: Continuously ask user for numbers and add them to a list until the sum exceeds 100.

numbers = []
total = 0

while total <= 100:
    num = int(input("Enter a number: "))
    numbers.append(num)
    total += num

print("Numbers entered:", numbers)
print("Total sum:", total)
