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

# School mapped out with nodes
    g = Graph()

    #floor 0 (basement)
    g.add_vertex('A0')
    g.add_vertex('B0')
    g.add_vertex('D0')
    g.add_vertex('E0')
    g.add_vertex('F0')

    #floor 0 connections
    g.add_edge('D0', 'E0', 39)
    g.add_edge('E0', 'F0', 43)
    g.add_edge('F0', 'A0', 58)
    g.add_edge('A0', 'B0', 40)

    #floor 1
    g.add_vertex('A1')
    g.add_vertex('B1')
    g.add_vertex('C1')
    g.add_vertex('D1')
    g.add_vertex('E1')
    g.add_vertex('F1')

    #floor 1 connections
    g.add_edge('B1', 'C1', 50)
    g.add_edge('C1', 'D1', 53)
    g.add_edge('D1', 'E1', 39)
    g.add_edge('E1', 'F1', 53)
    g.add_edge('F1', 'A1', 58)
    g.add_edge('A1', 'B1', 40)
    g.add_edge('C1', 'F1', 39)

    #floor 2
    g.add_vertex('A2')
    g.add_vertex('B2')
    g.add_vertex('C2')
    g.add_vertex('D2')
    g.add_vertex('E2')
    g.add_vertex('F2')

    #floor 2 connections
    g.add_edge('B2', 'C2', 50)
    g.add_edge('C2', 'D2', 53)
    g.add_edge('D2', 'E2', 39)
    g.add_edge('E2', 'F2', 53)
    g.add_edge('F2', 'A2', 58)
    g.add_edge('A2', 'B2', 40)
    g.add_edge('C2', 'F2', 39)

    #floor 3
    g.add_vertex('A3')
    g.add_vertex('B3')
    g.add_vertex('C3')
    g.add_vertex('D3')
    g.add_vertex('E3')
    g.add_vertex('F3')

    #floor 3 connections
    g.add_edge('B3', 'C3', 50)
    g.add_edge('C3', 'D3', 53)
    g.add_edge('D3', 'E3', 39)
    g.add_edge('E3', 'F3', 53)
    g.add_edge('F3', 'A3', 58)
    g.add_edge('A3', 'B3', 40)
    g.add_edge('C3', 'F3', 39)

    #floor 4
    g.add_vertex('A4')
    g.add_vertex('B4')
    g.add_vertex('C4')
    g.add_vertex('D4')
    g.add_vertex('E4')
    g.add_vertex('F4')

    #floor 4 connections
    g.add_edge('B4', 'C4', 50)
    g.add_edge('C4', 'D4', 53)
    g.add_edge('D4', 'E4', 39)
    g.add_edge('E4', 'F4', 53)
    g.add_edge('F4', 'A4', 58)
    g.add_edge('A4', 'B4', 40)
    g.add_edge('C4', 'F4', 39)

    #floor 5
    g.add_vertex('A5')
    g.add_vertex('B5')
    g.add_vertex('C5')
    g.add_vertex('D5')
    g.add_vertex('E5')
    g.add_vertex('F5')

    #floor 5 connections
    g.add_edge('B5', 'C5', 50)
    g.add_edge('C5', 'D5', 53)
    g.add_edge('D5', 'E5', 39)
    g.add_edge('E5', 'F5', 53)
    g.add_edge('F5', 'A5', 58)
    g.add_edge('A5', 'B5', 40)

    #floor 6
    g.add_vertex('A6')
    g.add_vertex('B6')
    g.add_vertex('C6')
    g.add_vertex('D6')
    g.add_vertex('E6')
    g.add_vertex('F6')

    #floor 6 connections
    g.add_edge('B6', 'C6', 50)
    g.add_edge('C6', 'D6', 53)
    g.add_edge('D6', 'E6', 39)
    g.add_edge('E6', 'F6', 53)
    g.add_edge('F6', 'A6', 58)
    g.add_edge('A6', 'B6', 40)
    g.add_edge('C6', 'F6', 39)

    #floor 7
    g.add_vertex('A7')
    g.add_vertex('B7')
    g.add_vertex('C7')
    g.add_vertex('D7')
    g.add_vertex('E7')
    g.add_vertex('F7')

    #floor 7 connections
    g.add_edge('B7', 'C7', 50)
    g.add_edge('C7', 'D7', 53)
    g.add_edge('D7', 'E7', 39)
    g.add_edge('E7', 'F7', 53)
    g.add_edge('F7', 'A7', 58)
    g.add_edge('A7', 'B7', 40)
    g.add_edge('C7', 'F7', 39)

    #floor 8

    g.add_vertex('C8')
    g.add_vertex('F8')

    #floor 8 connections
    g.add_edge('C7', 'C8', 12)
    g.add_edge('F7', 'F8', 12)
    g.add_edge('C8', 'F8', 39)

    #stairs (change length later)

    #A stairs
    g.add_edge('A0', 'A1', 12)
    g.add_edge('A1', 'A2', 12)
    g.add_edge('A2', 'A3', 12)
    g.add_edge('A3', 'A4', 12)
    g.add_edge('A4', 'A5', 12)
    g.add_edge('A5', 'A6', 12)
    g.add_edge('A6', 'A7', 12)
    
    #B stairs
    g.add_edge('B0', 'B1', 12)
    g.add_edge('B1', 'B2', 12)
    g.add_edge('B2', 'B3', 12)
    g.add_edge('B3', 'B4', 12)
    g.add_edge('B4', 'B5', 12)
    g.add_edge('B5', 'B6', 12)
    g.add_edge('B6', 'B7', 12)

    #C stairs
    g.add_edge('C1', 'C2', 12)
    g.add_edge('C2', 'C3', 12)
    g.add_edge('C3', 'C4', 12)
    g.add_edge('C4', 'C5', 12)
    g.add_edge('C5', 'C6', 12)

    #D stairs
    g.add_edge('D0', 'D1', 12)
    g.add_edge('D1', 'D2', 12)
    g.add_edge('D2', 'D3', 12)
    g.add_edge('D3', 'D4', 12)
    g.add_edge('D4', 'D5', 12)
    g.add_edge('D5', 'D6', 12)
    g.add_edge('D6', 'D7', 12)

    #E stairs
    g.add_edge('E0', 'E1', 12)
    g.add_edge('E1', 'E2', 12)
    g.add_edge('E2', 'E3', 12)
    g.add_edge('E3', 'E4', 12)
    g.add_edge('E4', 'E5', 12)
    g.add_edge('E5', 'E6', 12)
    g.add_edge('E6', 'E7', 12)

    #F stairs
    g.add_edge('F0', 'F1', 12)
    g.add_edge('F1', 'F2', 12)
    g.add_edge('F2', 'F3', 12)
    g.add_edge('F3', 'F4', 12)
    g.add_edge('F4', 'F5', 12)
    g.add_edge('F5', 'F6', 12)

    #Elevators (distance tbd)

    #student ones

    

    #floor 8 (to be added with 9th floor chorus room)


    for v in g:
        for w in v.get_connections():
            vid = v.get_id()
            wid = w.get_id()
            print ('( %s , %s, %3d)'  % ( vid, wid, v.get_weight(w)))

    for v in g:
        print ('g.vert_dict[%s]=%s' %(v.get_id(), g.vert_dict[v.get_id()]))





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
