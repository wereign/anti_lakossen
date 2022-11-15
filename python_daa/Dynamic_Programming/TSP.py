from sys import maxsize
v = 4

def next_perm(l):
    n = len(l)
    i = n-2

    while i >= 0 and l[i] > l[i+1]:
        i -= 1
    
    if i == -1:
        return False

    j = i+1
    while j < n and l[j] > l[i]:
        j += 1

    j -= 1

    l[i], l[j] = l[j], l[i]
    left = i+1
    right = n-1

    while left < right:
        l[left], l[right] = l[right], l[left]
        left += 1
        right -= 1
    return True


def travelling_salesman_function(graph, s):
    vertex = []
    for i in range(v):
        if i != s:
            vertex.append(i)

    min_path = maxsize
    while True:
        current_cost = 0
        k = s
        for i in range(len(vertex)):
            current_cost += graph[k][vertex[i]]
            k = vertex[i]
        current_cost += graph[k][s]
        min_path = min(min_path, current_cost)

        if not next_perm(vertex):
            break
    return min_path




graph = [[0,10,15,20],[5,0,9,10],[6,13,0,12],[8,8,9,0]]
s = 0

print(travelling_salesman_function(graph,s))