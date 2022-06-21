import math
x1=0
y1=0
x2=10
y2 = 10

n = 9

distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
move = distance/n 

slope = (y2-y1)/(x2-x1)
print(x1,y1)
x=x1
y=y1
for i in range(n):
	newx = x + move/math.cos(math.atan(slope))
	newy = y + move/math.sin(math.atan(slope))
	print(newx,newy)
	x=newx
	y=newy
