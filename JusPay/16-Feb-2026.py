"""
Link - https://docs.google.com/document/d/1KgK_cLtyQ3aArwfRD3TVFOoht72pOIc_TWddu7maED8/edit?tab=t.0
"""



from collections import deque
from collections import defaultdict


# Sample_Input
N = 5
M = 2
k = 4
Arr1 = [1, 1, 0, 1, 1]   
Arr2 = [[1,2],[2,3],[3,4],[4,5]]



def safeViewPoints(N, M, k, Arr1, Arr2):
    graph = defaultdict(list)
    for u, v in Arr2:
        graph[u].append(v)
        graph[v].append(u)

    prefix = [0] * (N + 1)
    maxi = [0] * (N + 1)
    used = [0] * (N + 1)

    used[1] = 1
    prefix[1] = 1 if Arr1[0] == 0 else 0
    maxi[1] = prefix[1]

    q = deque([1])
    while q:
        v = q.popleft()
        for child in graph[v]:
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
        if len(graph[i]) == 1 and maxi[i] <= M:
            count += 1
    return count



print(safeViewPoints(N, M, k, Arr1, Arr2))