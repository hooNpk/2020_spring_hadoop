#!/usr/bin/env python
import sys

data_list = []
for line in sys.stdin:
    if(line):
        line = line.strip()
        #line = line.replace(' ','')
        tuple_list = line.split(",") # Splits a string into a list.
                
        rname = tuple_list[0]
        price = tuple_list[1]
        distance = int(tuple_list[2])
        
        data_list.append((rname, price, distance))

data_list = sorted(data_list, key=lambda x:x[2])
for data in data_list:
    print('{0}\t{1}'.format('res', data[0]+','+data[1]+','+str(data[2]))) 
