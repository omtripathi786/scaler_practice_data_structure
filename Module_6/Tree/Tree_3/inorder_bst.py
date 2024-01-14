from binarytree import build


def inorder_bst_nodes(root, ans=None):
    if ans is None:
        ans = []
    if root is not None:
        inorder_bst_nodes(root.left, ans)
        ans.append(root.value)
        inorder_bst_nodes(root.right, ans)
    return ans


if __name__ == "__main__":
    nodes = [7, 3, 15, 1, 5, 8, 20, 0, 2, 4, 6, None, None, 17, 26]
    root = build(nodes)
    print(root)
    print(inorder_bst_nodes(root))
