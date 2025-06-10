def dfs(visited, graph,path, root, goal):
    if root not in visited :
        visited.add(root)
        path.append(root)
        # print(root)
        if root == goal:
            return path
        for neighbour in graph[root]:
            result = dfs(visited, graph,path, neighbour, goal)
            if result:
                return result

graph = {
    "A": ["B", "D", "E"],
    "B": ["A", "C"],
    "C": ["B", "D"],
    "D": ["A", "C", "E"],  
    "E": ["A", "D"]
}
path = []
visited = set()
path=[]
path = dfs(visited, graph,path, "A", "Z")
print(path)