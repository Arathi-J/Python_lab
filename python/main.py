from graphics import rectangle,circle
from graphics.threeD_graphics import cuboid,sphere

#using triangle  module 

b=int(input("Enter the breadth of the triangle = "))
h=int(input("Enter the height of the triangle = "))
print("area of the triangle = ",triangle.area(l,b))


#using square module
a=int(input("\nEnter the side of the square = "))
print("area of of the square = ",square.area(a))
print("perimeter of the square = ",square.perimeter(a))


#using rectangle module 

l=int(input("Enter the length of the rectangle = "))
b=int(input("Enter the breadth of the rectangle = "))
print("area of the rectangle= ",rectangle.area(l,b))
print("perimeter of the rectangle = ",rectangle.perimeter(l,b))

#using circle module

r=int(input("\nEnter the radius of the circle = "))
print("area of the circle = ",circle.area(r))
print("perimeter of the circle = ",circle.perimeter(r))

#using cuboid module

l=int(input("\nEnter the length of the cupid = "))
b=int(input("Enter the breadth of the cupid = "))
h=int(input("Enter the height of the cupid = "))
print("surface area of the cupid = ",cuboid.surface_area(l,b,h))
print("volume of the cuboid = ",cuboid.volume(l,b,h))

#using shere module
r=int(input("\nEnter the radius of the sphere = "))
print("surface area of the sphere = ",sphere.surface_area(r))
print("volume of the cupid = ",sphere.volume(r))
