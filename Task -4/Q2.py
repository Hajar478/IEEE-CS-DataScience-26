students_hours ={}
subject_hours ={}

file_path =r"D:\downloads\students.txt"
with open(file_path,'r') as f:
    lines=f.readlines()
    if len(lines)==0:
        print('File is empty')
        exit()

for line in lines:
    line=line.strip()
    vals = line.split(",")#list
    if len(vals) != 3:
        print("Invalid format:",line)
        continue
    name=vals[0].strip()
    try:
        hours=int(vals[1].strip())
    except ValueError:
        print('invalid hours',line)
        continue
    subject=vals[2].strip()
    if name in students_hours:
        students_hours[name] +=hours
    else:
        students_hours[name] =hours

    if subject in subject_hours:
        subject_hours[subject] +=hours
    else:
        subject_hours[subject] =hours

top_student=""
max_hours_stu=-1
for student in students_hours:
    if students_hours[student]>max_hours_stu:
        max_hours_stu=students_hours[student]
        top_student=student

top_subject=""
max_hours_sub=-1
for subject in subject_hours:
    if subject_hours[subject]>max_hours_sub:
        max_hours_sub=subject_hours[subject]
        top_subject=subject

with open("mysummary.txt",'w') as output:
    output.write("Total Hours Per Student:\n\n")
    for student in students_hours:
        output.write(student + ": " + str(students_hours[student]) + "\n")

    output.write("\nTotal Hours Per Subject:\n\n")
    for subject in subject_hours:
        output.write(subject + ": " + str(subject_hours[subject]) + "\n")
        
    output.write("\nTop Student: " + top_student + "(" + str(max_hours_stu) + " hours)\n")

    output.write("Most Studied Subject: " + top_subject)
     

