#taking names from student 
#taking marks of student in every subjects 
#calculating percentage 
# print 3 class toppers with their %
n = int(input("Enter the number of students in the class: "))

student_report = {}  # Initialize an empty dictionary to store student data

for x in range(n):  # Loop n times to collect data for each student
    name = input("Enter the name of the student: ")
    
    # Collect marks for different subjects
    marks = {
        "Maths": int(input("Marks scored in Maths: ")),
        "English": int(input("Marks scored in English: ")),
        "Hindi": int(input("Marks scored in Hindi: ")),
        "Science": int(input("Marks scored in Science: ")),
        "Social_science": int(input("Marks scored in Social science: "))
    }
    
    # Add the student's name and their marks to the dictionary
    student_report[name] = marks


# Print the final report after collecting all student data
print("\nStudent Report:")
for name, marks in student_report.items():
    print(f"{name}: {marks}")
    #finding % of each student= sum of marks obtained in each subject/no. of subjects
    percentage = (marks["Maths"]+marks["English"]+marks["Hindi"]+marks["Science"]+marks["Social_science"])/5
    print(f"the % of {name} is {percentage}%")

