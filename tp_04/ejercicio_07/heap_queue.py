from typing import Any
from data_structures import ArrayHeap


class HeapQueue:

    def __init__(self) -> None:
        self._data = ArrayHeap()
        self._priority = 0

    def __len__(self) -> int:
        return self._data.__len__()

    def is_empty(self) -> bool:
        return self.__len__() == 0

    def peek(self) -> Any:
        """Devuelve (sin quitar) el elemento ubicado en el frente de la cola. Raises:
                Exception: Arroja excepción si la estructura está vacía."""
        return self._data.min()[1]

    def dequeue(self) -> Any:
        """Remueve y devuelve el primer elemento de la cola. Raises:
                Exception: Arroja excepción si la estructura está vacía."""
        return self._data.remove_min()[1]

    def enqueue(self, elem: Any) -> None:
        """Agrega un elemento al final de la cola"""
        self._priority += 1
        self._data.add(self._priority, elem)
