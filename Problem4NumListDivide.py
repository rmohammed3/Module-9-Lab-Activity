# Raheemuddin Mohammed
# 9/2/2025
# Problem 4: Append values divisible by 10 from 0 to 50 into a list.

tens = []
counter = 0

while counter <= 50:
    if counter % 10 == 0:
        tens.append(counter)
    counter += 1

print("Values divisible by 10 from 0 to 50:", tens)
