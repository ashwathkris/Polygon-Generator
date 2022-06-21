import matplotlib
import random
import math
import matplotlib.patches as patches
import pylab

n = 1000
factor = 1
complexity = 0
perimeter = 0
ver = n//100
hull = []
pos = 1
for _ in range(ver):
    x = random.randrange(-80,80)
    y = random.randrange(-80,80)
    hull.append([x,y])

x = 0; y = 0
ampl = 2
freq = 2

#sort by polar angle
hull.sort(key=lambda p: math.atan2(p[1],p[0]))
final_map = []

for i in range(0,(ver-1)):
    coord2 = hull[i+1]
    coord1 = hull[i]
    x2 = coord2[0]
    y2 = coord2[1]
    x1 = coord1[0]
    y1 = coord1[1]
    distance = math.sqrt(((x2-x1)**2)+((y2-y1)**2))
    x = x2-x1
    y = y2-y1
    x_factor = (x/distance)
    y_factor = (y/distance)
    x = x1
    y = y1
    distance = int(distance)//2
    count = 1
    final_map.append(hull[i])
    for _ in range(distance):
        x = x+(2*x_factor)+random.uniform(-ampl,ampl)
        y = y+(2*y_factor)+random.uniform(-ampl,ampl)
        final_map.append([x,y])
        count+=1
    #if(i+1<=ver-1):
    #    final_map.append(hull[i+1])
    #if(i+2<=ver-1):
    #    final_map.append(hull[i+2])

final_map.append(hull[ver-1])
pylab.scatter([p[0] for p in final_map],[p[1] for p in final_map])
#plot border lines
#pylab.gca().set_aspect('equal', adjustable='box')
pylab.gca().add_patch(patches.Polygon(final_map,closed=True,fill=False))
pylab.grid()
pylab.show()   