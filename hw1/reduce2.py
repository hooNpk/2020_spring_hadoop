#!/usr/bin/env python
import sys

last_deptno = None
dname, dloc = None, None
sgpas = []
total_gpa, max_gpa = 0, 0

for key_value in sys.stdin:
    total_gpa, max_gpa = 0, 0
    key_value = key_value.strip()
    dept_no, table_value = key_value.split("\t")
    table, value1, value2 = None, None, None
    table_value = table_value.split(",")
    
    #print("===== start for =====")
    if(len(table_value)==2):
        table, value1 = table_value
    else:
        table, value1, value2 = table_value
    
    if last_deptno == dept_no: 
        if table == 'student':
            #print("table==student")
            sgpas.append(value1)
        else: # table == 'dept'
            dname, dloc = value1, value2
    else:
        if last_deptno and dname and sgpas: # last_deptno and location and enames are not none
            for sgpa in sgpas:
                #print(total_gpa)
                temp_sgpa = float(sgpa)
                total_gpa += temp_sgpa
                if(temp_sgpa>max_gpa):
                    max_gpa = temp_sgpa
            if(total_gpa/len(sgpas)>3.5):
                print("%s, %s, %s"%(dname, str(max_gpa) ,dloc))
        # Init the location and enames
        dname, dloc= None, None
        sgpas = []
        
        if table == 'student':
            sgpas = [value1]
        else: # table == 'dept'
            dname, dloc = value1, value2
        
        last_deptno = dept_no

total_gpa, max_gpa = 0, 0
if last_deptno and dname and sgpas: # last_deptno and location and enames are not none
    for sgpa in sgpas:
        temp_sgpa = float(sgpa)
        total_gpa += temp_sgpa
        if(temp_sgpa>max_gpa):
            max_gpa = temp_sgpa
    if(total_gpa/len(sgpas)>3.5):
        print("%s, %s, %s"%(dname, str(max_gpa), dloc))

