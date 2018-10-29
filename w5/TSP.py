# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 14:10:09 2018

@author: kalpof
"""

#this is the code for a tsp solver, i'll give more infos later, during the writing of the
#algorithm, due to the complexity of the approach to this problem

#first of all, data loading

#################################### DATA LOADING ################################

file2import = open("/home/kalpof/Downloads/TSP2.txt", "r")
file2import2 = open("/home/kalpof/Downloads/TSP2.txt", "r")

nodes = []
edges = {} #in this case, i think that the edges must be a dictionary, so we can access a 2D matrix easily
#note that in this case edges in somewhat similar to an hash table

#the data are just the longitude and latitude of some cities, so a vertex is in a form of a (x,y)
#point on a 2D plain

for e1 in file2import:
    e1 = e1.strip("\n")
    e1 = e1.split(" ") #here we're finding the coordinates of the first city
    
    nodes.append((float(e1[0]), float(e1[1]))) #create a vertex from the city




for e1 in nodes: #we need a second nested cycle due to the fact that every city is connected to every other one
        #with their euclidean distance, for a total of 625 edges        
        for e2 in nodes:       
            if(e1 != e2):
                distance = ((float(e1[0]) - float(e2[0]))**2 + (float(e1[1]) - float(e2[1]))**2)**0.5 #euclidead distance between 2 points
                edges[(((float(e1[0]), float(e1[1]))), (float(e2[0]), float(e2[1])))] = distance #adding of the edge
                #that's a bit clunky to read, but it's right syntax
                
###################################### HELPER FUNCTIONS #############################   
                
def returnpermutation(size,nodes, dim): #this function returns all the permutation of an set of nodes
#simply cycle in all the combination of n in nodes and create all possible sets of nodes
    
    i=0
    j=0
    permutation = []
    while(True):
        if(i<1):
            for e in nodes:
                permutation.append([e])
        else:
            while(j<size):
                permutation.append(permutation[i-1]+[nodes[j]])
                j+=1

        j=permutation[i][len(permutation[i])-1]
        i+=1    
        if(len(permutation[i-1]) > dim-1):
            break
    
    return permutation       
                         
##################################### ALGORITHM #######################################
            
#we've completed our graph, using points on the 2D plain and the euclidead distances
  
n = len(nodes) #just the number of our cities/vertices

#this algorithm takes a dynamic approach, so we need to set a base case. The base case is setted with the matrix
#For the algorithm we need a distance matrix, composed of all the edge costs we found using the euclidean distance
#In the first cycle, we add only the "base case" so 
#virtually speaking

A = {} #instance of the  "matrix" (using a dictionary due to python)

for e in edges: #adding the nodes and the edge cost related to the first node (that we initially skip) to the matrix
    k = (nodes[0])
    if(e[0] == (nodes[0]) and e[0][1] != (nodes[0])):
        A[(e[1],None)] = edges[e]

totelements=[]
k=[]

#returnpermutation return all the possible permutation of a set of numbers n. The script below
#converts the numbers in nodes. Again, it's clucnky but working
for e in returnpermutation(len(nodes),range(1,len(nodes)+1),len(nodes)):
    for e1 in e:
        if(1 not in e):
            k.append(nodes[e1-1])
    if(len(k) != 0):   
        totelements.append(k)
    k=[]


#here that's the real part of the algorithm
#the iteraction that we follow to solve this problem is basically this
#A[S,w] = min( C(w,k) + A[S-w,w] ) f.e. w in S, f.e. k in Nodes. Seems easy right? Well, it's not lmao
#We have to cycle thorught all the nodes from 2 to n (leaving aside the first node)
# and from here, we need to find the minimun cost route using the edge costs and the distance matrix itself
#the code, truly speaking, is fairly easy to read, but it took me a lot of time to get it right. A special thanks to wikipedia
#https://en.wikipedia.org/wiki/Held%E2%80%93Karp_algorithm
for e in totelements:
    for k in nodes[1:]:
        if(k not in e):
            for value in e:
                if(len(e) < 2):
                    y = e[:]
                    A[(k,tuple(e))] = edges[k,value] + A[value,y.remove(value)]
                else:
                    try:
                        A[(k,tuple(e))]
                    except:
                        A[(k,tuple(e))] = edges[k,value] + A[(value,tuple([x for x in e if x != value]))]
                    else:
                        if(edges[k,value] + A[(value,tuple([x for x in e if x != value]))] < A[(k,tuple(e))]):
                            A[(k,tuple(e))] = edges[k,value] + A[(value,tuple([x for x in e if x != value]))]
                            

#the last step of the algoritm. We need to find the shortest path from A[{2,3...n},1] to 1. So
#the last step is simply A[1,{2,3..n}] = min( A[S-k,k] + C(1,k) ) for each k in S and for each n=2,3...n in Nodes
#the last print is the shortest path using the euclidead distance
for e in nodes[1:]:
    try:
        A[(nodes[0], tuple(totelements[len(totelements)-1]))]
    except:
        A[(nodes[0], tuple(totelements[len(totelements)-1]))] = edges[nodes[0],e] + A[(e,tuple([x for x in nodes[1:] if x != e]))]
    else:
        if(edges[nodes[0],e] + A[(e,tuple(x for x in nodes[1:] if x != e))] < A[(nodes[0], tuple(totelements[len(totelements)-1]))]):
                            A[(nodes[0], tuple(totelements[len(totelements)-1]))] = edges[nodes[0],e] + A[(e,tuple([x for x in nodes[1:] if x != e]))]

print A[(nodes[0], tuple(totelements[len(totelements)-1]))]       

######################################################################################     











