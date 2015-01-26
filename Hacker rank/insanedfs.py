# Enter your code here. Read input from STDIN. Print output to STDOUT
count = int(raw_input())
A =  [int(i) if i!='?'else i for i in raw_input().split()]
A1 =  [int(i) if i!='?'else 0 for i in A]
candidates =1
for i in xrange(count):
    if A[i]=='?' or A[i]<=i: #valid candidates only
        if A[i]=='?' and i!=0:
            candidates *=min(i, sum(A1))
    else:
        candidates =0
        break
print candidates


candidate_list =[]
for i in xrange(count):
    can=[]
    for j in range(count):
        can =can+[j]