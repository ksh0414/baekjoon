import sys
input = sys.stdin.readline

students = []
for _ in range(int(input())):
    name, a, b, c = input().rstrip().split()
    students.append((-int(a), int(b), -int(c), name))
students.sort()

for student in students:
    print(student[3])