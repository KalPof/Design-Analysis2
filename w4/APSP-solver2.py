# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 16:13:00 2018

@author: kalpof
"""

#This is an APSP solver using a johnson algorithm.




############################### DATA STRUCTURE ###################################

#The Johnson Algorithm works using a technique to solve negative costs cycles in graphs, which are
#quite difficult to handle. Having solved this problem, we can use a dijkstra shortest path and a bellman ford
#algorithm to solve our problem. To solve the negative costs edges, we need to find the shortest path
#for every vertex (tarting from a source vertex S, connected to every other vertex with an edge of cost 0)
#

#first of all, we create the data structure

class Graph(object):
    
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges
    
    def returnNodes(self):
        return self.nodes
    
    def returnEdges(self):
        return self.edges
    
    def addNode(self,name):
        self.nodes.insert(0,Node(name))
    
    def addEdge(self,n1,n2,weight):
        #n1 and n2 has be to nodes
        self.edges.insert(0,Edge(n1,n2,weight))
    
    def PPNodes(self):
        for e in self.nodes:
            print(e.returnName())
    
    def PPValues(self):
        for e in self.nodes:
            print(e.returnValue())
    
    def PPEdges(self):
        for e in self.edges:
            print(str(e.returnN1().returnName()) + " " + str(e.returnN2().returnName()) + " " + str(e.returnWeight()))
    

class Node(object):
    
    def __init__(self, name):
        self.name = name
        self.value = None
    
    def returnName(self):
        return self.name
    
    def setValue(self,value):
        self.value = value
    
    def returnValue(self):
        return self.value
        

class Edge(object):
    
    def __init__(self, node1,node2,weight):
        self.node1 = node1
        self.node2 = node2
        self.weight = weight
    
    def returnN1(self):
        return self.node1
    
    def returnN2(self):
        return self.node2
    
    def returnWeight(self):
        return self.weight


########################## DATA LOADING ############################

file2import = open("/home/kalpof/Downloads/APSPtest5.txt", "r")

nodes = []
edges = []
container = []

for e in file2import:
    e = e.strip("\n")
    e = e.split(" ")
    
    n1 = Node(int(e[0]))
    n2 = Node(int(e[1]))
    
    if(n1.returnName() not in container):
       nodes.append(n1)
       container.append(n1.returnName())
       
    if(n2.returnName() not in container):
        nodes.append(n2)
        container.append(n2.returnName())
        
    edges.append(Edge(n1,n2,int(e[2])))

NewGraph = Graph(nodes,edges)


############################# ACTUAL ALGORITHM ########################


def Johnson(G): #G stands for a directed graph

    #the first thing to do is to add a source vertex
    G.addNode(0) #the source vertex has name = 0 (we could use any other name, it's just for std reasons 
    
    j = range(len(nodes))
    j.reverse()
    for e in j:
        G.addEdge(G.returnNodes()[0],G.returnNodes()[e],0)
    
    #G.PPNodes()
    #G.PPEdges()

    Bellman_Ford(G,G.returnNodes(),G.returnNodes()[0])


def Bellman_Ford(G,n,s): #G stands for a directed graph and n stands for an array of vectors
    #in this case, we don't need really the vector array, just the length of the array
    
    A = [float("inf") for q in range(len(n))]
    A[s.returnName()] = 0
    
    #coso = []
    for i in range(1,len(n)):
        #print ("\n")
        for e in G.returnEdges():
            n1 = e.returnN1().returnName() #stands for the first node
            n2 = e.returnN2().returnName() #stands for the second node
            w = e.returnWeight()
            
            if(A[n1] + w < A[n2]):
                    A[n2] = A[n1] + w

    
    A.sort()
    print(A[0])

Johnson(NewGraph)

    