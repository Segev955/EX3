from unittest import TestCase
import os.path

from src.GraphAlgo import GraphAlgo


class TestGraphAlgo(TestCase):
    g = GraphAlgo()
    g.load_from_json("../data/G1.json")

    def test_get_graph(self):
        g = GraphAlgo()
        g.graph.add_node(0)
        self.assertEqual(g.get_graph(), g.graph)

    def test_load_from_json(self):
        g = GraphAlgo()
        g.load_from_json("../data/G1.json")
        self.assertEqual(17, g.graph.v_size())

    def test_save_to_json(self):
        g = GraphAlgo()
        g.load_from_json("../data/G1.json")
        g.save_to_json("newG1")
        self.assertTrue(True, os.path.isfile("newG1.json"))

    def test_shortest_path(self):
        g = GraphAlgo()
        g.load_from_json("../data/G1.json")
        ans = g.shortest_path(1, 5)
        self.assertEqual(5.091901160431474, ans[0])
        self.assertEqual([1, 2, 6, 5], ans[1])

    def test_tsp(self):
        print("tsp")

    def test_center_point(self):
        g = GraphAlgo()
        g.load_from_json("../data/G1.json")
        self.assertEqual(8, g.centerPoint()[1])
        self.assertEqual(9.925289024973141, g.centerPoint()[0])

    def test_plot_graph(self):
        g = GraphAlgo()
        g.load_from_json("../data/G1.json")
        g.plot_graph()
