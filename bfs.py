# Calling bfs function will traverse and print using bfs method

def graphSort(graph):
    newGraph = dict()
    for key in graph:
        lst = graph[key]
        lst.sort()
        newGraph[key] = lst
    return newGraph

queue = []

def bfs(graphMap, currentNode):
    graph = graphSort(graphMap)
    completed = []
    completed.append(currentNode)
    print(currentNode)
    traversebfs(graph, currentNode, completed)
    
def traversebfs(graph, currentNode, completed): 
    for node in graph[currentNode]:
        if node not in completed:
            print(node)
            completed.append(node)
            queue.append(node)
    if len(queue) != 0:        
        traversebfs(graph, queue.pop(0), completed)
