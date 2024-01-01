import csv
field=['rollno','name','age']
sdict=[{'rollno':1,'name':Arathi,'age':33},
         {'rollno':4,'name':Anu,'age':20},
         {'rollno':3,'name':Aparna,'age':25},
         {'rollno':9,'name':Archana,'age':29}]
with open('dpt.csv','w')as dfile:
   writer=csv.DictWriter(dfile,fieldnames=field)
   writer.writeheder()
   writer.writerows(sdict)
data=pandas.read_csv("dpt.csv")
print(data)
