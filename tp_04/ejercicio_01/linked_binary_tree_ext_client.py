from data_structures import BinaryTreeNode
from linked_binary_tree_ext import LinkedBinaryTreeExt
from io import UnsupportedOperation
import unittest


class TestLinkedStackExt(unittest.TestCase):

    nodo_a = BinaryTreeNode('A')
    nodo_b = BinaryTreeNode('B')
    nodo_c = BinaryTreeNode('C')
    nodo_d = BinaryTreeNode('D')
    nodo_f = BinaryTreeNode('F')
    nodo_g = BinaryTreeNode('G')
    nodo_h = BinaryTreeNode('H')
    nodo_i = BinaryTreeNode('I')
    nodo_k = BinaryTreeNode('K')
    nodo_m = BinaryTreeNode('M')
    nodo_n = BinaryTreeNode('N')
    arbol = LinkedBinaryTreeExt()
    arbol.add_left_child(None, nodo_a)
    arbol.add_left_child(nodo_a, nodo_b)
    arbol.add_right_child(nodo_a, nodo_f)
    arbol.add_left_child(nodo_b, nodo_c)
    arbol.add_right_child(nodo_b, nodo_d)
    arbol.add_left_child(nodo_f, nodo_g)
    arbol.add_right_child(nodo_f, nodo_k)
    arbol.add_left_child(nodo_g, nodo_h)
    arbol.add_right_child(nodo_g, nodo_i)
    arbol.add_left_child(nodo_k, nodo_m)
    arbol.add_right_child(nodo_k, nodo_n)

    def test_hermanos(self):
        self.assertEqual(self.arbol.hermanos(self.nodo_b, self.nodo_f), True)

    def test_hojas(self):
        self.assertEqual(self.arbol.hojas(), "['C', 'D', 'H', 'I', 'M', 'N']")

    def test_internos(self):
        self.assertEqual(self.arbol.internos(), "['B', 'F', 'G', 'K']")

    def test_profundidad(self):
        self.assertEqual(self.arbol.profundidad(self.nodo_g), 2)

    def test_altura(self):
        self.assertEqual(self.arbol.altura(self.nodo_a), 3)


if __name__ == '__main__':
    unittest.main()
