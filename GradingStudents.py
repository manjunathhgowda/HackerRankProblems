
'''
Question:
HackerLand University has the following grading policy:
- Every student receives a grade in the inclusive range from 0 to 100.
- Any grade less than 40 is a failing grade.
- If the difference between the grade and the next multiple of 5 is less than 3, round up to that multiple.
- If the grade is less than 38, no rounding occurs (still failing).

Example:
Input grades: [73, 67, 38, 33]
Output after rounding: [75, 67, 40, 33]

Explanation:
- 73 → next multiple of 5 is 75, difference is 2 < 3 → round to 75
- 67 → next multiple of 5 is 70, difference is 3 → no rounding → 67
- 38 → next multiple of 5 is 40, difference is 2 < 3 → round to 40
- 33 → below 38 → no rounding → 33
'''
def gradingStudents(grades):
    rounded_grades = []

    for grade in grades:
        if grade >= 38:
            # Find the next multiple of 5
            next_multiple_of_5 = ((grade // 5) + 1) * 5
            # Round if difference is less than 3
            if next_multiple_of_5 - grade < 3:
                grade = next_multiple_of_5
        # Append the (possibly rounded) grade to the result
        rounded_grades.append(grade)
    return rounded_grades
print(gradingStudents([73, 67, 38, 33]))