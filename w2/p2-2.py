# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 16:56:04 2018

@author: kalpof
"""



################################################ COSE ########################


class ConnectedComponent(object):
    
    def __init__(self, name):
        self.name = name
        self.size=1
        self.leadernode= name
        self.nodes=[]
        self.edges=[]
        self.pathweight = 0
    
    
    """
    def addedge(self, edge):
        
        if(str(edge[1][0]) not in self.nodes):
            self.nodes += str(edge[1][0])
            self.edges.append(edge)
        elif(str(edge[1][1]) not in self.nodes):
            self.nodes += str(edge[1][1])
            self.edges.append(edge)
     """
        

    
    def addedge(self, edge):
        
        if(self.nodes.__contains__(int(edge[1][0])) !=True):
            self.nodes.append((edge[1][0]))
            self.edges.append(edge)
        
        elif(self.nodes.__contains__(int(edge[1][1])) !=True):
            self.nodes.append((edge[1][1]))
            self.edges.append(edge)
     
    
    
    def changeSize(self, size):
        self.size = size
    
    def changeLeader(self,leadernode):
        self.leadernode = leadernode
        
    def returnNodes(self):
        return self.nodes
    
    def returnEdges(self):
        return self.edges
    
    def addNode(self,node):
        self.nodes += str(node)
        
    def returnSize(self):
        return self.size
        
    def returnName(self):
        return self.name
        
    def returnLeader(self):
        #print("quando c'era lvi i treni erano in orario")#just a random easter egg
        return self.leadernode
        
    def changePW(self, PW):
        self.pathweight = PW
    
    def returnPW(self):
        return self.pathweight



class UnionFind(object):
    
    def __init__(self):
        self.ConnectedComponents = [None] * 500
    
    
    def addConnectedComponent(self, ConnectedComponent):
        self.ConnectedComponents[ConnectedComponent.returnName()-1] = ConnectedComponent
    
    
    def Merge(self, edge):
        
        leaderCoCo1 = self.ConnectedComponents[(self.ConnectedComponents[edge[1][0]-1].returnLeader())-1]
        leaderCoCo2 = self.ConnectedComponents[(self.ConnectedComponents[edge[1][1]-1].returnLeader())-1]
        coco1 = self.ConnectedComponents[edge[1][0]-1]
        coco2 = self.ConnectedComponents[edge[1][1]-1] 

        if(leaderCoCo1.returnSize() >= leaderCoCo2.returnSize()):
            if(leaderCoCo1 != leaderCoCo2):
                leaderCoCo1.changeSize(leaderCoCo1.returnSize() + leaderCoCo2.returnSize())
            else:
                 leaderCoCo1.changeSize(leaderCoCo1.returnSize() + 1)
            
            coco2.changeLeader(leaderCoCo1.returnName())
            coco1.addedge(edge)
            coco2.addedge(edge)
            leaderCoCo2.changeLeader(coco2.returnLeader())
        else:
            if(leaderCoCo1 != leaderCoCo2):
                leaderCoCo2.changeSize(leaderCoCo2.returnSize() + leaderCoCo1.returnSize())
            else:
                leaderCoCo2.changeSize(leaderCoCo1.returnSize() + 1)
            
            coco1.changeLeader(leaderCoCo2.returnName())
            coco1.addedge(edge)
            coco2.addedge(edge)
            leaderCoCo1.changeLeader(coco1.returnLeader())
        
    
    def Printer(self):
        for e in self.ConnectedComponents:
            if(e != None):
                print("Nome: " + str(e.returnName()))
                print("Leader: " + str(e.returnLeader()))
                print("Size: " + str(e.returnSize()))
                print("Leader Size: " + str(self.ConnectedComponents[e.returnLeader()-1].returnSize()))
                #print("total weight: " + str(self.ConnectedComponents[e.returnLeader()-1].returnPW()))
                #print("\n")
                

    
    
    def returnCoCo(self):
        return self.ConnectedComponents

######################################### TEST #############################

jobsfile = open("/home/kalpof/daa/tests/t3.txt","r")
nodes=[] #just an instance for all the vertices/nodes V in the tree
edges=[] #just an instance of an j=object whic contains all the edges in the tree
#weight=[]

for e in jobsfile:
    e=e.strip("\n")
    e=e.split(" ")
    if(nodes.__contains__(e[0]) != True):
        nodes.append(e[0])
    
    
    if(nodes.__contains__(e[1]) != True):
        nodes.append(e[1])
    
    edges.append([int(e[2]), [int(e[0]), int(e[1])]])
    #weight.append(int(e[2]))


#print(nodes)
#print(edges)


U = UnionFind()

for e in nodes:
   
    U.addConnectedComponent(ConnectedComponent(int(e)))
    
    
#U.Printer()

#i = 0
for e in edges:
    #print(e[1])
    U.Merge(e)
    U.Printer()
    
    
    
    
"""

cose1 = []
for e in nodes:
   
    cose1.append(ConnectedComponent(int(e)))

U = UnionFind()

for e in cose1:
    U.addConnectedComponent(e)
    
    
"""
    
    
    

"""
            if(str(edge[1][0]) not in leaderCoCo1.returnNodes() or str(edge[1][1]) not in leaderCoCo1.returnNodes()):
                leaderCoCo1.changePW(leaderCoCo1.returnPW() + edge[0] + coco2.returnPW())
                leaderCoCo1.addNode(coco2.returnNodes())
                leaderCoCo1.addNode(coco1.returnNodes())
"""   


"""
            if(str(edge[1][0]) not in leaderCoCo1.returnNodes() or str(edge[1][1]) not in leaderCoCo1.returnNodes()):
                leaderCoCo2.changePW(leaderCoCo2.returnPW() + edge[0] + coco1.returnPW())
                leaderCoCo2.addNode(coco2.returnNodes())
                leaderCoCo2.addNode(coco1.returnNodes())
"""








        
    