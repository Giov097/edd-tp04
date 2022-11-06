from io import UnsupportedOperation
from heap_queue import HeapQueue
import unittest


class HeapQueueClient(unittest.TestCase):

    def test_empty_ok(self):
        heap_queue = HeapQueue()
        self.assertEqual(heap_queue.is_empty(), True)
        heap_queue.enqueue(1)
        self.assertEqual(heap_queue.is_empty(), False)
        heap_queue.dequeue()
        self.assertEqual(heap_queue.is_empty(), True)

    def test_len_ok(self):
        heap_queue = HeapQueue()
        heap_queue.enqueue("1")
        heap_queue.enqueue("2")
        heap_queue.enqueue("3")
        heap_queue.enqueue("4")
        heap_queue.enqueue("5")
        self.assertEqual(heap_queue.__len__(), 5)

    def test_peek_ok(self):
        heap_queue = HeapQueue()
        heap_queue.enqueue(1)
        self.assertEqual(heap_queue.peek(), 1)
        heap_queue.enqueue(2)
        heap_queue.enqueue(3)
        heap_queue.enqueue(4)
        heap_queue.enqueue(5)
        self.assertEqual(heap_queue.peek(), 1)
        heap_queue.dequeue()
        heap_queue.dequeue()
        self.assertEqual(heap_queue.peek(), 3)

    def test_peek_exception(self):
        heap_queue = HeapQueue()
        with self.assertRaises(Exception):
            heap_queue.peek()

    def test_dequeue_ok(self):
        heap_queue = HeapQueue()
        heap_queue.enqueue(1)
        heap_queue.enqueue(2)
        heap_queue.enqueue(3)
        self.assertEqual(heap_queue.dequeue(), 1)
        self.assertEqual(heap_queue.dequeue(), 2)
        heap_queue.enqueue(4)
        heap_queue.enqueue(5)
        self.assertEqual(heap_queue.dequeue(), 3)
        self.assertEqual(heap_queue.dequeue(), 4)
        self.assertEqual(heap_queue.dequeue(), 5)

    def test_dequeue_exception(self):
        heap_queue = HeapQueue()
        with self.assertRaises(Exception):
            heap_queue.dequeue()


if __name__ == '__main__':
    unittest.main()
