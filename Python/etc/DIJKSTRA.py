# def dijkstra(node, edges, source_index = 0):
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
#         for v, w in adjacent_nodes[u].items():     # {'a': {'b': 4, 'd': 2}, ... }
#             path_length[v] = min(path_length[v], path_length[u] + w)

#     return path_length


# node = []
# edges = {}

# n = int(input("How many line : "))
# for i in range(n):
#     s, t, w = input("Input 2 point and weight : ").split()
#     if not s in node:
#         node.append(s)
#     if not t in node:
#         node.append(t)
#     edges[s,t] = int(w)

# s, t = input("start and end point : ").split()
# answer = dijkstra(node, edges, s)
# print("Shortest path = ", answer[t], end ='')



# def mst(graph, sum = 0):
#     check = {}
#     test = {}                              #create dict for get 2 point in g[][0]
#     for i in range(len(graph)):
#         test[graph[i][0]] = graph[i][1]
#     for (u, v), w in test.items():
#        # print(u,v,w)
#         if not u in check:
#             sum += w
#             check[u] = u
#             check[v] = u
#             #print("u = ",u,"\tv = ",v,"\theadU = ",check[u],"\theadV = ",check[v],"\tsum = ",sum,sep='')
#         elif not v in check:
#             sum += w
#             check[v] = check[u]    
#             #print("u = ",u,"\tv = ",v,"\theadU = ",check[u],"\theadV = ",check[v],"\tsum = ",sum,sep='')
#         elif check[u] != check [v]:
#             sum += w
#             #print("u = ",u,"\tv = ",v,"\theadU = ",check[u],"\theadV = ",check[v],"\tsum = ",sum,sep='')
#             for i in check:
#                 if check[i] == check[v] or check[u]:
#                     check[i] = check[u]   
# #    print(check)
#     return sum


# # check = node = []
# graph = edges = {}
# n = int(input("How many line : "))
# for i in range(n):
#     s, t, w = input("Input 2 point and weight : ").split()
#     # if not s in node:
#     #     node.append(s)
#     # if not t in node:
#     #     node.append(t)
#     edges[s,t] = int(w)
# #print(edges)
# sort_edges = sorted(edges.items(), key=lambda x: x[1])
# #for i in range(len(sort_edges)):
# #    graph[sort_edges[i][0]] = sort_edges[i][1]
# #print(sort_edges,graph)
# print("Minimum spanning tree = ",mst(sort_edges))

"""
graph = {
  'A' : ['B','E'],
  'B' : [],
  'C' : ['D'],
  'D' : [],
  'E' : ['C'],
}

visited = [] # List for visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node): #function for BFS
  visited.append(node)
  queue.append(node)

  while queue:          # Creating loop to visit each node
    m = queue.pop(0) 
    print (m, end = " ") 

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

# Driver Code
print("Following is the Breadth-First Search")
bfs(visited, graph, 'A')"""

#################################################################################################################################
#MST Kruskal's
def mst(graph, sum = 0):

    return sum


graph = edges = {}
n = int(input("\nHow many line : "))
for i in range(n):
    s, t, w = input("Input 2 point and weight : ").split()
    edges[w,s,t]
print(type(edges),edges)
print("Minimum spanning tree = ",mst(sort_edges))