from binarytree import build


def lca_bst(root, x, y):
    curr = root
    while curr:
        if x < curr.value and y < curr.value:
            curr = curr.left
        elif x > curr.value and y > curr.value:
            curr = curr.right
        else:
            return curr.value
    return None


if __name__ == "__main__":
    nodes = [7, 3, 15, 1, 5, 8, 20, 0, 2, 4, 6, None, None, 17, 26]
    root = build(nodes)
    print(root)
    print(lca_bst(root, 0, 26))
