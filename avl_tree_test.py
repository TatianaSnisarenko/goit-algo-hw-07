import unittest
from avl_tree import AVLTree
import random


class TestAVLTree(unittest.TestCase):
    def setUp(self):
        self.tree = AVLTree()

    def test_empty_tree(self):
        self.assertIsNone(self.tree.root)

    def test_insertion(self):
        self.tree.insert(10)
        self.assertEqual(self.tree.root.key, 10)

    def test_height_after_insertion(self):
        self.tree.insert(10)
        self.tree.insert(20)
        self.assertEqual(self.tree.root.height, 2)

    def test_balance_after_insertion(self):
        keys = [10, 20, 30, 40]
        for key in keys:
            self.tree.insert(key)
        self.assertEqual(self.tree.get_balance(self.tree.root), -1)
        self.tree.insert(15)
        self.tree.insert(3)
        self.assertEqual(self.tree.get_balance(self.tree.root), 0)

    def test_min_value_node(self):
        keys = random.sample(range(1, 100), 10)
        for key in keys:
            self.tree.insert(key)
        self.assertEqual(self.tree.min_value_node().key, min(keys))

    def test_max_value_node(self):
        keys = random.sample(range(1, 100), 10)
        for key in keys:
            self.tree.insert(key)
        self.assertEqual(self.tree.max_value_node().key, max(keys))

    def test_sum(self):
        keys = random.sample(range(1, 100), 10)
        for key in keys:
            self.tree.insert(key)
        self.assertEqual(self.tree.sum(), sum(keys))

    def test_deletion(self):
        self.tree.insert(10)
        self.tree.insert(20)
        self.tree.insert(30)
        self.tree.root = self.tree.delete_node(self.tree.root, 20)
        self.assertNotEqual(self.tree.root.key, 20)

    def test_height_after_deletion(self):
        self.tree.insert(10)
        self.tree.insert(20)
        self.tree.insert(30)
        self.tree.root = self.tree.delete_node(self.tree.root, 30)
        self.assertEqual(self.tree.root.height, 2)

    def test_balance_after_deletion(self):
        self.tree.insert(10)
        self.tree.insert(20)
        self.tree.insert(30)
        self.tree.root = self.tree.delete_node(self.tree.root, 30)
        self.assertEqual(self.tree.get_balance(self.tree.root), 1)


if __name__ == '__main__':
    unittest.main()
