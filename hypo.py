import math
base=int(input("Enter the length of base:"))
per=int(input("Enter the length of perpendicular:"))
hypo=math.sqrt((per**2)+(base**2))
print("Hypotenuse of right angle triangle is",round(hypo,2))