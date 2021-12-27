import json
import random
import sys
from typing import List
from src import GraphInterface
from src.DiGraph import DiGraph, Node
import matplotlib.pyplot as plt

from src.GraphAlgoInterface import GraphAlgoInterface


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph=DiGraph()):
        self.graph = graph

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        with open(file_name, "r") as f:
            dict = json.load(fp=f)
        for n in dict["Nodes"]:
            if "pos" in n:
                s = n["pos"]
                l = s.split(",")
                self.graph.add_node(int(n["id"]), (float(l[0]), float(l[1]), float(l[2])))
            else:
                s = None
                self.graph.add_node(int(n["id"]), s)
        for v in dict["Edges"]:
            self.graph.add_edge(v["src"], v["dest"], v["w"])
        return True

    def save_to_json(self, file_name: str) -> bool:
        toJson = {"Edges": [], "Nodes": []}
        for v in self.graph.nodes.keys():  # make random pos
            if not self.graph.nodes[v].pos:
                self.graph.nodes[v].pos = random.uniform(0, 100), random.uniform(0, 100), random.uniform(0, 100)
        for v in self.graph.nodes.keys():
            p = self.graph.nodes[v].pos
            pos = f'{p[0]},{p[1]},{p[2]}'
            toJson["Nodes"].append({"pos": pos, "id": self.graph.nodes[v].id})
            for u in self.graph.edges[self.graph.nodes[v].id]:
                toJson["Edges"].append(
                    {"src": self.graph.nodes[v].id, "w": self.graph.nodes[u].id, "dest": self.graph.edges[v][u]})

        with open(file_name + ".json", "w") as f:
            json.dump(toJson, fp=f, indent=2)
        return True

    def dijkstra(self, src):
        ng = self.graph
        self.maxValue(ng)
        ng.nodes[src].w = 0
        q = []
        for t in ng.nodes:
            q.append(ng.nodes[t])
        while len(q) != 0:
            x = self.listMin(q)
            q.remove(x)
            x = x.id
            for e in ng.all_out_edges_of_node(x):
                if ng.nodes[e].w > ng.nodes[x].w + ng.edges[x][e]:  # if des_weight > src_weight + edges_weight
                    ng.nodes[e].w = (ng.nodes[x].w + ng.edges[x][e])  # des_weight = src_weight + edges_weight
                    ng.nodes[e].tag = x  # des_tag = src

    def maxValue(self, ng: DiGraph):
        for t in ng.nodes:
            ng.nodes[t].tag = -1
            ng.nodes[t].w = sys.float_info.max

    def listMin(self, l: []) -> int:  # take the minimum from the list(and remove)
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
        path = []
        self.dijkstra(id1)
        path.append(id2)  # start from the last and add the 'father'
        x = id2
        distance = 0.0
        while x != id1:
            y = x
            x = self.graph.nodes[x].tag
            if x == -1:
                return float('inf'), []
            path.append(x)
            distance += self.graph.edges[x][y]
        path.reverse()  # reverse all (cus we started from the des)
        return distance, path

    # def copygraph(self, node_list: list, ng: DiGraph) -> DiGraph:
    #     for i in node_list:
    #         ng.add_node(i)
    #     for i in node_list:
    #         for e in self.graph.all_out_edges_of_node(i):
    #             ng.add_edge(i, e, self.graph.edges[i][e])
    #     return ng

    # def shortest_path_for_tsp(self, id1: int, id2: int, ng: DiGraph) -> (float, list):
    #     path = []
    #     self.dijkstra(id1, ng)
    #     path.append(id2)
    #     x = id2
    #     distance = 0.0
    #     while x != id1:
    #         y = x
    #         x = ng.nodes[x].tag
    #         if x == -1:
    #             return float('inf'), []
    #         path.append(x)
    #         distance += ng.edges[x][y]
    #     path.reverse()
    #     return distance, path

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        self.graph.add_node(-1)
        dis = sys.float_info.max
        ans = []
        for i in node_lst:
            l = self.tsp_rec(i, node_lst=node_lst, ans_lst=[], w=0.0, finaldes=sys.float_info.max, finalpath=[])
            if l[1] < dis:
                dis = l[1]
                ans = l[0]
        return ans, dis

    def tsp_rec(self, i: int, node_lst: List[int], ans_lst: List[int], w: float, finaldes, finalpath):
        if all(item in ans_lst for item in node_lst):
            finaldes = w
            finalpath.extend(ans_lst)
            ans_lst.clear()
            w = 0.0
            return finalpath, finaldes
        for n in self.graph.all_out_edges_of_node(i):

            if n in ans_lst:
                continue
            w += self.graph.edges[i][n]
            ans_lst.append(n)
            self.tsp_rec(n, node_lst, ans_lst, w, finaldes, finalpath)

        return finalpath, finaldes

        # # ng = DiGraph()
        # # ng = self.copygraph(node_lst, ng)
        # tempList2 = []
        # anslist = []
        # anslist2 = []
        # disans = sys.float_info.max
        # # s = node_lst.pop()
        # for i in node_lst:
        #     s = node_lst.index(i)
        #     node_lst2 = copy.deepcopy(node_lst)
        #     dis2 = 0
        #     while len(node_lst2) != 0:
        #         dis2 = 0
        #         t = False
        #         index = -1
        #         mini = sys.float_info.max
        #         for i in range(len(node_lst2)):
        #             l = self.shortest_path(s, node_lst2[i])
        #             tempList = l[1]
        #             dis = l[0]
        #             if dis == float('inf') and len(node_lst2) <=1:
        #                 break
        #             if dis < mini:
        #                 t = True
        #                 mini = dis
        #                 tempList2 = tempList
        #                 index = node_lst2[i]
        #         if t:
        #             dis2 += dis
        #             s = index
        #             node_lst2.remove(index)
        #             anslist.extend(tempList2)
        #         self.deleteDupes(anslist)
        #     if dis2 < disans:
        #         disans = dis2
        #         anslist2 = anslist
        #
        # return anslist2

    def deleteDupes(self, l: list):
        for i in range(len(l) - 2):
            if l[i] == l[i + 1]:
                l.pop(i)
        return l

    def centerPoint(self) -> (int, float):
        alld = sys.float_info.max
        ans = -1
        for i in self.graph.nodes:
            dista = 0  # max
            for j in self.graph.nodes:
                dis = self.shortest_path(self.graph.nodes[i].id, self.graph.nodes[j].id)
                tmpdis = dis[0]  # take the distance from "shortest_path"
                if tmpdis > dista:
                    dista = tmpdis
            if (dista < alld):
                ans = self.graph.nodes[i]
                alld = dista
        return alld, ans.id

    # def to_matrix(self):
    #     N = self.graph.v_size()
    #     inf = sys.float_info.max
    #     mat = [N][N]
    #
    #     # make all inf or 0
    #     for i in range(N):
    #         for j in range(N):
    #             mat[i][j] = inf
    #             if i == j:
    #                 mat[i][j] = 0
    #     for src, i in self.graph.edges.items():
    #         for dest, w in i.items():
    #             x = src

    def plot_graph(self) -> None:
        for v in self.graph.nodes.keys():
            if not self.graph.nodes[v].pos:
                self.graph.nodes[v].pos = random.uniform(0, 100), random.uniform(0, 100), random.uniform(0, 100)
        for v in self.graph.nodes.keys():
            x, y, z = self.graph.nodes[v].pos
            plt.plot(x, y, markersize=10, marker='.', color='pink')

            for u in self.graph.edges[self.graph.nodes[v].id]:
                his_x, his_y, his_z = self.graph.nodes[u].pos
                plt.annotate("", xy=(x, y), xytext=(his_x, his_y), arrowprops=dict(arrowstyle="<-"))
            plt.text(x, y, str(self.graph.nodes[v].id), color="blue", fontsize=10)

        plt.show()
