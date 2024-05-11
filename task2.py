import random
from avl_tree import AVLTree


def find_min(tree: AVLTree):
    return tree.min_value_node().key


if __name__ == '__main__':
    tree = AVLTree()
    keys = random.sample(range(1, 1000), 100)
    for key in keys:
        tree.insert(key)
    print(find_min(tree))
    print(find_min(tree) == min(keys))
