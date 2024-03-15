# https://www.hackerrank.com/challenges/nested-list/problem

# In a classroom of N students, find the student with the second lowest grade.

# Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

# Method 1

if __name__ == '__main__':
    grade_names = {}

    for _ in range(int(input("Enter number of students: "))):
        name = input("Enter name of student: ")
        score = float(input("Enter score of student: "))

        if score in grade_names:
            grade_names[score].append(name)
        else:
            grade_names[score] = [name]

    # print(grade_names)

    second_lowest_student_key = sorted(grade_names.keys())[1]
    second_lowest_student_name = sorted(grade_names[second_lowest_student_key])
    
    for _ in second_lowest_student_name:
        print(_)

# Method 2
if __name__ == '__main__':
   records = []
   names = []
   for _ in range(int(input("Enter number of students: "))):
      name = input("Enter name of student: ")
      score = float(input("Enter score of student: "))
      records.append([name,score])

   print(records)
   score_list = sorted(set([i[1] for i in records]))
   print(score_list)
   for i in records:
      if i[1] == score_list[1]:
         names.append(i[0])
   for i in sorted(names):
      print(i)
