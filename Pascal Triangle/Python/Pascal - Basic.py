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
    for j in range(0, i+1):
        print(pascal(i,j), end=" ") 
    print()

end = time.time() #end timer
print(end - start) #print the time elapsed