n = int(input())
student_marks = {}

for i in range(n):
    line = input().split()
    name = line[0]
    marks = list(map(float, line[1:]))
    student_marks[name] = marks

query_name = input()
avg = (sum(student_marks[query_name]) / len(student_marks[query_name]))

print("{:.2f}".format(avg))
