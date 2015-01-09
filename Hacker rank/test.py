import itertools
T = int(raw_input())
for t in range(T):
    n, m = map(int, raw_input().split())
    powers = {}
    bullets = {}
    origBullet = 0
    levelBullet = 0
    for ni in range( n):
        powers[ni] = map(int, raw_input().split())
    for ni in range( n):
        bullets[ni] = map(int, raw_input().split())
    maxorig= float("inf")
    revn =list(reversed(range(1,n)))
    curn =list(range(1,n))
    lastrow = min(powers[n-1])
    dp ={}
    def createpath(tup,x):
        orig=0
        for j in list(reversed(range(1,x))):
            cur= i[j]
            lev = bullets[j-1][i[j-1]]  
            orig+= powers[j][cur] - lev if powers[j][cur] - lev>0 else 0
            dp[i[j-1:]]=orig
    for i in itertools.product(range(m),repeat=n):
        orig =0
        lev=0
        for x in curn:
            nextpath = dp.get(i[x:])
            if nextpath:
                orig+=nextpath
                if orig <maxorig :
                    maxorig =orig
                break
            else:
                createpath(i,x)      
    print maxorig
    print dp
