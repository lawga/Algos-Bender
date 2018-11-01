from math import floor

def pascal(x, y):
    if (x==0 and y==0) : 
        array[x][y] = 1
        return array[x][y]
    if (x==y) : 
        array[x][y] = 1
        return array[x][y]
    if (y>x) : return 0
    return array[x-1][y] + array[x-1][y-1] 

import time
start = time.time() #start timer

x = 15
y = 0
k = [0 for location in range(x)]
array = [[0 for location in range(x)] for b in range(x)]

for i in range(0, x):
    
    if i % 2 == 0:
        num = "even"
        k[i] = floor((i+1)/2)+1
    else:
        num = "odd"
        k[i] = floor((i+1)/2) 
    for j in range(0, k[i]):
        array[i][j] = pascal(i,j) #Calculate the first half
        print(array[i][j], end=" ")  #print the 1st half in the line
    if num == "odd":
        for l in range(1,k[i]+1,1):
            array[i][k[i]+l-1]=array[i][k[i]-l]
            print(array[i][k[i]+l-1], end=" ") #print the 2nd half (mirrored from the center) - ODD NUMBER OF COLUMNS
    else:
        for l in range(1,k[i],1):
            array[i][k[i]+l-1]=array[i][k[i]-l-1]
            print(array[i][k[i]+l-1], end=" ") #print the 2nd half (mirrored from the center) - EVEN NUMBER OF COLUMNS
    print()

end = time.time() #end timer
print(end - start) #print the time elapsed  
