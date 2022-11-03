from typing import Any, List, Union
from linked_binary_tree_ext_abstract import LinkedBinaryTreeExtAbstract
from data_structures.trees.linked_binary_tree import LinkedBinaryTree
from data_structures import BinaryTreeNode


class LinkedBinaryTreeExt(LinkedBinaryTreeExtAbstract, LinkedBinaryTree):

    def hermanos(self, nodo1: BinaryTreeNode, nodo2: BinaryTreeNode) -> bool:
        return self._search_parent(nodo1) == self._search_parent(nodo2)

    def hojas(self) -> List[Any]:
        lista = []

        def agregar_elementos_hoja(node: BinaryTreeNode, list: List) -> None:
            if node:
                if (node.children_count() == 0):
                    list.append(node.element)

                agregar_elementos_hoja(node.left_child, list)
                agregar_elementos_hoja(node.right_child, list)
        agregar_elementos_hoja(self._root, lista)
        return lista

    def internos(self) -> List[Any]:
        lista = []

        def agregar_elementos_interos(node: BinaryTreeNode, list: List) -> None:
            if node:
                if (self._search_parent(node) != None and (node.left_child != None or node.right_child != None)):
                    list.append(node.element)

                agregar_elementos_interos(node.left_child, list)
                agregar_elementos_interos(node.right_child, list)
        agregar_elementos_interos(self._root, lista)
        return lista

    def profundidad(self, nodo: BinaryTreeNode) -> int:
        def encontrar_profundidad(node: BinaryTreeNode) -> int:
            if node:
                if (self._search_parent(node) != None):
                    node = self._search_parent(node)
                    return 1 + encontrar_profundidad(node)
                else:
                    return 0

        return encontrar_profundidad(nodo)

    def altura(self, nodo: BinaryTreeNode) -> int:
        def encontrar_altura(node: BinaryTreeNode) -> int:
            if node:
                if (node.left_child != None):
                    return 1 + encontrar_altura(node.right_child)
                elif (node.right_child != None):
                    return 1 + encontrar_altura(node.left_child)
                else:
                    return 0

        return encontrar_altura(nodo)
