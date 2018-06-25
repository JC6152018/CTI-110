# CTI-110
# P3T1 - Areas of Rectangles
# Jessica Washington
# June 24th, 2018

#This program tells which rectangle has the greater area
#or if the two rectangles have equal areas.

#Calculate the area of rectangle 1
rec1_length = int(input("Enter the length of rectangle 1:"))
rec1_width = int(input("Enter the width of rectangle 1:"))
rec1_area = rec1_length * rec1_width

#Calculate the area of rectangle 2
rec2_length = int(input("Enter the length of rectangle 2:"))
rec2_width = int(input("Enter the width of rectangle:"))
rec2_area = rec2_length * rec2_width

#Find which rectangle has the greater area, if they are not equal in areas
if rec1_area > rec2_area:
    print("Rectangle 1 has the greater area.")
elif rec1_area < rec2_area:
    print("Rectangle 2 has the greater area.")
else:
    print("Both rectangles have equal areas.")
    


