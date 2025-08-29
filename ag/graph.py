class Graph:
    def __init__(self):
        self.map = dict()
        self.nodes = []
        self.starting_node = None
        self.final_node = None

    def insert_path(self, origin, destination, cost):
        if origin not in self.map:
            self.map[origin] = {}
            self.nodes.append(origin)
        if destination not in self.map:
            self.nodes.append(destination)
            self.map[destination] = {}
        self.map[origin][destination] = cost 
        self.map[destination][origin] = cost
    
    def valid_path(self, path):
        if len(path) <= 1:
            return True
        # recorre pares consecutivos (u, v)
        marked = {}
        for u, v in zip(path, path[1:]):
            if v not in self.get_neighbours(u):  # si no hay arista u-v
                return False
            if u in marked and u != self.starting_node:
                return False
            else:
                marked.add(u)

        return True
    
    def get_neighbours(self, node):
        return list(self.map.get(node, {}).keys())
    
    def is_neighbour(self, node1, node2):
        return node1 in self.get_neighbours(node2)