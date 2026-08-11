## DFS = Depth-First Search （深度優先搜尋）
# 跟 BFS 相反：

# BFS → 一層一層
# DFS → 一條路走到底，再回頭

graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B"],
    "F": ["C"]
}

def dfs(graph, current, visited):
    visited.add(current)

    print(current)

    for neighbor in graph[current]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

dfs(graph, "A", set())