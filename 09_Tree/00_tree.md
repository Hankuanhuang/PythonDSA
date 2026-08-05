What is tree
    a hierarchical data structure
    each node can connect to other nodes
    Binary Tree = each node has at most 2 children


tree Node 
    Binary Tree have difference from linked list.
        will have root, left node, right node.
        root.left = store left value
        root.right = store right value

        root.left.left, root.left.right are more deep layer children


Traversal-preorder
    1. print the top root first 
    2. root -> left -> right
    3. A - > B -> D -> E -> C 
    4. top -> left -> right

Traversal-inorder
    1. print the left first
    2. left -> root -> right
    3. D -> B -> E -> A -> C

Traversal-postorder
    1. print the left first
    2. left -> right -> root
    3. D -> E -> B -> C -> A