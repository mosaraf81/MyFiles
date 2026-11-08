# Task-2: Student Grade Calculator


# Required Student Information
name = input("Enter student name: ")
math = float(input("Enter Math marks: "))
english = float(input("Enter English marks: "))
python = float(input("Enter Python marks: "))


# Logical outline

if (math > 100 or math < 0) or (english > 100 or english < 0) or (python > 100 or python < 0):
    print(f"Marks is invalid: Marks must not be less than 0 and greater than 100.")
else:
    average = (math + english + python) / 3

    if (average >= 80):
        Grade = "A+" 
    elif (average >= 70):
        Grade = "A"
    elif (average >= 60):
        Grade = "A-"
    elif (average >= 50):
        Grade = "B"
    elif (average >= 40):
        Grade = "C"
    else:
        Grade = "F"
    print(f"Student Name: {name}")
    print(f"Average Marks: {round(average, 2)}")
    print(f"Final Grade: {Grade}")

