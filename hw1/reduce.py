#!/usr/bin/env python
import sys

student_list = []
dept_list= []
reduced_student_list = []

for key_value in sys.stdin:
    
    dept_no, table, sgpa, dname, dcampus = None, None, None, None, None

    key_value = key_value.strip()
    dept_no, table_value = key_value.split("\t")
    table_value = table_value.split(',')

    if(len(table_value)==2):#from student
        table, sgpa = table_value
        student_list.append((dept_no, sgpa))
        #print(table, sgpa)
    else:#from dept
        table, dname, dcampus = table_value
        dept_list.append((dept_no, dname, dcampus))
        #print(table, dname, dcampus)

for dept in dept_list:
    for student in student_list:
        if(dept[0] == student[0]):
            reduced_student_list.append((student[0], student[1], dept[1], dept[2]))
            #print((student[0], student[1], dept[1], dept[2]))

for dept in dept_list:
    gpa_max = 0
    gpa_total = 0
    stu_num = 0
    for student in reduced_student_list:
        if(dept[0] == student[0]):
            gpa = float(student[1])
            gpa_total += gpa
            stu_num += 1
            if(gpa>gpa_max):
                gpa_max = gpa
    #print(gpa_total, stu_num)
    if(gpa_total/stu_num>3.5):
        print("%s, %s, %s"%(dept[1], gpa_max, dept[2]))

