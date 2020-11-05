# Calling dfs function will traverse and print using dfs method

def graphSort(graph):
    newGraph = dict()
    for key in graph:
        lst = graph[key]
        lst.sort()
        newGraph[key] = lst
    return newGraph

stack = []

def dfs(graphMap, currentNode):
    graph = graphSort(graphMap)
    dict_map = dict()
    for node in graphMap:
        dict_map[node] = False
    traverse(graph, currentNode, dict_map)

def traverse(graph, currentNode, dict_map):
    stack.append(currentNode)
    for node in graph[currentNode]:
        if node not in stack:
            traverse(graph, node, dict_map)
    if dict_map[stack[-1]] != True:
        dict_map[stack[-1]] = True
        print(stack.pop())
