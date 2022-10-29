from io import UnsupportedOperation
import unittest
from unsorted_priority_queue import UnsortedPriortyQueue


class TestLinkedStackExt(unittest.TestCase):

    def test_empty(self):
        queue = UnsortedPriortyQueue()
        self.assertEqual(queue.is_empty(), True)
        queue.add(10, "Pochoclo")
        self.assertEqual(queue.is_empty(), False)

    def test_len(self):
        queue = UnsortedPriortyQueue()
        self.assertEqual(queue.__len__(), 0)
        queue.add(10, "Pochoclo")
        queue.add(7, "Puflito")
        queue.add(1, "Chizito")
        queue.add(10, "Tutuca")
        queue.add(5, "Pizzito")
        queue.add(1, "Palito")
        self.assertEqual(queue.__len__(), 6)

    def test_min(self):
        queue = UnsortedPriortyQueue()
        queue.add(10, "Pochoclo")
        queue.add(7, "Puflito")
        queue.add(1, "Chizito")
        queue.add(10, "Tutuca")
        queue.add(5, "Pizzito")
        queue.add(1, "Palito")
        self.assertEqual(queue.min(), [1, "Chizito"])

    def test_remove_min(self):
        queue = UnsortedPriortyQueue()
        queue.add(10, "Pochoclo")
        queue.add(7, "Puflito")
        queue.add(1, "Chizito")
        queue.add(10, "Tutuca")
        queue.add(5, "Pizzito")
        queue.add(1, "Palito")
        self.assertEqual(queue.remove_min(), [1, "Chizito"])
        self.assertEqual(queue.min(), [1, "Palito"])
        self.assertEqual(queue.remove_min(), [1, "Palito"])
        self.assertEqual(queue.min(), [5, "Pizzito"])

    def test_min_exception(self):
        queue = UnsortedPriortyQueue()
        with self.assertRaises(UnsupportedOperation):
            queue.min()

    def test_remove_min_exception(self):
        queue = UnsortedPriortyQueue()
        with self.assertRaises(UnsupportedOperation):
            queue.remove_min()


if __name__ == '__main__':
    unittest.main()
