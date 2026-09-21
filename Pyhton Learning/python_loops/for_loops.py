"""numbers = range(1, 1000)
total = 0

for num in numbers:
    if (num % 3 == 0) or (num % 5 == 0):
        total += num
        
print(f"Multiple of 3 or 5 = {total}")
"""

# Write a code to add the sum of odd square numbers within 1 and 787,000 numbers

square_total = 0
numbers = range(1, 787000)

for num in numbers:
    # Find even numbers
    even_num = num % 2 == 0
    
    # Get odd numbers
    if not even_num:
        odd_num = num
        square_num = odd_num ** 2
        square_total += square_num

print(square_total)
        
   