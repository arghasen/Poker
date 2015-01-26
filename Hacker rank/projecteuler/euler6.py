#6: Sum square difference
count = int(raw_input())
for i in range(count):
    maxval = int(raw_input())
    sum1 = sum([x*x for x in xrange(1,maxval+1)])
    sum2 = pow(sum([x for x in xrange(1,maxval+1)]),2)
    print sum2- sum1