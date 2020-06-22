#!/usr/bin/env python
import sys

for line in sys.stdin:
    line = line.strip()
    #line = line.replace(' ','')
    tuple_list = line.split(",") # Splits a string into a list.
                
    if len(tuple_list) == 6: # student file
        gpa = tuple_list[5]
        deptno = tuple_list[4]
                                                
        # deptno = key  emp,ename = value
        print('{0}\t{1}'.format(deptno, 'student,'+gpa)) 
                                                                        
    else: # dept file
        name = tuple_list[1]
        campus = tuple_list[2]
        deptno = tuple_list[0]
                                                                                                        
        # deptno = key  dept,loc = value
        print('{0}\t{1}'.format(deptno, 'dept,'+name+','+campus))

