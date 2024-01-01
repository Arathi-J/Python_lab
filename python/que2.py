#2.crete a list of num peform following op
#   a.smallest num from list
#   b.largest num from list
#   c.remove duplicates from the list
#   d.append a list of numbers to the existing list

li=[]
n=int(input('Enter te number of elements in the list '))
for i in range(n):
  x=int(input())
  li.append(x)
print(li)
print("Smallest : ",min(li))
print("Largest : ",max(li))
