import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from io import UnsupportedOperation
from typing import Any
from tp_04.ejercicio_03.unsorted_priority_queue import UnsortedPriorityQueue


class PriorityQueueStack:

    def __init__(self) -> None:
        self._next_priority = 0
        self._stack = UnsortedPriorityQueue()

    def is_empty(self):
        """Indica si la estructura está vacía o no."""
        return self._stack.is_empty()

    def push(self, v: Any):
        """Inserta un nuevo ítem en el tope de la estructura."""
        self._stack.add(self._next_priority, v)
        self._next_priority -= 1

    def size(self) -> int:
        """Devuelve la cantidad de elementos en la estructura"""
        return self._stack.__len__()

    def peek(self) -> Any:
        """Devuelve el primer elemento de la pila. Arroja excepción si está vacía"""
        return self._stack.min()[1]

    def pop(self) -> Any:
        """Quita y devuelve el primer elemento de la pila. Arroja excepción si está vacía"""
        return self._stack.remove_min()[1]
