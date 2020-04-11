
""" 2. Build graph
-nodes: parents /child
-edges: relationship between parent/child
-directed: parent can only be parent, child can only be child
-acyclic
- node on avg connected to more than 1/2 other nodes?: sparse
- DFS- find the farthest relationship/path

Given the dataset and the ID of an
individual in the dataset, returns their earliest known
ancestor – the one at the farthest distance from the input
individual.

If there is more than one ancestor tied for "earliest",
return the one with the lowest numeric ID.

If the input individual has no parents, the function should
return -1.

#if vertext has no more neighbors


Assuming a bit more memory usage is not a problem and if the first
item of your tuple is hashable, you can create a dict out of your
list of tuples and then looking up the
value is as simple as looking up a key from the dict

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                   (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
^ if has children, it is in ancester[tuple#][0]
^ if has parent it is in ancester[tuple#][1], if start is not in ancester[i][1], has no parent
^ track through list to check of parent has parent
^ once parent no longer has parent, return that vertex, thats the farthest ancestor

^ Extra:count the number of times its in ancester[i][1] == number of ancestors
 -other hints, can flip way its traversing towards ancestor
 and compare longest length 

 -we dont always need to bild vert/ edges.. no, b/c
 depends on type of DS underhood thats storing our
 argument 

 -focus on sprint challenge, vs sprint wording 
 """


from util import Stack, Queue


def get_parents(ancestors, start):
    arr_par = []
    for i in range(len(ancestors)):
        print("get parents", start, ancestors[i], ancestors[i][1])
        if start == ancestors[i][1]:
            print("start found", start, ancestors[i][1])
            arr_par.append(ancestors[i][0])

    if len(arr_par) > 0:
        return arr_par
    else:
        return None


def earliest_ancestor(ancestors, starting_node):
    s = Stack()
    s.push([starting_node])
    visited = set()

    # ancestors=[(), ()] is list of sets/tuples
    while s.size() > 0:
        # Pop the vertex from back/end of stack, keeps check all in stack in order
        path = s.pop()
        a = path[-1]  # last element in list
        stack_size = s.size()

        if a not in visited:  # only explore that node if not yet explored
            visited.add(a)
            amount_parents = len(visited)
            print("popped", a, "path", path, visited,
                  stack_size, s, amount_parents)
            find_parents = get_parents(ancestors, a)
            # if find parents exist, add parents to stack
            if find_parents is not None:
                # needs to return list of parents
                for parent in get_parents(ancestors, a):
                    path_copy = path.copy()

                    if parent is not None:
                        # each parent of 6 added [6, 5, 3 ] 3 is popped & check for parent
                        print("parent", parent)
                        path_copy.append(parent)
                    # [6,3,5] 3 or 5 is popped
                    # check for neighbor of 3 or 5,
                    # add parents of 3 to stack [6, 5, 2, 1]
                    # pop off 1
                    # check for parents of 1
                        s.push(path_copy)
                    # return negative one, if only one node was enqued& popped (resulting in len(visited)==1), & find_parent returns none
            if find_parents is None and stack_size == 0 and amount_parents == 1:
                return -1
            if find_parents is None and stack_size == 0 and amount_parents > 1:
                return a
            # returns smaller parent by default, since parents in tupls are sorted by
            # the smaller parent will always be popped last, since stack
            # pops by last in (larger parent appended last)


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                  (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(test_ancestors, 6))
