import random 
import math 
import matplotlib.patches as patches
import pylab
# import numpy as np
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
        # distance_list.append(int(distance))
        # print(distance)
        # print(int(distance)//2)
    # print("Distance",distance_list)
    perimeter = sum(distance_list)
    return distance_list, perimeter
    # final_arr = np.array(distance_list)/np.amax(distance_list)
    # print(final_arr)

def points_generation(distance, perimeter, points_gen):
    factor = 990//perimeter #n-10/perimeter
    final_array = []
    print(factor)
    for i in range(len(distance)):
        # print(distance[i], perimeter, points_gen[i], points_gen[i+1])
        dis = distance[i]
        final_array.append(points_gen[i])
        x1 = points_gen[i][0]
        y1 = points_gen[i][1]
        x2 = points_gen[i+1][0]
        y2 = points_gen[i+1][1]
        x = x1
        y = y1
        num_points = int(factor*dis)
        print(factor,num_points, dis)
        slope = abs((y2-y1)/(x2-x1))
        for k in range(num_points):
            new_x = x
            x = math.cos(math.atan(slope))*(x + (num_points/dis)) + random.uniform(-ampl,ampl)
            y = (new_x + (num_points/dis))*slope+ random.uniform(-ampl,ampl)
            final_array.append([x, y])
    return final_array



points_gen = hull_generation(1000)
print(len(points_gen))
distance_list, perimeter = perimeter_gen(points_gen)

print("Distance_List", distance_list)
print("Perimeter", int(perimeter))

final_array = points_generation(distance_list, perimeter, points_gen)
final_array.append(points_gen[-1])

# pylab.scatter([p[0] for p in final_array],[p[1] for p in final_array])
#     #plot border lines
#     #pylab.gca().set_aspect('equal', adjustable='box')
# pylab.gca().add_patch(patches.Polygon(final_array,closed=True,fill=False))
# pylab.grid()
# pylab.show()

pylab.scatter([p[0] for p in points_gen],[p[1] for p in points_gen])
    #plot border lines
    #pylab.gca().set_aspect('equal', adjustable='box')
pylab.gca().add_patch(patches.Polygon(points_gen,closed=True,fill=False))
pylab.grid()
pylab.show()