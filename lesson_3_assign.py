#_______Lesson 3: Assignments | Python Lists_____
# 1. Python List Transformation


print("\n\n_____Lesson 3: Assignments | Python Lists____\n")
print("="*50)


    #Task 1
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort(reverse=True)
print("Sorted grades in descending order are:\n", grades)

    #Task 2
total_grades = sum(grades)
num_grades = len(grades)
average_grade = total_grades / num_grades
print("The average grade is:\n", average_grade,"\n")
print("="*50)



#================================================
#2. Advanced Slicing Techniques
    #Task 1

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
second_week_temperatures = temperatures[7:14]
print("Temperatures for the second week are:\n", second_week_temperatures)



#================================================
    #Task 2

temperatures_above_100 = [temp for temp in temperatures if temp > 100]
print("Temperatures above 100 are:\n", temperatures_above_100)
print("="*50)


#================================================
    #Task 3

temperatures_5th_to_10th = temperatures[4:10]
print("Temperatures from the 5th to the 10th are:\n", temperatures_5th_to_10th)
print("="*50)
