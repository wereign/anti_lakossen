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

    return min(total_cost)



def wrapper_function(starting_point,graph):

    start = starting_point
    og_start = starting_point
    vertex_set = set([i for i in range(len(graph))])
    vertex_set.remove(start)

    return tsp(start,og_start,vertex_set,graph)


print(wrapper_function(0,graph))    