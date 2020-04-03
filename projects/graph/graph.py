"""
Simple graph implementation

class notes:
sets & dicts are HT under hood

{
    '0': {'1', '3'},
    '1': {'0'},
    '2': set(),
    '3': {'0'}
}
^ dict of sets

-undirected/ bidirectional edges (0 points 1, 1 points 0)
(0 point 3, 3 points 0)
-.add_edge to node that doesn't exist, get exception

-for this problem all directed edges

"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.

        """
        # just add another row to our vertices
        # self.vertices[new row] = empty set
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # check if v1 & v2 exist as vertice
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            print("can't add to vertices that dont exist")

    def add_undirected_edge(self, v1, v2):
        """
        Add a un directed edge to the graph.
        """
        # check if v1 & v2 exist as vertice
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
        else:
            print("can't add to vertices that dont exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            print("Vertex id does not exist")
            raise ValueError("Vertex id does not exist")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        -Look at everything thats 1 away #does not have to be looked at in order L->R
        -Look at everything thats 2 away # ^
        -Look at everything thats 3 away  # ^
        etc...

        # create a queue FIFO
        # enqueue the starting vertix
        # create a set to store visited vertices
        # while queue is not empty:
                -Dequeue the first vertex
                # when dequeue, (queueing allows u to check if its been vistied in order) (check if in set?)
                # mark it as visited (if not, add to set) If has been visited, ignore, deque the next vertix in queue
                # enqueue all its neighbors (add its children BDT children to end of queue)
                    # (1 away, 2 away, 3 away ) 
                    # deque the next vert in FIFO order 
                    # check if been visited
                    # mark it as visited 
                    # enqueu its nieghbors /children (add to end of queue)

        q= []
        visited = {1,2,4,4,6,7,5}
        memorize pseduo, not code

        """
        # create a queue FIFO
        q = Queue()
        # enqueue the starting vertix
        q.enqueue(starting_vertex)
        # create a set to store visited vertices
        visited = set()
        # while queue is not empty:
        while q.size() > 0:
            # Dequeue the first vertex
            v = q.dequeue()
            # when dequeue, (queueing allows u to check if its been vistied in order)
            # (check if in set?)
            # mark it as visited (if not, add to set) If has been visited (else ignore, deque the next vertix in queue)
            if v not in visited:
                print(v)
                visited.add(v)
            # enqueue all its neighbors (add its children BDT children to end of queue)
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        DFT recursive application fits well:

        mark as visited
        do the thing (print, modify, do action)
        DFT traversal on each of children (parent of children wont return
        until traversal completed for children. left children always traversed
        first. 
        -PARENT stack will continue, after `all` its children return
        -DFT calls of parent & its 2nd child wont start until all the children's children children
        of the 1st child is completed/visted (in case where theres 2 childs of a parent) )
        -if its _been_ visted that node can return 

           # create a stack FILO/ LIFO (like pancake) related to RECURSION
        # PUSH the starting vertix to stack
        # create a set to store visited vertices
        # while stack is not empty:
                # Pop the vertex from back/end of stack
                # Check if its been visited
                # if it hasn't been visited:
                    # Mark it as visited
                    # Push all its neighbors onto the stck 

        # optimazations are tradeoffs based on the constraints of your system for time/space
        its all relative based on what kind of system youre operating in 

        """
        # create a stack FILO/ LIFO (like pancake) related to RECURSION
        s = Stack()
        # PUSH the starting vertix to stack
        s.push(starting_vertex)
        # create a set to store visited vertices
        visited = set()
        # while stack is not empty:
        while s.size() > 0:
            # Pop the vertex from back/end of stack
            v = s.pop()
            # Check if its been visited
            # if it hasn't been visited:
            if v not in visited:
                # Mark it as visited
                print(v)
                visited.add(v)
                # Push all its neighbors onto the stck
                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)

    # add default arg python gotchas docs.python.guide
    def dft_recursive(self, starting_vertex, visted=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # check if not node has been visited
        # if not...
        # mark it as visited #how to carry out visited set thru all recursive calls
        # nested recursive function
        # implement a helper

        # call dft_recursive on each neighbor

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list `PATH` containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create a queue FIFO
        # enqueue A PATH to starting vertix
        # create a set to store visited vertices
        # while queue is not empty:
        # Dequeue the first path
        # GRAB THE VERTEX FROM END OF PATH
        # check if its been visted
        # If hasn't been visited:
        # mark it as visisted
        # enquene A PATH to all its neighbors
        # MAKE A COPY OF THE PATH
        # ENQUE THE COPY

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)  # first arg is start node, 2nd arg is end node
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print: adjacent list 
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    # print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    # graph.bft(1)

    '''
    Valid DFT paths: (many)
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    # graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    # print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    # print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))

    # once build graph, get insight by analyzing relationships
    # neural networks, all graph traversals
    # nodes, relationships between nodes, which edges are more strongly correlated, neural netork
    # traversing will give you insights
