class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

if __name__ == '__main__':

    g = Graph()

    #floor 0 (basement)
    g.add_vertex('A0')
    g.add_vertex('B0')
    g.add_vertex('C0')
    g.add_vertex('D0')
    g.add_vertex('E0')
    g.add_vertex('F0')

    #floor 0 connections
    g.add_edge('B', 'C', 0)
    g.add_edge('C', 'D', 0)
    g.add_edge('D', 'E', 0)
    g.add_edge('E', 'F', 0)
    g.add_edge('F', 'A', 0)
    g.add_edge('A', 'B', 0)

    #floor 1
    g.add_vertex('A1')
    g.add_vertex('B1')
    g.add_vertex('C1')
    g.add_vertex('D1')
    g.add_vertex('E1')
    g.add_vertex('F1')

    #floor 1 connections
    g.add_edge('B', 'C', 0)
    g.add_edge('C', 'D', 0)
    g.add_edge('D', 'E', 0)
    g.add_edge('E', 'F', 0)
    g.add_edge('F', 'A', 0)
    g.add_edge('A', 'B', 0)

    #floor 2
    g.add_vertex('A2')
    g.add_vertex('B2')
    g.add_vertex('C2')
    g.add_vertex('D2')
    g.add_vertex('E2')
    g.add_vertex('F2')

    #floor 2 connections
    g.add_edge('B', 'C', 0)
    g.add_edge('C', 'D', 0)
    g.add_edge('D', 'E', 0)
    g.add_edge('E', 'F', 0)
    g.add_edge('F', 'A', 0)
    g.add_edge('A', 'B', 0)

    #floor 3
    g.add_vertex('A3')
    g.add_vertex('B3')
    g.add_vertex('C3')
    g.add_vertex('D3')
    g.add_vertex('E3')
    g.add_vertex('F3')

    #floor 3 connections
    g.add_edge('B', 'C', 0)
    g.add_edge('C', 'D', 0)
    g.add_edge('D', 'E', 0)
    g.add_edge('E', 'F', 0)
    g.add_edge('F', 'A', 0)
    g.add_edge('A', 'B', 0)

    #floor 4
    g.add_vertex('A4')
    g.add_vertex('B4')
    g.add_vertex('C4')
    g.add_vertex('D4')
    g.add_vertex('E4')
    g.add_vertex('F4')

    #floor 4 connections
    g.add_edge('B', 'C', 0)
    g.add_edge('C', 'D', 0)
    g.add_edge('D', 'E', 0)
    g.add_edge('E', 'F', 0)
    g.add_edge('F', 'A', 0)
    g.add_edge('A', 'B', 0)

    #floor 5
    g.add_vertex('A5')
    g.add_vertex('B5')
    g.add_vertex('C5')
    g.add_vertex('D5')
    g.add_vertex('E5')
    g.add_vertex('F5')

    #floor 5 connections
    g.add_edge('B', 'C', 0)
    g.add_edge('C', 'D', 0)
    g.add_edge('D', 'E', 0)
    g.add_edge('E', 'F', 0)
    g.add_edge('F', 'A', 0)
    g.add_edge('A', 'B', 0)

    #floor 6
    g.add_vertex('A6')
    g.add_vertex('B6')
    g.add_vertex('C6')
    g.add_vertex('D6')
    g.add_vertex('E6')
    g.add_vertex('F6')

    #floor 6 connections
    g.add_edge('B', 'C', 0)
    g.add_edge('C', 'D', 0)
    g.add_edge('D', 'E', 0)
    g.add_edge('E', 'F', 0)
    g.add_edge('F', 'A', 0)
    g.add_edge('A', 'B', 0)

    #floor 7
    g.add_vertex('A7')
    g.add_vertex('B7')
    g.add_vertex('C7')
    g.add_vertex('D7')
    g.add_vertex('E7')
    g.add_vertex('F7')

    #floor 7 connections
    g.add_edge('B', 'C', 0)
    g.add_edge('C', 'D', 0)
    g.add_edge('D', 'E', 0)
    g.add_edge('E', 'F', 0)
    g.add_edge('F', 'A', 0)
    g.add_edge('A', 'B', 0)

    #floor 8 (to be added with 9th floor chorus room)



    #floor  connections
    g.add_edge('B', 'C', 0)
    g.add_edge('C', 'D', 0)
    g.add_edge('D', 'E', 0)
    g.add_edge('E', 'F', 0)
    g.add_edge('F', 'A', 0)
    g.add_edge('A', 'B', 0)


    for v in g:
        for w in v.get_connections():
            vid = v.get_id()
            wid = w.get_id()
            print '( %s , %s, %3d)'  % ( vid, wid, v.get_weight(w))

    for v in g:
        print 'g.vert_dict[%s]=%s' %(v.get_id(), g.vert_dict[v.get_id()])





'''
import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
G.add_edges_from(
    [('A', 'B'), ('A', 'C'), ('D', 'B'), ('E', 'C'), ('E', 'F'),
     ('B', 'H'), ('B', 'G'), ('B', 'F'), ('C', 'G')])

val_map = {'A': 1.0,
           'D': 0.5714285714285714,
           'H': 0.0}

values = [val_map.get(node, 0.25) for node in G.nodes()]

# Specify the edges you want here
red_edges = [('A', 'C'), ('E', 'C')]
edge_colours = ['black' if not edge in red_edges else 'red'
                for edge in G.edges()]
black_edges = [edge for edge in G.edges() if edge not in red_edges]

# Need to create a layout when doing
# separate calls to draw nodes and edges
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'),
                       node_color = values, node_size = 500)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos, edgelist=red_edges, edge_color='r', arrows=True)
nx.draw_networkx_edges(G, pos, edgelist=black_edges, arrows=False)
plt.show()
'''
