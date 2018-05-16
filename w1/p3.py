jobsfile = open("/home/kalpof/daa/tests/t2.txt","r")

nodes=[] #just an instance for all the vertices/nodes V in the tree
edges=[] #just an instance of an j=object whic contains all the edges in the tree

for e in jobsfile:
    e=e.strip("\n")
    e=e.split(" ")
    if(nodes.__contains__(e[0]) != True):
        nodes.append(e[0])
    
    
    if(nodes.__contains__(e[1]) != True):
        nodes.append(e[1])
    
    edges.append([[int(e[0]), int(e[1])], int(e[2])])

#maybe i need'em, may be not. JUst in case, i instantiate them

X = [] #create in instance of X. which contains all the nodes i've seen during the procedure of the algorithm
T = [] #this is the instance of the tree which contains the edges. Now, obviously, is empty



X.append(nodes[0]) #just for testing procedure, i add the first vertex/node of V to X, so i can start my algorithm

nodes.sort()

totalweight = 0
while(X !=  nodes):
    
    #now i need to find the weightless edges of my tree where the first node is the one i've already added, and the
    #second one isn't already in X, and we add it next.
    
    findnode = 0
    findedge = 0
    parking = 1000000000 #just an arbitrary big number so the edge cant be heavier than this
    for e in edges:
        if(X.__contains__(str(e[0][0])) and X.__contains__(str(e[0][1])) != True):
            if(parking > e[1]):
                parking = e[1]
                findnode = e[0][1]
        elif(X.__contains__(str(e[0][0])) != True and X.__contains__(str(e[0][1]))):
            if(parking > e[1]):
                parking = e[1]
                findnode = e[0][1]
                findedge = e
    
    if(findnode != 0 and X.__contains__(str(findnode)) != True):
        X.append(str(findnode))
        T.append(findedge)
    elif(X.__contains__(str(findedge[0][1]))):
        X.append(str(findedge[0][0]))
        
    if(len(X) == len(nodes)):
       X.sort()
        
    totalweight += parking


print(totalweight)


# in this kind of array, the elements are jobs to be scheduled, wich are composed of values.
#the first one is the weight, and the last one is he length. What i need to do is to give the jobs
#a score, defined as S = W -L, which is not always good (as a greedy kind of algorithm whis isn't always true)
#cause is not a ratio, which we've proved to be always a good approach.
#From here, we need to computer C = Sum(length), and the min(sum(C*weight))
#Assigning a score, what we do is to create a schedule where the jobs are stacked given the score value