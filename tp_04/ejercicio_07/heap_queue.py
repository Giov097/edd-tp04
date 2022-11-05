from typing import Any

class HeapQueue:
    
    def __init__(self) -> None:
        self._data = []
    
    def __len__(self) -> int:
        return len(self._data)
        
    def is_empty(self) -> bool:
        return len(self) == 0

    def first(self) -> Any:
        """Devuelve (sin quitar) el elemento ubicado en el frente de la cola."""
        if self.is_empty(): 
            raise Exception("Heap vacío. No se puede continuar.")
        
        return self._data[0]
    
    def dequeue(self) -> Any:
        """Remueve y devuelve el primer elemento de la cola."""

        if self.is_empty():
            raise Exception("Estructura vacía. No se puede continuar")

        self._data[0], self._data[len(self._data) - 1] = self._data[len(self._data) - 1], self._data[0]
        item = self._data.pop()
        self._downheap(0)

        return item
    
    def enqueue(self, elem: Any) -> None:
        """Agrega un elemento al final de la cola"""

        self._data.append(elem)
        self._upheap(len(self._data) - 1)



    
    def _parent(self, j: int) -> int:
        return (j - 1) // 2

    def _left(self, j: int) -> int:
        return 2 * j + 1

    def _right(self, j: int) -> int:
        return 2 * j + 2

    def _has_left(self, j: int) -> bool:
        return self._left(j) < len(self._data)

    def _has_right(self, j: int) -> bool:
        return self._right(j) < len(self._data) 

    def _swap(self, i: int, j: int) -> None:
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, j: int) -> None:
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent)

    def _downheap(self, j: int) -> None:
        if self._has_left(j): 
            left = self._left(j)
            small_child = left
            
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    small_child = right
            
            if self._data[small_child] < self._data[j]:
                self._swap(j, small_child)
                self._downheap(small_child)