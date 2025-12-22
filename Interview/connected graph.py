from collections import defaultdict

v = int(input())  
E = int(input())  

adj = defaultdict(list)

for i in range(E):
    v1, v2 = map(int, input().split())
    adj[v1].append(v2)
    adj[v2].append(v1)

co = 0
visited = set()

for i in range(v):
    if i not in visited:
        queue = [i]
        visited.add(i)
        while queue:
            node = queue.pop()
            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        co += 1

print(co)
