from typing import get_args


def countNetwork(graph):
    network = {}
    traversed = []
    count = 0
    for i in graph:
        if i not in traversed:
            count += 1
            networkData = call(i, graph)
            network[count] = networkData
            traversed += networkData

    return network

def call(value, graph):
    queue = [value] 
    traversed = []
    
    while len(queue) > 0:
        for i in graph[queue[0]]:
            if i not in queue and i not in traversed:queue.insert(-1, i)
        
        traversed.insert(-1, queue[0])
        queue.pop(0)
    
    return traversed
        

graph = {
    "A":["B","C"],
    "B":["A","D"],
    "C":["A","D"],
    "D":["B","C"],
    "E":["F"],
    "F":["E"],
}
             
countNetwork(graph)         