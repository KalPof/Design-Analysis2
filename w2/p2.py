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
        self.leadernode= self
        self.nodes=[name]
        self.edges=[]
        self.pathweight = 0
        
    def addedge(self, edge):
        
        if(self.nodes.__contains__(edge[1][0]) !=True):
            #self.nodes.append(edge[1][0])
            return True
        elif(self.nodes.__contains__(edge[1][1]) != True):
            #self.nodes.append(edge[1][1])
            return True
        
        return False
    
    def changeSize(self, size):
        self.size = size
    
    def changePW(self, PW):
        self.pathweight += PW
        
    def returnPW(self):
        return self.pathweight
        
    def changeLeader(self,leadernode):
        self.leadernode = leadernode
        
    def returnNodes(self):
        return self.nodes
    
    def returnEdges(self):
        return self.edges
    
    def returnSize(self):
        return self.size
        
    def returnName(self):
        return self.name
        
    def returnLeader(self):
        #print("quando c'era lvi i treni erano in orario")#just a random easter egg
        return self.leadernode

    def addNode(self,node):
        if(self.nodes.__contains__(node) !=True):
            self.nodes.append(node)
    


class UnionFind(object):
    
    def __init__(self):
        self.ConnectedComponents = [None] * 1500
        
    def addConnectedComponent(self, ConnectedComponent):
        self.ConnectedComponents[ConnectedComponent.returnName()-1] = ConnectedComponent
    
    def findLeader(self,CoCo):

        if(CoCo.returnName() != CoCo.returnLeader().returnName()):
            #print("cuccua")
            CoCo.changeLeader(self.findLeader(CoCo.returnLeader()))
        
        return CoCo.returnLeader()
    
    def Merge(self, edge):
        
        i= False
        leaderCoCo1=self.findLeader(self.ConnectedComponents[edge[1][0]-1])
        #print(leaderCoCo1.returnName())
        leaderCoCo2=self.findLeader(self.ConnectedComponents[edge[1][1]-1])
        #leaderCoCo1 = self.ConnectedComponents[(self.ConnectedComponents[edge[1][0]-1].returnLeader())-1]
        #leaderCoCo2 = self.ConnectedComponents[(self.ConnectedComponents[edge[1][1]-1].returnLeader())-1]
        #print(leaderCoCo2.returnName())
        coco1 = self.ConnectedComponents[edge[1][0]-1]
        coco2 = self.ConnectedComponents[edge[1][1]-1] 
        
        
        if(leaderCoCo1.returnSize() >= leaderCoCo2.returnSize()):
            #print("cosabello")
            if(leaderCoCo1 != leaderCoCo2):
                leaderCoCo1.changeSize(leaderCoCo1.returnSize() + leaderCoCo2.returnSize())
            else:
                 leaderCoCo1.changeSize(leaderCoCo1.returnSize() + 1)
                
            coco2.changeLeader(leaderCoCo1)     
            
            if(leaderCoCo1.addedge(edge)):
                #print("added")
                #leaderCoCo1.changePW(edge[0] + leaderCoCo2.returnPW())
                i = True
            #else:
                #print("not added")
                
                
            for k in leaderCoCo2.returnNodes():
                leaderCoCo1.addNode(k)               
            

            leaderCoCo2.changeLeader(coco2.returnLeader())
        else:
            #print("wut")
            if(leaderCoCo1 != leaderCoCo2):
                #print("cosabello2")
                leaderCoCo2.changeSize(leaderCoCo2.returnSize() + leaderCoCo1.returnSize())
            else:
                leaderCoCo2.changeSize(leaderCoCo1.returnSize() + 1)
 
                
            
            coco1.changeLeader(leaderCoCo2)     
            
            if(leaderCoCo2.addedge(edge)):
                #print("added")
                #leaderCoCo2.changePW(edge[0] + leaderCoCo1.returnPW())
                i = True
            #else:
                #print("not added")
                
            for k in leaderCoCo1.returnNodes():
                leaderCoCo2.addNode(k)               
            

            leaderCoCo2.changeLeader(coco1.returnLeader())
        
        
        if(i):
            return True
        else:
            return False
            
    def Printer(self):
        for e in self.ConnectedComponents:
            if(e != None):
                print("Nome: " + str(e.returnName()))
                print("Leader: " + str(e.returnLeader().returnName()))
                print("Size: " + str(e.returnSize()))
                print("Leader Size: " + str(self.ConnectedComponents[e.returnLeader().returnName()-1].returnSize()))
                print("Leader nodes: " + str(self.ConnectedComponents[e.returnLeader().returnName()-1].returnNodes()))
                print("total weight: " + str(self.ConnectedComponents[e.returnLeader().returnName()-1].returnPW()))
                print("\n")
                

    def returnCoCo(self):
        return self.ConnectedComponents

######################################### TEST #############################

jobsfile = open("/home/kalpof/daa/tests/t13.txt","r")
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
allCoCo = []
for e in nodes:
   
    U.addConnectedComponent(ConnectedComponent(int(e)))
    allCoCo.append(int(e))
    
    
#U.Printer()

edges.sort()
total = 0
#allCoCo = U.returnCoCo()
#print(edges)
i=0
#print(allCoCo)
for e in edges:
    #print(e)
    #U.Printer()
    if(U.Merge(e)):
        total += e[0]
        #i+=1
    
    try:
        allCoCo.remove(e[1][1])
        allCoCo.remove(e[1][0])
    except:
        try:
            allCoCo.remove(e[1][0])
        except:
            try:
                allCoCo.remove(e[1][0])
            except:
                i=0

    
    
        
    if(len(allCoCo) < 3):
        #print(i)
        #print("break")
        print(e)
        print(allCoCo)
        break
    
    #i+=1
    
    
    
    """
    if(i > len(nodes) + 7):
        print(e)
        break
    #print("\n")
    """

"""
for e in U.returnCoCo():
    print e.returnName()
    print e.returnEdges()
    print e.returnLeader()
"""   

#print(total)
    
#U.Printer()
    
print("fine")
    
    
"""

cose1 = []
for e in nodes:
   
    cose1.append(ConnectedComponent(int(e)))

U = UnionFind()

for e in cose1:
    U.addConnectedComponent(e)
    
    
"""
    
    
    














        
    