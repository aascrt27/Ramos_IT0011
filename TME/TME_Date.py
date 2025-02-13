from datetime import datetime

date_input = input("Enter the date (mm/dd/yyyy): ")

try:
    date_object = datetime.strptime(date_input, "%m/%d/%Y")
    readable_date = date_object.strftime("%B %d, %Y")
    
    print(f"Date Output: {readable_date}")
except ValueError:
    print("Invalid date format! Please enter the date in mm/dd/yyyy format.")