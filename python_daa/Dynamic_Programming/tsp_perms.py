graph = [[0,10,15,20],
         [5,0,9,10],
         [6,13,0,12],
         [8,8,9,0]]




def tsp(start,og_start,vertex_set,graph):


    if not vertex_set:
        return graph[start][og_start]

    total_cost = []

    for point in vertex_set:

        v_copy = vertex_set.copy()
        v_copy.remove(point)  # removing the point travelled to , from the start point
        
        cost = graph[start][point] + tsp(point,og_start,v_copy,graph=graph) 
        
        total_cost.append(cost)

    print("This is total_cost",total_cost)
    return min(total_cost)


print(tsp(0,0,vertex_set={1,2,3},graph = graph))