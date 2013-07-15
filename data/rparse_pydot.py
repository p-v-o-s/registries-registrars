import csv
import json
import pydot

graph=pydot.Dot(graph_type='digraph')

data=[]
links=[]

registries=[]

infile='rr2.csv'

with open(infile,'rb') as csvfile:
    spamreader = csv.reader(csvfile,delimiter=';')
    for row in spamreader:
        regs=row[5].split(' ')
        for r in regs:
            registries.append(r)
        atom={}
        company=row[0]
#        company=unicode(company, errors='ignore')
#        company=company.decode("cp1252", "ignore")
        atom["name"]="company"
        atom["group"]=1
        data.append(atom)

        newNode=pydot.Node(company, style="filled", fillcolor="green")
        graph.add_node(newNode)

