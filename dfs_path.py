def dfs(graph, start, goal):
    stack = [start]
    visited = set()
    path = []
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            path.append(vertex)
            print(vertex)
            if vertex == goal :
                return path
            for neighbour in graph[vertex]:
                if neighbour not in visited:

                    stack.append(neighbour)
    return None

graph = {
    "A": ["B", "D", "E"],
    "B": ["A", "C"],
    "C": ["B", "D"],
    "D": ["A", "C", "E"],  
    "E": ["A", "D"]
}


path = dfs(graph, "A", "C")
print(path)
    

