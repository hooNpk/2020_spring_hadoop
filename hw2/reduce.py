#!/usr/bin/env python
import sys

#last_rname = None
rprice, rdistance = None, None
standard_price = 999999999
res_list = []

for key_value in sys.stdin:
    key_value = key_value.strip()
    table, table_value = key_value.split("\t")
    rname, rprice, rdistance = table_value.split(",")
    rprice, rdistance = rprice, rdistance
    res_list.append((rname, rprice, rdistance))
    #if(standard_price == 0):
    #    standard_price = int(rprice)+100
    #print("rname : ", rname, " rprice : ", rprice, " rdistance : ", rdistance)
    #print("last_rname : ", last_rname, " std_price : ", standard_price)
    #print(' ')

res_list = sorted(res_list, key=lambda x:int(x[2]))
#print(res_list)

for rest in res_list:
    #if(standard_price==0):
    #    print("%s"%(rest[0])
    #    standard_price = int(rest[1])
    #print(standard_price)
    if(int(rest[1]) < standard_price):
        print("%s"%(rest[0]))
        standard_price = int(rest[1])

"""
if last_rname and rprice and rdistance:
        if(rprice<standard_price):
            standard_price = rprice
            print("%s"%(rname))
        last_rname = rname
    else:
        last_rname, standard_price = rname, rprice
        print("%s"%(rname))

if last_rname and rprice and rdistance: # last_deptno and location and enames are not none
    if(rprice<standard_price):
        standard_price = rprice
        print("%s"%(rprice))
"""
