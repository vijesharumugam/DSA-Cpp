import heapq
def shortestPath(n,edge,src):
    h = [(0,src)]
    lis = [float('inf')]*n 
    lis[src] = 0
    while(h):
        d,i = heapq.heappop(h)
        if edge[i]!=-1:
            c = d + 1
            if c < lis[edge[i]]:
                lis[edge[i]] = c 
                heapq.heappush(h,(c,edge[i]))
    return lis


n = int(input())
edge = list(map(int,input().split()))
print(shortestPath(n,edge,0))

