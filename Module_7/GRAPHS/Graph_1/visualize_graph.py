import networkx as nx
import matplotlib.pyplot as plt


def visualize_graph_from_adj_list(graph):
    G = nx.Graph()
    # Add edges based on your adjacency list
    for node, edges in enumerate(graph):
        for edge in edges:
            G.add_edge(node, edge)
    # Draw the graph
    nx.draw(G, with_labels=True)
    plt.show()


def visualize_graph_from_adj_matrix(matrix):
    G = nx.Graph()
    # Add edges based on your adjacency matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                G.add_edge(i, j)
    # Draw the graph
    nx.draw(G, with_labels=True)
    plt.show()


if __name__ == '__main__':
    # Your adjacency list
    graph = [[2, 3], [4], [0, 3, 4], [2, 4, 0], [1, 3, 2]]
    # Call the function
    visualize_graph_from_adj_list(graph)

    # Your adjacency matrix
    matrix = [
        [0, 0, 1, 1, 0],
        [0, 0, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [1, 0, 1, 0, 1],
        [0, 1, 1, 1, 0]
    ]
    # Call the function
    visualize_graph_from_adj_matrix(matrix)
