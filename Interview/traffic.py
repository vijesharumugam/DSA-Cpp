from collections import defaultdict

def getPath(x,y):
    path = []
    while(x!=y):
        if x > y:
            path.append(x)
            x=x//2
        else:
            path.append(y)
            y=y//2
    return path



q = int(input())
toll = defaultdict(int)
tot = 0
for i in range(q):
    qt,x,y,t = map(int,input().split())
    path = getPath(x,y)
    if qt ==1:
        for i in path:
            toll[i]+=t
    else:
        sm = 0
        for i in path:
            sm+=toll[i]
        tot+=sm
        print(sm)
print(tot)


        