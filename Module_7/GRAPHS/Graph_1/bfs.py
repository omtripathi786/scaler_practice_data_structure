from visualize_graph import visualize_graph_from_adj_list


def bfs(graph, start=0):
    visited = [False] * len(graph)
    queue = [start]
    while queue:
        vertex = queue.pop(0)
        if not visited[vertex]:
            print(vertex, end='--->')
            visited[vertex] = True
            for neighbor in graph[vertex]:
                if not visited[neighbor]:
                    queue.append(neighbor)


if __name__ == '__main__':
    graph = [[2, 3], [4], [0, 3, 4], [2, 4, 0], [1, 3, 2]]
    visualize_graph_from_adj_list(graph)
    bfs(graph)
