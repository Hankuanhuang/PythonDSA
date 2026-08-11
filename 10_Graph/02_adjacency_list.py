graph = { ##Undirected Graph
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}
print(graph["A"])
print(graph["B"])
