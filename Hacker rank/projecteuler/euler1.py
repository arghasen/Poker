count = int(raw_input())
for i in range(count):
    maxval = int(raw_input())-1
    ap1=divmod(maxval,3)
    ap2=divmod(maxval,5)
    ap3=divmod(maxval,15)
    sum = ap1[0]*(3+maxval-ap1[1])/2+ap2[0]*(5+maxval-ap2[1])/2-ap3[0]*(15+maxval-ap3[1])/2
    print sum