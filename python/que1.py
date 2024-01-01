#write a program to find the sum of elements in list of numbers

li=[]
n=int(input('Enter te number of elements in the list '))
for i in range(n):
  x=int(input())
  li.append(x)
print(li)
print(sum(li))
