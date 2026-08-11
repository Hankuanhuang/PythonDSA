graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B"],
    "F": ["C"]
}


def dfs_stack(graph, start):
    stack = []
    visited = set()

    stack.append(start)

    while stack:
        current = stack.pop()

        if current not in visited:
            visited.add(current)
            print(current)

            for neighbor in graph[current]:
                if neighbor not in visited:
                    stack.append(neighbor)

dfs_stack(graph, "A")