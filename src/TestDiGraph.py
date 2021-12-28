from unittest import TestCase

from src.DiGraph import DiGraph, Node


class TestDiGraph(TestCase):

    def test_v_size(self):
        g = DiGraph()
        for n in range(4):
            g.add_node(n)
        self.assertEqual(4, g.v_size())

    def test_e_size(self):
        g = DiGraph()
        for n in range(4):
            g.add_node(n)
        g.add_edge(0, 1, 1)
        g.add_edge(1, 0, 1.1)
        g.add_edge(1, 2, 1.3)
        g.add_edge(2, 3, 1.1)
        g.add_edge(1, 3, 1.9)
        self.assertEqual(5, g.e_size())

    def test_get_all_v(self):
        g = DiGraph()
        for n in range(4):
            g.add_node(n)
        self.assertEqual(4, len(g.get_all_v()))

    def test_all_in_edges_of_node(self):
        g = DiGraph()
        for n in range(4):
            g.add_node(n)
        g.add_edge(0, 1, 1)
        g.add_edge(1, 0, 1.1)
        g.add_edge(1, 2, 1.3)
        g.add_edge(2, 3, 1.1)
        g.add_edge(1, 3, 1.9)

        self.assertEqual({0: 1}, g.all_in_edges_of_node(1))

    def test_all_out_edges_of_node(self):
        g = DiGraph()
        for n in range(4):
            g.add_node(n)
        g.add_edge(0, 1, 1)
        g.add_edge(1, 0, 1.1)
        g.add_edge(1, 2, 1.3)
        g.add_edge(2, 3, 1.1)
        g.add_edge(1, 3, 1.9)
        print(type(g.all_out_edges_of_node(1).keys()))
        self.assertEqual({0: 1.1, 2: 1.3, 3: 1.9}, g.all_out_edges_of_node(1))

    def test_get_mc(self):
        g = DiGraph()
        for n in range(4):
            g.add_node(n)
        g.add_edge(0, 1, 1)
        g.add_edge(1, 0, 1.1)
        g.add_edge(1, 2, 1.3)
        g.add_edge(2, 3, 1.1)
        g.add_edge(1, 3, 1.9)
        self.assertEqual(9, g.get_mc())
        g.remove_edge(1, 3)
        self.assertEqual(10, g.get_mc())

    def test_add_edge(self):
        g = DiGraph()
        for n in range(4):
            g.add_node(n)
        g.add_edge(0, 1, 1)
        self.assertEqual({1: 1}, g.edges[0])

    def test_add_node(self):
        g = DiGraph()
        for n in range(4):
            g.add_node(n, (1, 1, 2))
        self.assertEqual(4, g.v_size())

    def test_remove_node(self):
        g = DiGraph()
        for n in range(4):
            g.add_node(n)
        self.assertEqual(4, g.v_size())
        g.remove_node(1)
        self.assertEqual(3, g.v_size())

    def test_remove_edge(self):
        g = DiGraph()
        for n in range(4):
            g.add_node(n)
        g.add_edge(0, 1, 1)
        g.add_edge(1, 0, 1.1)
        g.add_edge(1, 2, 1.3)
        g.add_edge(2, 3, 1.1)
        g.add_edge(1, 3, 1.9)
        self.assertEqual({1: 1}, g.edges[0])
        g.remove_edge(0, 1)
        self.assertEqual({}, g.edges[0])
