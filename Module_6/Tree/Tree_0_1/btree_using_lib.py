from binarytree import build

# Generate a binary tree
nodes = [3, 6, 8, 2, 11, None, 13]
binary_tree = build(nodes)
print(binary_tree)

from graphviz import Digraph
from binarytree import build


def add_edges(graph, node, idx=0):
    if node:
        if node.left:
            graph.edge(str(idx), str(2 * idx + 1))
            add_edges(graph, node.left, 2 * idx + 1)
        if node.right:
            graph.edge(str(idx), str(2 * idx + 2))
            add_edges(graph, node.right, 2 * idx + 2)


def add_nodes(graph, node, idx=0):
    if node:
        graph.node(str(idx), str(node.value))
        add_nodes(graph, node.left, 2 * idx + 1)
        add_nodes(graph, node.right, 2 * idx + 2)


def draw_tree(tree):
    graph = Digraph()
    add_nodes(graph, tree)
    add_edges(graph, tree)
    return graph


# Create a binary tree
nodes = [1, 2, 3, 4, 5, None, None, None, None, None, None]
binary_tree = build(nodes)
# Draw the tree
graph = draw_tree(binary_tree)
graph.view()
