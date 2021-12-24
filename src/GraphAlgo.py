import json
import queue
import sys
from typing import List
from src import GraphInterface
from src.DiGraph import DiGraph, Node


class GraphAlgo:

    def __init__(self, graph: DiGraph):
        self.graph = graph

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        # dict = {}
        with open(file_name, "r") as f:
            dict = json.load(fp=f)
        for n in dict["Nodes"]:
            s = n["pos"]
            l = s.split(",")
            self.graph.add_node(int(n["id"]), (l[0], l[1], l[2]))
        for v in dict["Edges"]:
            self.graph.add_edge(v["src"], v["dest"], v["w"])
        return True

    def save_to_json(self, file_name: str) -> bool:
        with open(file_name, "w") as f:
            json.dump(self, fp=f, indent=1, default=lambda x: x.__dict__)
        return True

    def dijkstra(self, src):
        self.maxValue()
        self.graph.nodes[src].w = 0
        q = []
        for t in self.graph.nodes:
            q.append(self.graph.nodes[t])
        while len(q) != 0:
            x = self.listMin(q)
            q.remove(x)
            x = x.id
            for e in self.graph.all_out_edges_of_node(x):
                print(self.graph.edges[x][e])
                if self.graph.nodes[e].w > self.graph.nodes[x].w + self.graph.edges[x][e]:  # if des_weight > src_weight + edges_weight
                    self.graph.nodes[e].w = (self.graph.nodes[x].w + self.graph.edges[x][e])  # des_weight = src_weight + edges_weight
                    self.graph.nodes[e].tag = x  # des_tag = src

    def maxValue(self):
        for t in self.graph.nodes:
            self.graph.nodes[t].tag = -1
            self.graph.nodes[t].w = sys.float_info.max

    def listMin(self, l: []) -> int:
        templist = []
        n = l.pop()
        templist.append(n)
        min = n.w
        key = n
        while len(l) != 0:
            n = l.pop()
            templist.append(n)
            if n.w < min:
                min = n.w
                key = n
        while len(templist) != 0:
            l.append(templist.pop())
        return key

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
        Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
        @param id1: The start node id
        @param id2: The end node id
        @return: The distance of the path, a list of the nodes ids that the path goes through
        Example:
    #      >>> from GraphAlgo import GraphAlgo
    #       >>> g_algo = GraphAlgo()
    #        >>> g_algo.addNode(0)
    #        >>> g_algo.addNode(1)
    #        >>> g_algo.addNode(2)
    #        >>> g_algo.addEdge(0,1,1)
    #        >>> g_algo.addEdge(1,2,4)
    #        >>> g_algo.shortestPath(0,1)
    #        (1, [0, 1])
    #        >>> g_algo.shortestPath(0,2)
    #        (5, [0, 1, 2])
        Notes:
        If there is no path between id1 and id2, or one of them dose not exist the function returns (float('inf'),[])
        More info:
        https://en.wikipedia.org/wiki/Dijkstra's_algorithm
        """

        path = []
        self.dijkstra(id1)
        path.append(id2)
        x = id2
        distance = 0.0
        while x != id1:
            y = x
            x = self.graph.nodes[x].tag
            if x == -1:
                return float('inf'), []
            path.append(x)
            distance += self.graph.edges[x][y]
        path.reverse()
        return distance, path

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        """
        Finds the shortest path that visits all the nodes in the list
        :param node_lst: A list of nodes id's
        :return: A list of the nodes id's in the path, and the overall distance
        """
        tempList = []
        s = node_lst.pop()
        while len(node_lst) != 0:
            for i in node_lst:
                tempList = self.shortest_path(s, node_lst[i])

    def centerPoint(self) -> (int, float):
        """
        Finds the node that has the shortest distance to it's farthest node.
        :return: The nodes id, min-maximum distance
        """

    def plot_graph(self) -> None:
        """
        Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner.
        @return: None
        """
        raise NotImplementedError
