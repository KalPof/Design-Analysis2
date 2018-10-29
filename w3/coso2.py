# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

####################### LOADING PART #####################################

import sys
file2import = open("/home/kalpof/Downloads/knapsack_big.txt","r")

elements = [] #instance of the items we use in our problem, size of the kanpsack  ntr 10k

for e in file2import: 
    e = e.strip("\n")
    e = e.split(" ") 
    elements.append([int(e[0]), int(e[1])])


#print(elements)
#print elements
    
############################# ACTUAL ALGORITHM ###################
    
W = 2000000 #the size of our knapsack, which is important for the cycle
tot_items = 2000 #number of items we use in our problem, what here we refere with x

#instance of the knapsack

knapsack = {}
#from here, the knapsack is just an empty container. What we need to do is, initally
#fill the first column with 0. The array is composed with tot_items+1 as number of columns
#and W+1 as number of rows

#for now, just create an empty matrix, using None

#elements.sort(reverse=True)



def knapsack_solution(array, PartialWeight):
    
    #print (total)
    if (W<=0):
        return 0
    
    last_item = array[-1]
    
    if(len(array) == 1):
        if(last_item[1] <= W):
            return last_item[1]
        else:
            return 0
    
    key1= (len(array[:-1]), PartialWeight)
    val1 = knapsack.get(key1)
    
    if val1 == None:
        #print ("h1")
        val1= knapsack_solution(array[:-1], W)
        knapsack[key1] = val1
    
    key2 = (len(array[:-1]), W-last_item[1])
    val2pre = knapsack.get(key2)
    
    if val2pre == None:
        #print ("h2")
        val2pre = knapsack_solution(array[:-1], W - last_item[1])
    
    if last_item[1] <= W:
        val2 = val2pre + last_item[0]
    else:
        val2 = 0
    
    if(val1 >= val2):
        retval= val1
    else:
        retval = val2
    
    return retval


sys.setrecursionlimit(tot_items+200)
k = knapsack_solution(elements,W)
#print(total)

print k  
    
#for the second output the corrent answer is 4243395   

















































"""
total = 0
i=0
We=0
resto=0

for i in range(tot_items):
    
    if(We + elements[i][1] <= W):
        total += elements[i][2]
        We += elements[i][1]
    else:
        print(elements[i])
        print i
        resto = W - We
        #total += elements[i][2] * resto/elements[i][1]
        break

print total
"""