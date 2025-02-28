try:
    with open("students.txt", "r") as file:
        print("Reading student information:")
        
        while True:
            student = [file.readline().strip() for _ in range(5)]
            if not student[0]: 
                break
            
            print(f"{student[0]}")
            print(f"{student[1]}")
            print(f"{student[2]}")
            print(f"{student[3]}")
            print(f"{student[4]}")
            print()  

except FileNotFoundError:
    print("Error: 'students.txt' not found.")
