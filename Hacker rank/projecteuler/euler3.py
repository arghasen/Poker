# Project Euler #3: Largest prime factor
import math
count = int(raw_input())
for i in range(count):
    maxval = int(raw_input())
    maxprime =1
    while (maxval%2==0):
        maxval=maxval/2
        maxprime=2        
    for x in xrange(3,int(math.sqrt(maxval))+1,2 ):
        while (maxval%x == 0)
            print x;
            maxval = maxval/x;
            maxprime =x
        if maxval==1:
            break
    print maxprime
        