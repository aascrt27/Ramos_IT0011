first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = input("Enter your age: ")
full_name = first_name + " " + last_name
sliced_name = first_name[:3]
greeting = f"Greeting Message! Hello, {sliced_name}! Welcome. You are {age} years old."

print("\nFull name:", full_name)
print("Sliced name:", sliced_name)
print(greeting)