last_name = input("Last name: ")
first_name = input("First name: ")
age = input("Age: ")
contact_number = input("Contact Number: ")
course = input("Course: ")
student_info = f"""Last Name: {last_name}
First Name: {first_name}
Age: {age}
Contact Number: {contact_number}
Course: {course}
"""

with open("students.txt", "a") as file:
    file.write(student_info + "\n")

print("Student information has been saved to 'students.txt'.")
