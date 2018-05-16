# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 10:53:19 2018

@author: kalpof
"""

jobsfile = open("/home/kalpof/daa/w2/clustering_big.txt","r")
emparray = [None] * 17000000

print("ciccio")
coso1= jobsfile.readline().split()
print("ciccio2")#

print(coso1)
#print(coso2)

for e in jobsfile:
    e=e.strip("\n")
    e=e.strip(" ")
    emparray[int(e,2)-1] = e
    #if(emparray.__contains__(e) != True):
    
total = 0
for e in emparray:
    
    if(e != None):
        total += 1
    #else:
    #   print(e)

print(total)
    
    