'''
Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

Example
records=[["chi",20.0],["beta",50.0],["alpha",50.0]]

The ordered list of scores is[20.0,50,0] , so the second lowest score is 50.0 . There are two students with that score: . Ordered alphabetically, the names are printed as:

alpha
beta
Input Format

The first line contains an integer, , the number of students.
The  subsequent lines describe each student over  lines.
- The first line contains a student's name.
- The second line contains their grade.

Constraints
2<=N<=5
There will always be one or more students having the second lowest grade.
Output Format

Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line.'''
n = int(input())
Grade = []
sortList = []
for i in range(n):
    Name = input()
    score = float(input())
    Grade.append([Name,score])
    sortList.append(score)
    
sortList = list(set(sortList))
sortList.sort()
printList = []
for i in range(nTestCase):
    if Grade[i][1] == sortList[1]:
        printList.append(Grade[i][0])
printList.sort()
for i in range(len(printList)):
    print(printList[i])
