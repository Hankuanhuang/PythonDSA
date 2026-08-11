## 1. garph is a bunch of node and line be connected
## 2. Vertex = one point
## 3. Edge = two point to be connected
## Graph = Vertex + Edge


# A ----- B
# |       |
# |       |
# C ----- D

# Vertex: A, B, C, D

# Edge:
# A - B
# A - C
# B - D
# C - D

# 4 Vertices
# 4 Edges

## Tree is more rules than graph
## Tree have to start from the top

vertices = ["A", "B", "C", "D"]

edges = [
    ("A", "B"),
    ("A", "C"),
    ("B", "D"),
    ("C", "D")
]
print("Vertices:", vertices)
print("Edges:", edges)