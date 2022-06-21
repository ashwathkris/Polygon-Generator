import csv
i = 1
with open('COUNTY.csv','rt')as file:
   csv_rows = csv.reader(file)
   for row in csv_rows:
      #print(row)
      i+=1
      if(i==6):
         a = row
         break


p = ''      #wkt format
for i in range(len(a[0])):
   if(a[0][i] == ')' and a[0][i+1]==')'):
      p+='))'
      break
   else:
      p+=a[0][i]


comma = 0
for i in p:
   if(i == ','):
      comma+=1
print('number of coords = ', comma+1)
