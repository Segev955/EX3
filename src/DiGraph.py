class Node:
    def __init__(self, id, pos):
        self.id = id
        self.pos = pos

    def __repr__(self) -> str:
        return f"pos={self.pos} id={self.id}"


class DiGraph:
    def __init__(self, nodes={}, edges={}, edgesOut={}, mc=0):
        self.nodes = nodes
        self.edges = edges
        self.edgesOut = edgesOut
        self.mc = mc

    def v_size(self) -> int:
        return len(self.nodes)

    def e_size(self) -> int:
        return len(self.edges)

    def get_all_v(self) -> dict:
        return self.nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        return self.edgesOut[id1]

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.edges[id1]

    def get_mc(self) -> int:
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if not self.edges.get(id1) and not self.edgesOut.get(id2):
            pass
        if id1 in self.nodes and id2 in self.nodes:
            self.edges[id1][id2] = weight
            self.edgesOut[id2][id1] = weight
            self.mc+=1
            return True
        return False

    def add_node(self, node_id: int, pos: tuple = (0, 0)) -> bool:
        if node_id in self.nodes:
            pass
        else:
            self.nodes[node_id] = Node(node_id, pos)
            self.edges[node_id] = {}
            self.edgesOut[node_id] = {}
            self.mc += 1
            return True
        return False

    def remove_node(self, node_id: int) -> bool:
        if node_id not in self.nodes:
            pass
        else:
            self.nodes.pop(node_id)
            self.mc += 1
            return True
        return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if not self.edges.get(node_id1) and not self.edgesOut.get(node_id2):
            pass
        else:
            self.edges[node_id1][node_id2] = None
            self.edgesOut[node_id2][node_id1] = None
            self.mc += 1
            return True
        return False

    def __repr__(self) -> str:
        return f"nodes={self.nodes}\n edges={self.edges}"