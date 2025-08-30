class Graph:
    def __init__(self):
        self.map = dict()
        self.nodes = []
        self.starting_node = None
        self.final_node = None

    def insert_path(self, origin, destination, cost):
        if origin not in self.nodes:
            self.nodes.append(origin)
        if destination not in self.nodes:
            self.nodes.append(destination)
        self.map[(origin, destination)] = cost 
        self.map[(destination, origin)] = cost
    
    def valid_path(self, path):
        length = len(path)
        if length != len(self.nodes) + 1:
            print(self.nodes)
            return False
        marked = set()
        starting_node_appareances = 0
        for i in range(length - 1):
            u = path[i]
            v = path[i + 1]
            if u == self.starting_node:
                starting_node_appareances += 1
                if starting_node_appareances > 2:
                    return False
            if not self.is_neighbour(u, v):
                return False
            if u in marked and u != self.starting_node:
                return False
            else:
                marked.add(u)
        return True
    
    def is_neighbour(self, node1, node2):
        return (node1, node2) in self.map
    
    def calculate_cost(self, path):
        cost = 0
        for i in range(len(path) - 1):
            cost += self.map[(path[i], path[i + 1])]
        return cost