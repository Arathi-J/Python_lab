class Rectangle:
   def __init__(self, length, width):
   	self._length = length # Private attribute
   	self._width = width # Private attribute
   def area(self):
   	return self._length * self._width
   def __lt__(self, other):
   	return self.area() < other.area()

# Example usage:
print("Enter length and width for 1st rectangle")
l=int(input())
b=int(input())
rectangle1 = Rectangle(l, b)
print("Enter length and width for 2nd rectangle")
l1=int(input())
b1=int(input())
rectangle2 = Rectangle(l1, b1)
if rectangle1 < rectangle2:
   print("Area of Rectangle 1 is smaller than the area of Rectangle 2.")
elif rectangle1 > rectangle2:
   print("Area of Rectangle 1 is larger than the area of Rectangle 2.")
else:
   print("Both rectangles have the same area.")
