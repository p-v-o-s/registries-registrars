import csv
import json


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

lengthBefore=len(data)

registries=list(set(registries))

for r in registries:
    atom={}
    atom["name"]=r
    atom["group"]=2
    data.append(atom)

with open(infile,'rb') as csvfile:
    spamreader = csv.reader(csvfile,delimiter=';')
    index=0
    for row in spamreader:
        regs=row[5].split(' ')
        for r in regs:
            link={}
            #print index, registries.index(r)+lengthBefore
            link["source"]=index
            link["target"]=registries.index(r)+lengthBefore
            link["value"]=1
            #print link
#            print link
            links.append(link)

        index=index+1

#print links

#data = [ { 'a':'A', 'b':(2, 4), 'c':3.0 } ]
#print 'DATA:', repr(data)
#print data

overarch={'nodes':data,'links':links}
#print overarch
#print overarch
#overarch={data,data}

data_string = json.dumps(overarch)
print data_string
#print data_string
#        print ', '.join(row)
