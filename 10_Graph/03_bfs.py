## BFS = Bredadth-First Search (廣度優先搜尋）
## BFS = Queue + level by level search

# deque     → 容器
# append()  → 右邊加入
# popleft() → 左邊拿走

from collections import deque ## in collection library 

graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B"],
    "F": ["C"]
}

def bfs(graph, start):
    queue = deque()
    visited = set()

    queue.append(start) ## add start to the queue
    visited.add(start) ## mark start as visited

    while queue: ## queue container still have value and keep do it
        current = queue.popleft()    

        print(current)

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


bfs(graph, "A")

# queue     → 等待處理的 Vertex
# current   → 現在處理的 Vertex
# neighbor  → current 旁邊的 Vertex
# visited   → 已經去過的 Vertex