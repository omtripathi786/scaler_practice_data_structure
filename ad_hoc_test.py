from binarytree import build


def bfs1(root):
    ans, q = [], [root]
    while q:
        node = q.pop(0)
        ans.append(node.value)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return ans


def bfs2(root):
    ans, q = [], [root]
    while q:
        level = []
        for _ in range(len(q)):
            node = q.pop(0)
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        ans.append(level)
    return ans


def vertical_order(root):
    queue, hash_map = [(root, 0)], {}
    while queue:
        node, col = queue.pop(0)
        if col not in hash_map:
            hash_map[col] = []
        hash_map[col].append(node.val)
        if node.left:
            queue.append((node.left, col - 1))
        if node.right:
            queue.append((node.right, col + 1))
    ans = []
    for col in sorted(hash_map.keys()):
        ans.append(hash_map[col][0])
    return ans


if __name__ == '__main__':
    nodes = [1, 2, 3, 5, 8, 10, 13, 6, None, None, None, 9, 7,
             4, None, None, None, None, None, None, None, None, None, None, None, 12, 11]
    root = build(nodes)
    print(root)
    print(bfs1(root))
    print(bfs2(root))
    nodes = [9, 6, 4, 2, 3, 5, 8, 6, 3, 10, 11, None, None]
    root = build(nodes)
    print(root)
    print(vertical_order(root))
