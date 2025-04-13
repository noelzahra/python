def grades_result(grade)->int:
    result = None
    if grade >= 70:
        result = f"You passed! Mark:{grade}. Grade: A"
    elif grade >= 60:
        result = f"You passed! Mark:{grade}. Grade: B"
    elif grade >= 50:
        result = f"You passed! Mark:{grade}. Grade: C"
    else:
        result = f"You failed: Mark:{grade}. Grade: F"
    
    return result

student_grades = {
    "Ivan"  :80, 
    "Bob"   :70, 
    "Tim"   :66, 
    "Jean"  :55, 
    "Lea"   :49
    }

for student in student_grades:
    print(f"{student}: {grades_result(student_grades[student])}")