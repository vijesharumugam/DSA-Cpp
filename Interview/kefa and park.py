from collections import defaultdict

def solution(n,m,A):
    res = 0
    adj = defaultdict(list)
    visited = set()
    for i in range(n-1):
        x,y = map(int,input().split())
        adj[x].append(y)
        adj[y].append(x)
    stack = [(1,0)]
    while stack:
        v,c = stack.pop()
        if v in visited:
            continue
        visited.add(v)
        if A[v-1]==1:
            c+=1
        else:
            c = 0 
        if c>m:
            continue
        if v!=1 and len(adj[v])==1:
            res +=1
        else:
            for aj in adj[v]:
                if aj not in visited:
                    stack.append([aj,c])


    return res,visited

n,m = map(int,input().split())
A = list(map(int,input().split()))
print(solution(n,m,A))