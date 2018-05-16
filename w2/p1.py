# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 11:05:51 2018

@author: kalpof
"""

jobsfile = open("/home/kalpof/daa/w1/edges.txt","r")
nodes=[] #just an instance for all the vertices/nodes V in the tree
edges=[] #just an instance of an j=object whic contains all the edges in the tree
#weight=[]

for e in jobsfile:
    #print e
    e=e.strip("\n")
    #print e
    e=e.split(" ")
    #print(e)

    
    if(nodes.__contains__(e[0]) != True):
        nodes.append(e[0])
    
    
    if(nodes.__contains__(e[1]) != True):
        nodes.append(e[1])
    
    edges.append([int(e[2]), [int(e[0]), int(e[1])]])
    #weight.append(int(e[2]))

    
    
################# METHODS ############################
    
#this script is used to solve the kruskla mst problem. For now, i just create the algorithm and then i create
#the union find ds to solve the problem, needed for the k-mean clustering problem


"""
def createcicles(edge,tree):
    #a simple method used to find if adding an edge to a st creates a cicle
    
    seenedges = []
    i=0
    for e in tree:
        print e
        print(edge)
        if(i==0):
            seenedges.append(e[1][0])
            seenedges.append(e[1][1])
        elif(seenedges.__contains__(e[1][1]) != True):
            seenedges.append(e[1][1])
        else:
            seenedges.append(e[1][0])
        
        print(seenedges)
        i+=1
    
    if(seenedges.__contains__(edge[1][0]) and seenedges.__contains__(edge[1][1])):
        return True
    else:
        return False
"""

def createcicles(edge,tree):
    #a simple method used to find if adding an edge to a st creates a cicle
    
    #seenedges = [edge[1][0],edge[1][1]]
    k=0
    i = False
    #print("ciao")
    #print(edge[0])
    #print("ciao2")
    #print(edge[0])
    #print("ciao3")
    #print(tree)
    for e in tree:
        #print("here")
        #print e

        if(e.__contains__(edge[0]) != True and e.__contains__(edge[1]) != True):
            #seenedges.append(str(e[1][0])+str(e[1][1]))
            k=0
        else:
            #print("sera")
            i = True
    
    if(i == False):
        #print("giovane")
        tree.append(edge)
        return False
    else:
        i=False
        j=False
        p1=0
        p2=0
        for e in tree:
            if(e.__contains__(edge[0]) and e.__contains__(edge[1])):
                return True
            elif(e.__contains__(edge[0]) != True and e.__contains__(edge[1])):
                p1=e
                i=True  
            elif(e.__contains__(edge[0]) and e.__contains__(edge[1]) != True):
                p2=e
                j=True
            
            #print(p1)
            #print("beh")
            #print(p2)
            #print("beh2")

        
        if(j and i):
            #print("cosa2")
            for k in tree[tree.index(p2)]:
                tree[tree.index(p1)].append(k)
            tree.pop(tree.index(p2))
        elif(i):
            #print("cosa3")
            tree[tree.index(p1)].append(edge[0])
        elif(j):
            #print("cosa4")
            #print(tree.index(p2))
            tree[tree.index(p2)].append(edge[1])
        
        #print(tree)
        
        return False
        
        #seenedges.append(e[1][1])
    
        
            
               
    

#the algorithm is fairly simple 
#sort the array

edges.sort()

#create an instance of an empty tree

#print(edges)
#print(edges)
T = []
total = 0
#create the cicle
i=True
for e in edges:
    #print("ciao")
    #print e[1]

    if(createcicles(e[1],T) != True):
        print("added " + str(e))
        
        total += e[0]
    else:
        print("not added " + str(e))
    
    print(total)
    #print("eccoci")
    #print(T)
print(total)



















