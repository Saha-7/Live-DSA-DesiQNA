from collections import deque
from collections import defaultdict


# Sample_Input
N = 5
M = 2
k = 4
Arr1 = [1, 1, 0, 1, 1]   
Arr2 = [[1,2],[2,3],[3,4],[4,5]]



def safeViewPoints(N, M, k, Arr1, Arr2):
    G = defaultdict(list)
    for u, v in Arr2:
        G[u].append(v)
        G[v].append(u)

    prefix = [0] * (N + 1)
    maxi = [0] * (N + 1)
    used = [0] * (N + 1)

    used[1] = 1
    prefix[1] = 1 if Arr1[0] == 0 else 0
    maxi[1] = prefix[1]

    q = deque([1])
    while q:
        v = q.popleft()
        for child in G[v]:
            if not used[child]:
                used[child] = 1
                q.append(child)
                if Arr1[child - 1] == 0:
                    prefix[child] = prefix[v] + 1
                else:
                    prefix[child] = 0          
                maxi[child] = max(prefix[child], maxi[v])  

    count = 0
    for i in range(2, N + 1):
        if len(G[i]) == 1 and maxi[i] <= M:
            count += 1
    return count



print(safeViewPoints(N, M, k, Arr1, Arr2))