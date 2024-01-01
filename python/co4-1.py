class Rectangle:
  def __init__(self, length, bredth):
    self.length = length
    self.bredth = bredth
  def area(self):
    return self.length*self.bredth
  def peremeter(self):
    return 2*(self.length+self.bredth)
    
    
print("Enter length and bredth")
l1=int(input())
b1=int(input())
Rectangle1=Rectangle(l1,b1)
print("Area of rectangle 1",Rectangle1.area())
print("peremeter of rectangle 1",Rectangle1.peremeter())

l2=int(input())
b2=int(input())
Rectangle2=Rectangle(l2,b2)
print("Area of rectangle 2",Rectangle2.area())
print("peremeter of rectangle 2",Rectangle2.peremeter())

if Rectangle1.area()>Rectangle2.area():
  print("Area of rectangle1 is greater  than rectangle2")
elif Rectangle1.area()<Rectangle2.area():
  print("Area of rectangle2 is greater  than rectangle1")
else:
  print("Both are of same area")
