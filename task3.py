import random
from avl_tree import AVLTree


def find_sum(tree: AVLTree):
    return tree.sum()


if __name__ == '__main__':
    tree = AVLTree()
    keys = random.sample(range(1, 1000), 100)
    for key in keys:
        tree.insert(key)
    print(find_sum(tree))
    print(find_sum(tree) == sum(keys))
