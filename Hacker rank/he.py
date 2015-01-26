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
    bullets[-1] = [0 for _ in range(m)]
    dpminbul={}
    def minbul(level=0):
            if dpminbul.get(level):
                return dpminbul[level]
            levelBullet = bullets[level-1]
            if level ==n:
                return 0
            dpminbul[level]=min([powers[level][i]-levelBullet[j]+minbul(level+1)if powers[level][i]-levelBullet[j] >0 else minbul(level+1)for i in range(m) for j in range(m)])
            return dpminbul[level]
    print minbul()