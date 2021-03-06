import csv
import json

import networkx as nx
import matplotlib.pyplot as plt


G=nx.Graph()


data=[]
links=[]

registries=[]

infile='rr2.csv'

index=0
with open(infile,'rb') as csvfile:
    spamreader = csv.reader(csvfile,delimiter=';')
    for row in spamreader:
        G.add_node(index)
        regs=row[5].split(' ')
        index=index+1
        for r in regs:
            registries.append(r)

lengthBefore=len(data)
registries=list(set(registries))

for r in registries:
    G.add_node(index)
    index=index+1

with open(infile,'rb') as csvfile:
    spamreader = csv.reader(csvfile,delimiter=';')
    index=0
    for row in spamreader:
        regs=row[5].split(' ')
        for r in regs:
            link={}
            #print index, registries.index(r)+lengthBefore
            G.add_edge(index,registries.index(r)+lengthBefore)

        index=index+1

pos=nx.graphviz_layout(G,prog="neato")
#pos=nx.graphviz_layout(G,prog='twopi',args='')
plt.figure(figsize=(8,8))
nx.draw(G,pos,node_size=20,alpha=0.5,node_color="blue", with_labels=False)
plt.axis('equal')
plt.savefig('circular_tree.png')
plt.show()
