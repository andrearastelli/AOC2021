from collections import defaultdict

class Graph:

    def __init__(self, graph_dict=None):
        if graph_dict is None:
            graph_dict = defaultdict(set)

        self.graph_dict = graph_dict

    def edges(self, vertice):
        return self.graph_dict[vertice]

    def all_vertices(self):
        return set(self.graph_dict.keys())

    def all_edges(self):
        return self.generate_edges()

    def add_vertex(self, vertex):
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = []

    def add_edge(self, edge):
        edge = set(edge)
        vertex1, vertex2 = tuple(edge)
        for x, y in [(vertex1, vertex2), (vertex2, vertex1)]:
            if x in self.graph_dict:
                self.graph_dict[x].add(y)
            else:
                self.graph_dict[x] = {y}

    def generate_edges(self):
        edges = []
        for vertex in self.graph_dict:
            for neighbour in self.graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})

        return edges

    def find_path(self, start, end, path=None):
        if path is None:
            path = []

        graph = self.graph_dict
        path = path + [start]

        if start == end:
            return path

        if start not in graph:
            return None

        for vertex in graph[start]:
            if vertex not in path:
                extended_path = self.find_path(vertex, end, path)
                if extended_path:
                    return extended_path

        return None

    def find_all_paths(self, start, end, path=None):
        if path is None:
            path = []

        graph = self.graph_dict
        path = path + [start]

        if start == end:
            return [path]

        if start not in graph:
            return []

        paths = []
        for vertex in graph[start]:
            if vertex not in path:
                extended_paths = self.find_all_paths(vertex, end, path)
                paths.extend(extended_paths)

        return paths

    def __iter__(self):
        self.iter_obj = iter(self.graph_dict)
        return self.iter_obj

    def __next__(self):
        return next(self.iter_obj)

    def __str__(self):
        res = f"Vertices: {' '.join(self.graph_dict.keys())}"
        res += f"\nEdges: {' '.join(map(str, self.generate_edges()))}"
        return res