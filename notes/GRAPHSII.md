# DFS TK
Algo to search graph
Explores all poss paths to find one with `smallest weight` 
traverse `down branch to its deepest level, before trav across same level to another branch`
-start at root node 
-picks out one branch, trace all the way down to leaf nodes until can't continue
-only vising explore nodes 1 time 
-picks next branch until move to right

-APP:
-When only 1 solution to problem (ex maze has only one solution path (which is required to reach an end))
-when solution is required to search through the very end of paths (`bfs` doesnt search through `end of path`)
-When `know` solution is very far from root node

# DFS (STACK)
-`psedo code`
1. Begin at starting vertex(s)
2. Explore vertex
    a. Check if it has unexpored adjacent vertex(s)
        i. `mark as grey` (`being explored`) & explore if it child has adjacent vertex(s), _repeat_ until reach `end` of path for that branch 
        ii: `add` grey exploring vertex to stack
    b. If vertext has no more adjacent to explore, `Mark explored once all adjacent vertices have been explored` (`remove`vertext from stack, pop. Mark as `black` ) `STACK FILO` 




# BFS TK
Algo to search graph
Explores all poss paths to find one with `smallest weight` 
`Starting at levels closest to the root and finishing at those furthest away `
traverse `across before traversing down`
Never revisits nodes 

APPLICATION-
-Path finding /route finding (one city to another, roads closest first to city)
-Social networking, thru levels of connections, chance of knowing someone?
-solving derivative of 'shortest path' problem
-know solution not far from the root

# BFS (QUEUE)
`pseduo`
1. Begin at starting vertex (s) (can be root on tree, or labled starting on undirected graph) `mark grey as scheduled add to [queue] FIFO`
2. Explore vertex `loop`
    a. while at least 1 `undscheduled` vertices adjacent to current vertex
        i. `schedule` _all_ adjacent vertex to explore (mark to explore by adding to `[queue]`) `mark grey as scheduled add to queue`
3. If all adjacent vertices of current vertice has been `scheduled grey/added to to queue`, Mark vertex as explored (remove from queue) `mark black as scheduled, remove from queue` 
4. `Move on to next in line for Queue (FIFO)`, & `check for unscheduled` vertices, repeat 

LECTURE:
-Bidrectional: 
all bidrectional functinally same as undirected
twitter (everyone follows each other, direction of relationship is still `directed edges`)
-`undirected graphs` nature of relationship: every single edge  must be `directed`(undirected edges are just underhood most of time reprented with 2 directed edges )

=Graphs still considered data structure, despite being able to represent many types of network of data
- visited is a set b/c of the O(1) search, & unique. also order doesn't matter . memory will be worst for set than array. set is HT under hood, has extra empty allocated buckets. Collision handle, may have LL extra overhead memory
Arrays a bit more memory effecient than set, but trade off is faster time for set . 
Time only moves in one direction.  

`big diff trees vs graphs`:
graphs can be `cyclic`
(why visited track is important)

# UPER

1. Translate problem into graph terminology - Is this a graphs problem? 
2. Buid your graph 
    -what are the nodes? edges? cyclic/acyclic? directed/undirected? dense? parse? , DFS/BFS 
3. Traverse your graph 

https://github.com/dwyl/english-words

for word question:

Given a dictionary, and two words ‘start’ and ‘target’ (both of same length). Find length of the smallest chain from ‘start’ to ‘target’ if it exists, such that adjacent words in the chain only differ by one character and each word in the chain is a valid word i.e., it exists in the dictionary. It may be assumed that the ‘target’ word exists in dictionary and length of all dictionary words is same.

Example:

Input:  Dictionary = {POON, PLEE, SAME, POIE, PLEA, PLIE, POIN} or some word list 
             start = TOON
             target = PLEA
Output: 7
Explanation: TOON - POON - POIN - POIE - PLIE - PLEE - PLEA

2. `Graph components`: 
i. `Edge`: Relationship between each node/word is one word difference 
ii. `verticies` are word
iii. `cyclic undirected` (if can transform _both ways_ between word a & b, by the edge which is just one varying letter) *by definiation of undirected, if goes one way must go the other way 
iV.  ratio of edges to nodes here is `sparse` (1 word only connected to handful of other words):
    -`any given node is on average connected to more than 1/2 of other nodes` (1/2 is threshhold for `dense vs sparse`)
    -`fully connected graphs` nodes are connected to every other node 
v. `bfs / dfs`? bfs : shortest transformation sequence/ shortest path 



2. build graph
3. traverse graph (BFS

having a better Big O solution is the key here.  
-change word list from dict to set to have O(1) lookup?
-26* O(n) 
-shortcut for l in char_range('a', 'z'):?