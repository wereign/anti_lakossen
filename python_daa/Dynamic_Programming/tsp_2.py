# for creating permutations
from itertools import permutations

# this will import the maximum value a variable of data can store
# in the system
from sys import maxsize

# given adjacency matrix
cost = [[0,10,15,20],
        [5,0,25,10],
        [15,30,0,5],
        [15,10,20,0]]

# main tsp function
def tsp(cost,start):
  # empty list for storing all points except starting point
  grid = []

 # inserting all points except starting point in grid
  for i in range(len(cost)):
    if i != start:
      print(i)
      grid.append(i)

  # assigning maxsize to min_path variable variable
  # this will allow larger values of data to also be stored
  min_path = maxsize
  print('minpath:', min_path)

  # creating permutations of points in grid and storing in perm
  #printing perm -> will print the address location
  perm = permutations(grid)
  print('perms ',perm)

  for i in perm:
    print('perm here is: ', i)
    current_cost = 0
    # storing variable start in k, so we can itterate from start to other
    # nodes
    k = start

    # will print the original starting point
    print('value of k: ', k)
    # going inside the permutation tree and adding to current cost
    for j in i:
      current_cost += cost[k][j]
      # incrementing k or start to next index
      k = j
      print('k in for-for loop: ', k)

    # adding from last index back to starting node
    current_cost += cost[k][start]
    # min path will be the minimum of path and the current cost
    min_path = min(min_path,current_cost)
    print('min_path: ',min_path)
    print('\n')

  # when both the for loops get over, the min path variable will have the lowest
  # value of total cost possible

  return min_path

print('Cost of shortest path is: ', tsp(cost,0))