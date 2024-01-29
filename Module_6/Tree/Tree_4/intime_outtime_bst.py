from binarytree import build


def in_time_out_time_bst(root):
    in_time, out_time = {}, {}
    t = [1]
    dfs(root, in_time, out_time, t)
    return in_time, out_time


def dfs(root, in_time, out_time, t):
    if root is None:
        return None
    in_time[root] = t[0]
    t[0] += 1
    if root.left:
        dfs(root.left, in_time, out_time, t)
    if root.right:
        dfs(root.right, in_time, out_time, t)
    out_time[root] = t[0]
    t[0] += 1


if __name__ == "__main__":
    nodes = [7, 3, 15, 1, 5, 8, 20, 0, 2, 4, 6, None, None, 17, 26]
    root = build(nodes)
    print(root)
    
