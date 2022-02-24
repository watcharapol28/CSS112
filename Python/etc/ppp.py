def dijkstra(graph, start, goal):
    shortest_distance = {}  # creating a dictionary to store shortest distance
    track_predecessor = {}  # keep track of the path
    unseenNodes = graph  # to iterate through the graph
    infinity = float("inf")  # infinity can a large number
    track_path = []  # going to trace our journey
    path = []

    for node in unseenNodes:
        shortest_distance[node] = infinity
        shortest_distance[start] = 0

    while unseenNodes:
        min_distance_node = None

        for node in unseenNodes:
            # print()
            # print("unseenNodes: ", unseenNodes)
            # print("shortest_distance: ", shortest_distance)
            # print("min_distance_node: ", min_distance_node)
            # print("track_predecessor: ", track_predecessor)
            # print('node', node)
            # print()
            if min_distance_node is None:
                min_distance_node = node
            elif shortest_distance[node] < shortest_distance[min_distance_node]:
                # print(f"short {shortest_distance[node]} : mindis  {shortest_distance[min_distance_node]}")
                min_distance_node = node

        path_options = graph[min_distance_node].items()
        # print("path_options: ", path_options)

        for child_node, weight in path_options:
            # print('weight + shortest distance[min_distanc_node]' , weight + shortest_distance[min_distance_node])
            if weight + shortest_distance[min_distance_node] < shortest_distance[child_node]:
                shortest_distance[child_node] = weight + shortest_distance[min_distance_node]
                track_predecessor[child_node] = min_distance_node

        unseenNodes.pop(min_distance_node)
    currentNode = goal
    while currentNode != start:
        try:
            track_path.insert(0, currentNode)
            currentNode = track_predecessor[currentNode]

        except KeyError:
            print('Path not reachable')
            break

    track_path.insert(0, start)

    if shortest_distance[goal] != infinity:
        print('Shortest distance is ' + str(shortest_distance[goal]))
        print('Path is ' + str(track_path))


dijkstra(graph, 'a', 'k')




"""#1 BFS
vec = [[] for i in range(100)]
q = []
check = []

def BFS():
    while len(q) != 0:
        #print(q)
        if not q[0] in check:
            check.append(q[0])
            print(q[0], end = ' ')
            if len(vec[q[0]]) != 0:
                for i in vec[q[0]]:
                    q.append(i)
        q.remove(q[0])

            
n = int(input("How many line : "))
for i in range(n):

    x, y = input("Input 2 point ").split()
    vec[int(x)].append(int(y))
    #vec[int(y)].append(int(x))
    if i == 0:
        begin = int(x)
q.append(begin)
BFS()

"""
#################################################################################################################################
#BFS
# q = []
# check = []
# graph = {}
# ans = [[]]
    
# def BFS():
#     while len(q) != 0:
#         check.append(q[0])
#         for i in graph[q[0]]:
#             if not i in check:
#                 q.append(i)
#         print(q[0], end = ' ')
#         q.remove(q[0])


# n = int(input("    ***  (BFS)  *** \nHow many line : "))
# for i in range(n):
#     print("[", i + 1, "]", sep = '', end = '')
#     x, y = input("Input 2 point : ").split()
#     if not x in graph:
#         graph[x]=[]
#     if not y in graph:
#         graph[y]=[]
#     graph[x].append(y)
#     graph[y].append(x)
#     if i == 0:
#         begin = x
# q.append(begin)
# print("BFS ", end ='-> ')
# BFS()


# #################################################################################################################################
# #DFS
# q = []
# check = []
# graph = {}
    
# def DFS():
#     while len(q) != 0:
#         value = q[0]
#         if not value in check:
#             print(value, end = ' ')
#         check.append(value)
#         q.remove(value)
#         nub = 0
#         for i in graph[value]:
#             if not i in check:
#                 q.insert(nub, i)
#                 nub += 1 
        

# n = int(input("\n\n    ***  (DFS)  *** \nHow many line : "))
# for i in range(n):
#     print("[", i + 1, "]", sep = '', end = '')
#     x, y = input("Input 2 point : ").split()
#     if not x in graph:
#         graph[x]=[]
#     if not y in graph:
#         graph[y]=[]
#     graph[x].append(y)
#     graph[y].append(x)
#     if i == 0:
#         begin = x
# q.append(begin)
# print("DFS ", end ='-> ')
# DFS()


#################################################################################################################################
# #Dijkstra Shortest path   credit NUT Nuttapon
# ans = {}
# def dijkstra(node, edges, ls):
#     path_length = { v: float('inf') for v in node }    # {'a': 0, 'b': inf, ...}
#     path_length[source_index] = 0
#     adjacent_nodes = { v: {} for v in node }    # {'a': {'b': 4, 'c': 2}, ... }
#     for (s, t), w in edges.items():
#         adjacent_nodes[s][t] = w
#         adjacent_nodes[t][s] = w
    
#     temporary_nodes = [v for v in node]
#     while len(temporary_nodes) != 0:
#         upper_bounds = { v: path_length[v] for v in temporary_nodes }  # {'a': 0, 'b': inf, ... } 
#         u = min(upper_bounds, key = upper_bounds.get)
#         #print(u, end = ' ')
#         temporary_nodes.remove(u)
#         for v, w in adjacent_nodes[u].items():     # {'a': {'b': 4, 'd': 2}, ... }\
#             if path_length[v] > path_length[u] + w:
#                 path_length[v] = path_length[u] + w
                      
#     #print(getlist)
#     return path_length


# node = []
# edges = {}

# n = int(input("\nHow many line : "))
# for i in range(n):
#     s, t, w = input("Input 2 point and weight : ").split()
#     if not s in node:
#         node.append(s)
#     if not t in node:
#         node.append(t)
#     edges[s,t] = int(w)
# ls = []
# s, t = input("start and end point : ").split()
# answer = dijkstra(node, edges, ls)
# print(ans)
# print("Shortest path = ", answer[t], end ='')

