import csv
import json

with open('rr1.csv','rb') as csvfile:
    spamreader = csv.reader(csvfile,delimiter=';')
    for row in spamreader:
        print row[4]

data = [ { 'a':'A', 'b':(2, 4), 'c':3.0 } ]
print 'DATA:', repr(data)

data_string = json.dumps(data)
print 'JSON:', data_string
#        print ', '.join(row)
