count = int(raw_input())
for i in range(count):
    maxval = int(raw_input())
    a=1
    b=1
    c=0
    sum =0
    while c<=maxval:
        if c%2==0:
            sum+=c
        c = a+b
        a= b
        b= c

    print sum