'''Find the number of steps needed: 
Write a program to find the number of steps needed to perform the following operation on a

number:

1. Input will be a 4-digit number including 0 e.g. 1234, 0345

2. Make two numbers by arranging the digits in ascending and descending order

3. Subtract the smaller number from the larger number

4. Repeat the process with the new number until we reach a number that has been processed before

5. Return the number of steps taken to reach an already processed number

Examples
Input: 1234
Output: 4

'''



def find_number_steps(num):
    seen_numbers = set()
    steps = 0

    while num not in seen_numbers:
        seen_numbers.add(num)
        # Convert the number to a list of digits and sort
        digits = list(str(num).zfill(4))  # Use zfill to handle leading zeros in 4-digit numbers
        ascending = int("".join(sorted(digits)))       # Ascending order number
        descending = int("".join(sorted(digits, reverse=True)))  # Descending order number
        
        # Calculate the new number by subtracting ascending from descending
        num = descending - ascending
        steps += 1

    return steps

print(find_number_steps(1234))  # Expected output: 4
