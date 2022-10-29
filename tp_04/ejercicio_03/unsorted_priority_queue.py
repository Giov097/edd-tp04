from io import UnsupportedOperation
from operator import itemgetter
from typing import Dict, Tuple, Any

from unsorted_priority_queue_abstract import UnsortedPriorityQueueAbstract


class UnsortedPriortyQueue(UnsortedPriorityQueueAbstract):

    def __init__(self):
        self.size = 0
        self._queue = list()

    def __len__(self) -> int:
        return self.size

    def is_empty(self) -> bool:
        return self.size == 0

    def add(self, k: Any, v: Any) -> None:
        self._queue.append([k,v])
        self.size += 1

    def min(self) -> Tuple[Any]:
        if self.is_empty():
            raise UnsupportedOperation()
        return min(self._queue, key=lambda x:x[0])

    def remove_min(self) -> Tuple[Any]:
        if self.is_empty():
            raise UnsupportedOperation()
        removed = self.min()
        self._queue.remove(self.min())
        return removed
