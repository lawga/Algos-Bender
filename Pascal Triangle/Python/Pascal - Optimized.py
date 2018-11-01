from math import floor

def pascal(x, y):
    if (x<=0 or y<=0) : return 1
    if (x==1 and y==1) : return 1
    if (y>x) : return 0
    return pascal(x-1, y) + pascal(x-1, y-1)

import time
start = time.time() #start timer

x = 15
y = 0

for i in range(0, x):
    a = []
    if (i) % 2 == 0: #since we start from line #0 and number of columns = line# +1
        num = "even"
        k = floor((i+1)/2)+1
    else:
        num = "odd"
        k = floor((i+1)/2) 
    for j in range(0, k):
        a.append(pascal(i,j)) #Calculate the first half
        print(a[j], end=" ")  #print the 1st half in the line
    if num == "even":
        for l in range(k-2,-1,-1):
            print(a[l], end=" ") #print the 2nd half (mirrored from the center) - ODD NUMBER OF COLUMNS
    else:
        for l in range(k-1,-1,-1):
            print(a[l], end=" ") #print the 2nd half (mirrored from the center) - EVEN NUMBER OF COLUMNS
    print()

end = time.time() #end timer
print(end - start) #print the time elapsed 