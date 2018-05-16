# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 17:11:57 2018

@author: kalpof
"""

jobsfile = open("/home/kalpof/daa/w1/jobs.txt","r")
emparray = []

for e in jobsfile:
    e=e.strip("\n")
    e=e.split(" ")
    emparray.append([int(e[0]), int(e[1])])
    
# in this kind of array, the elements are jobs to be scheduled, wich are composed of values.
#the first one is the weight, and the last one is he length. What i need to do is to give the jobs
#a score, defined as S = W -L, which is not always good (as a greedy kind of algorithm whis isn't always true)
#cause is not a ratio, which we've proved to be always a good approach.
#From here, we need to computer C = Sum(length), and the min(sum(C*weight))
#Assigning a score, what we do is to create a schedule where the jobs are stacked given the score value

emparray.sort()
emparray.reverse()
scores = []

unsortscores = []

for e in emparray:
    
    #i use this cycle to create the scores. For run time purpose what i want to do is 
    #to create an unsroted array of the scores, and the instanciate a new array equal to the previous
    #one, but only sorted, which i can use to access the values in the previous array without
    #need of an useless instantiation of an array
    scores.append(float(e[0])/float(e[1]))
    #from before, we changed the kind of score whe give to the jobs, this time is a ratio
    unsortscores.append(float(e[0])/float(e[1]))

scores.sort()
scores.reverse() #be carefull here, cause we need to sort in a decreasing order, so the 
#tiniest number on the list must be the last one, same for the greatest one 

 #i now use the built it method, but i wanna refresh the sorting methods i've
#done before, so, just to keep on going


#when 2 scores are equal, always prefer the job with the higher weight, so stack it on first

#instantiate the 2 values needed
completiontime = 0
total =0

#find the actual total

for e in scores:
    
    job = emparray[unsortscores.index(e)]
    
    completiontime += job[1]
    total += job[0]*completiontime 
    
    emparray.pop(unsortscores.index(e))
    unsortscores.pop(unsortscores.index(e))

print total
