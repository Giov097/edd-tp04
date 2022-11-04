from typing import Any
from tp_04.ejercicio_03.unsorted_priority_queue import UnsortedPriorityQueue


class PriorityQueueStack:

    def __init__(self) -> None:
        self._next_priority = 0
        self._stack = UnsortedPriorityQueue()

    def is_empty(self):
        return self._stack.is_empty()

    def push(self, v: Any):
        self._stack.add(self._next_priority, v)
        self._next_priority -= 1

    def size(self) -> int:
        return self._stack.__len__()

    def peek(self) -> Any:
        return self._stack.min()[1]

    def pop(self) -> Any:
        return self._stack.remove_min()[1]