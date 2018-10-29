# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

####################### LOADING PART #####################################

file2import = open("/home/kalpof/Downloads/knapsack3.txt","r")

elements = [] #instance of the items we use in our problem, size of the kanpsack  ntr 10k


for e in file2import: 
    e = e.strip("\n")
    e = e.split(" ") 
    elements.append([int(e[0]), int(e[1])])


#print elements
    
############################# ACTUAL ALGORITHM ###################
    
W = 7 #the size of our knapsack, which is important for the cycle
tot_items = 5 #number of items we use in our problem, what here we refere with x

#instance of the knapsack

knapsack = []
#from here, the knapsack is just an empty container. What we need to do is, initally
#fill the first column with 0. The array is composed with tot_items+1 as number of columns
#and W+1 as number of rows

#for now, just create an empty matrix, using None



knapsack = [[0 for x in range(W+1)] for y in range(tot_items+1)] #just a short-hand notation for setting-up the matrix
#nothing really too fancy

#the algorithm is easy, truly speaking, but knowing the procedure is somewhat painful. The algorithm simply scans throught the knapsack
#matrix, comparing the values we stored in. If the value of the element we are currently seeing is greater than the previous one, we use 
#that element, in other case, we simply add the previous one
i=1
x=0
while(i <= tot_items): #cycle throught the columns
    
    while(x <= W):
        if(x - elements[i-1][1] >= 0): #if we are at a valid point on the matrix, could also use try/catch block
            value1 = knapsack[i-1][x] #first value we use to solve the problem
            value2 = knapsack[i-1][x - elements[i-1][1]] + elements[i-1][0] #just finding the other element we're interested in
            knapsack[i][x] = max(value1,value2) #setting a compare
        else:
            knapsack[i][x] = knapsack[i-1][x] #the only other value remaining
        
        print knapsack
        x=x+1
    i=i+1
    x=0

print(knapsack[i-1][x-1]) #problem solved. ntr this is NOT the optimal solution, cause we can't traceback the items and so we can't output 
#how the solution was solved, truly speaking
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    