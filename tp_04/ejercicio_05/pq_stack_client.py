import unittest
from priority_queue_stack import PriorityQueueStack


class TestPQStack(unittest.TestCase):

    def test_empty_ok(self):
        stack = PriorityQueueStack()
        self.assertEqual(stack.is_empty(), True)
        stack.push(1)
        stack.pop()
        self.assertEqual(stack.is_empty(), True)

    def test_not_empty_ok(self):
        stack = PriorityQueueStack()
        stack.push("hola")
        self.assertEqual(stack.is_empty(), False)

    def test_size_ok(self):
        stack = PriorityQueueStack()
        stack.push(1)
        self.assertEqual(stack.size(), 1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        self.assertEqual(stack.size(), 4)
        stack.pop()
        self.assertEqual(stack.size(), 3)

    def test_peek_ok(self):
        stack = PriorityQueueStack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        stack.push(5)
        self.assertEqual(stack.peek(), 5)
        stack.pop()
        self.assertEqual(stack.peek(), 4)

    def test_pop_ok(self):
        stack = PriorityQueueStack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        stack.push(5)
        self.assertEqual(stack.pop(), 5)
        self.assertEqual(stack.pop(), 4)
        stack.push(40)
        self.assertEqual(stack.pop(), 40)


if __name__ == '__main__':
    unittest.main()
