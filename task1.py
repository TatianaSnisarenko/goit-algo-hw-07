import random
from avl_tree import AVLTree


def find_max(tree: AVLTree):
    return tree.max_value_node().key


if __name__ == '__main__':
    tree = AVLTree()
    keys = random.sample(range(1, 1000), 100)
    for key in keys:
        tree.insert(key)
    print(find_max(tree))
    print(find_max(tree) == max(keys))
