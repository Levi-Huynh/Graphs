from util import Stack, Queue  # These may come in handy

'''
Write a function that takes a 2D binary array and returns the number of 1 islands.
An island consists of 1s that are connected to the north, south, east or west.

For example:

-nodes:  slands are connected components (in the direction of N, S, W, E only, not diagonal)
-edges: where 1's are connected 
-BFS/DFS- BFS (exposes more connections across the matrix sooner/shorter path)
-directed/undirected- undirected (can go either direction with 1's in the connection)
-cyclic/acyclic : undirected, normally cyclic  4 1's example is possible

-Tuples can be hashed/ used as key for dicts (its immutable)

islands = [[0, 1, 0, 1, 0],   
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

print(island_counter(islands)) # returns 4

LEVI'S
islands[range 5][range 5]

if island[i][j] =has 1 neighbor in matrix:=> BEFORE, island[i+1][j], [i+1][j+1] , [i+1][j-1],  AFTER, [i-1][j]  [i-1][j+1], [i-1][j-1]
create check to make sure in bounds 
island count+=1 

have starting vertext
iterate thru vertext to see if has neighbor 1 using helper function (with ^ given slots)
have helper function return all neighbors in N/W/E/S in a list
island count+=1 for length of neighgbor list returned from helper 
append neighbors to path copy that has starting vertex & all neighbors
plug into stack/que : i think stack (iterate from one row, depth wise, & explre all directions)
pop STACK wont unstack until take care of children DFS/deque BFS  
add to visited if not in visited
loop to return total island count (number of neighbors each vert in 2d array has)

other ideas:
-change 1 to 0 , check if there another 1 near now changed 0, repeat until theres no
one (how to check for 1 near zero?)
'''

# 1. Translate the problem into graphs terminology you've learned this week
# 2. Build your graph
# 3. Traverse your graph

""" friend {1: {2, 5}, 2: {1, 10, 6}, 3: set(), 4: {8, 9},
 5: {1, 7}, 6: {9, 2}, 7: {9, 10, 5}, 8: {4}, 9: {4, 6, 7}, 10: {2, 7}} """


def get_neighbors(vertex, graph_matrix):
    x = vertex[0]
    y = vertex[1]
    neighbors = []
    # Check north
    if y > 0 and graph_matrix[y - 1][x] == 1:
        neighbors.append((x, y-1))
    # Check south
    if y < len(graph_matrix) - 1 and graph_matrix[y + 1][x] == 1:
        neighbors.append((x, y+1))
    # Check east
    if x < len(graph_matrix[0]) - 1 and graph_matrix[y][x+1] == 1:
        neighbors.append((x+1, y))
    # Check west
    if x > 0 and graph_matrix[y][x-1] == 1:
        neighbors.append((x-1, y))
    return neighbors


def bft(x, y, matrix, visited):
    # create a queue
    q = Queue()
    # push the starting vertext
    q.enqueue((x, y))
    # while the stack is not empty..
    while q.size() > 0:
        # pop the first vertex
        v = q.dequeue()
        x = v[0]
        y = v[1]
        # check if its been visited
        # if it hasn't been visited
        if not visited[y][x]:
            # Mark it as visited
            visited[y][x] = True
            # Push all its neighbors onto the stack
            for neighbor in get_neighbors((x, y), matrix):  # STUB
                q.enqueue(neighbor)
    # Return an updated visited matrix w/ all connected components marked
    return visited


def island_counter(matrix):
    # we’re probably going to loop through the islands,
    # do bfs on them and count how many times that BFT occurs\
    # Create a visited matrix
    visited = []
    for i in range(len(matrix)):  # has 6 elements, 6 tall
        # all sub elements will have same len as first item matrx[0]: len(matrix[0])
        visited.append([False] * len(matrix[0]))
    # Create a counter, initialize to 0
    counter = 0
    # Walk through each cel in the original matrix
    for x in range(len(matrix[0])):  # columns
        # If it has not been visited...
        if not visited[y][x]:
            # If you reach a 1...
            if matrix[y][x] == 1:
                # Do a BFT and mark each 1 as visited
                visited = bft(x, y, matrix, visited)  # STUB
                # Increment counter by 1
                counter += 1
    return counter


islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

print(island_counter(islands))  # returns 4

islands = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
           [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
           [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
           [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
           [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
           [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
           [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
           [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
           [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
           [0, 0, 1, 1, 0, 1, 0, 0, 1, 0],
           [1, 0, 1, 1, 0, 1, 0, 0, 1, 0],
           [1, 0, 1, 1, 0, 1, 0, 0, 1, 0],
           [1, 0, 1, 1, 0, 1, 0, 0, 1, 0]]

print(island_counter(islands))  # 14
