quality_points = float(input("How many quality points do you have? "))
gpa_hours = int(input("How many GPA hours do you have? "))

course_name = []
credits = []
grade = []
answer = "y"
score = 0

print("-------------------------")
while answer == "y":
    course_name.append(str(input("What was the department and section number of your course (e.g., MTH-111)? ")))
    credits.append(int(input("How many credit hours is your course? ")))
    let_grade = (str(input("What grade (A, A-, B, C+, etc) did you get? ")))
    if let_grade == "A":
        grade.append(4.00)
    elif let_grade == "A-":
        grade.append(3.67)
    elif let_grade == "B+":
        grade.append(3.33)
    elif let_grade == 'B':
        grade.append(3.00)
    elif let_grade == "B-":
        grade.append(2.67)
    elif let_grade == "C+":
        grade.appedn(2.33)
    elif let_grade == "C":
        grade.append(2.00)
    elif let_grade == "C-":
        grade.append(1.67)
    answer = input("Keep adding classes? (y/n) ")
    print("Courses added:", course_name)

print("-------------------------")
print("This semester:")
print("Your credit hours:", sum(credits))
i = 0
while i < len(credits):
    score += credits[i]*grade[i]
    i += 1
print("Your quality points:", score)
gpa_final = (quality_points + score)/(gpa_hours + sum(credits))
print("-------------------------")
print("If you get the grades you entered, your GPA is:", round(gpa_final, 3))
