angle1 = float(input("Enter the angle1\n"))
angle2 = float(input("Enter the angle2\n"))
angle3 = float(input("Enter the angle3\n"))

if angle1 == angle2 and angle1 == angle3:
    print("The Triangle is equilateral")
elif angle1 == angle2 and angle1 != angle3:
    print("The Triangle is isosceles")
elif angle1 == angle3 and angle1 != angle2:
    print("The Triangle is isosceles")
elif angle2 == angle3 and angle2 != angle1:
    print("The Triangle is isosceles")
else:
    print("The Triangle is scalene ")
