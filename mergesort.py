# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 11:39:06 2018

@author: kalpof
"""


j = [0,5,8,3,2,6,9,4,7,7,4]

def mergesorter(A, left, right):
    
    if(left < right):
        center = (left+right)/2
        mergesorter(A, left, center)
        mergesorter(A, center+1, right)
        merge(A, left, center, right)
    
def merge(A, v1,v2,v3): #stands for left, center and right
    
    i = v1
    j = v2+1
    t= []

    
    while(i <= v2 and j <= v3):
        if(A[i] > A[j]):

            t.append(A[j])
            j+=1
        else:

            t.append(A[i])
            i+=1

    
    while(i <= v2):

        t.append(A[i])
        i+=1

    
    while(j <= v3):
        t.append(A[j])
        j+=1

    e=v1
    while(e <= v3):

        A[e] = t[e-v1]
        e+=1
        
mergesorter(j,0,len(j)-1)

print(j)