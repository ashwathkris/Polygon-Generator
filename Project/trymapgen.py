import random 
import math 
import matplotlib.patches as patches
import pylab
import numpy as np

ampl = 2
def hull_generation(n):
    output = []
    n = n//100
    for _ in range(n):
        x = random.randrange(-80, 80)
        y = random.randrange(-80, 80)
        output.append([x,y])
    output.sort(key=lambda p: math.atan2(p[1],p[0]))
    return output

def perimeter_gen(points):
    distance_list = []
    for i in range(len(points)-1):
        x1 = points[i][0]
        x2 = points[i+1][0]
        y1 = points[i][1]
        y2 = points[i+1][1]
        distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
        distance_list.append(distance)
    perimeter = sum(distance_list)
    return distance_list, perimeter

def points_generation(distance, perimeter, points_gen,n):
    final_array = list()
    factor = n/perimeter
    for i in range(len(distance)):
        # print(distance[i], perimeter, points_gen[i], points_gen[i+1])
        dis = distance[i]
        final_array.append(points_gen[i])
        x1 = points_gen[i][0]
        y1 = points_gen[i][1]
        x2 = points_gen[i+1][0]
        y2 = points_gen[i+1][1]
        final_array.append([x1,y1])
        slope = (y2-y1)/(x2-x1)
        no_of_points = int(factor*distance[i])
        move = dis/no_of_points
        x=x1;y=y1
        for j in range(no_of_points):
            if(slope==0):
                new_x = x + move
                new_y = y
            elif(x2>x1):
                new_x = x + move/math.cos(math.atan(slope))
                if(y2>y1):
                    new_y =y + move/math.sin(math.atan(slope))
                else:
                    new_y =y - move/math.sin(math.atan(slope))
            elif(x1>x2):
                new_x = x - move/math.cos(math.atan(slope))
                if(y2>y1):
                    new_y =y + move/math.sin(math.atan(slope))
                else:
                    new_y =y - move/math.sin(math.atan(slope))
            final_array.append([new_x,new_y])
    return final_array



points_gen = hull_generation(1000)
print(len(points_gen))
distance_list, perimeter = perimeter_gen(points_gen)
n=100;
final_array = points_generation(distance_list,perimeter,points_gen,n)
#print('points: ', points_gen)
print("Distance_List", distance_list)
print("Perimeter", int(perimeter))
print(len(final_array))

#final_array = points_generation(distance_list, perimeter, points_gen)
#final_array.append(points_gen[-1])

pylab.scatter([p[0] for p in final_array],[p[1] for p in final_array])
#     #plot border lines
#     #pylab.gca().set_aspect('equal', adjustable='box')
pylab.gca().add_patch(patches.Polygon(final_array,closed=True,fill=False))
pylab.grid()
pylab.show()

'''
pylab.scatter([p[0] for p in points_gen],[p[1] for p in points_gen])
    #plot border lines  
    #pylab.gca().set_aspect('equal', adjustable='box')
pylab.gca().add_patch(patches.Polygon(points_gen,closed=True,fill=False))
pylab.grid()
pylab.show()'''