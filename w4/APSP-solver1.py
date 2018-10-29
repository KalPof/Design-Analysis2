# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 17:10:22 2018

@author: kalpof
"""

#this is an implementation of a floyd-warshall algorithm to solve an APSP (which is a SSSP without a definied start node, so every
#node/vertex can be our starting vertex, and with that the type of algorithm changes)


########################### FILE LOADING ############################

file2import = open("/home/kalpof/Downloads/APSPtest3.txt", "r")

nodes = []
edges = []
costs = []

for e in file2import:
    e = e.strip("\n")
    e = e.split(" ")
    
    if int(e[0]) not in nodes:
        nodes.append(int(e[0]))
    
    if int(e[1]) not in nodes:
        nodes.append(int(e[1]))
        
    edges.append([int(e[0]),int(e[1]), int(e[2])])
    



#print nodes
#print edges
################## ACTUAL ALGORITHM ####################################


#just a brief explanation of the algorithm. The Algoritgm is based on
#a 3-D array. The 3D array works around 3 variables, i, k and j.
#Assuming n as the number of vertices, we cycle using those 3 variables
#using n as a limit. 

n = len(nodes) +1 

#NOTE: the order of the variables trought the cicles is important. First, you must
#cycle using the limiter of the node, than the source node and last the end node


#if i'm right, the actual algorithm works this way. We need a 2D (not a 3D, dunno y)
#matrix. The matrix contains the weights of the edges of 2 nodes, so A(u,v) = w(u,v)
#with w -> E


#for the start of the algorithm, we create a 3D matrix where every number is infinity (or close)
A =  [[[10000000000 for q in range(n)] for w in range(n)] for t in range (n)]

print 1


#the next step is to change the values of the matrix. We assign 0 of every number where i=j
#so A[i][i]=0=A[j][j]. Last, we assign w(i,j) in E o the matrix, so that A[i][j] = w(i,j)
for e in edges:
        
    
    A[e[0]][e[0]][0] = 0
    A[e[1]][e[1]][0] = 0
    A[e[0]][e[1]][0] = e[2]
    
    #print A


k=1
i=1
j=1

container = []

#the next steps are self explanatory. We use a O(n^3) cycle to change the values of the matrix. We change the values
#based on the values precedentely stored inside the matrix, as seen below. The main point of the algorithm is
#to update the path using the nodes seen from 1 to k. We in fact are allowed only to use nodes labeled at max k, and find
#the shorest path with those. The shortest path is found using the previos values of the matrix. To find the
#APSP, we simply scan throught all of our nodes (using i and j as a range) but k as a limiter, and updating
#the matrix with that 
for k in range(1,n):
    for i in range(1,n):
        for j in range(1,n): 
            if(A[i][j][k-1] > A[i][k][k-1] + A[k][j][k-1]):
                A[i][j][k] =  A[i][k][k-1] + A[k][j][k-1]
                
            else:
                A[i][j][k] = A[i][j][k-1]
                if(A[i][j][k-1]/1000 < 100):
                    container.append(A[i][j][k-1])
                

#To find the APSP value, i simply add the values to and array and sort'em
container.sort()
print container[0]

"""
for e in A:
    print e
    print "cian \n"
"""