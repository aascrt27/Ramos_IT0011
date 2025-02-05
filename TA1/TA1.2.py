input_string = input("Enter a string: ")
digit_sum = 0

for char in input_string:
    if char.isdigit():
        digit_sum += int(char) 

print(f"The sum of the digits is: {digit_sum}")