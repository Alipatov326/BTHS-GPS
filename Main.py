import heapq
import tkinter as tk
from tkinter import ttk



# graph structure classes used for creating node map of the school
# functions and documentation found on geeksforgeeks.org
class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}

    def __str__(self):
        return str(self.id) + " adjacent: " + str([x.id for x in self.adjacent])

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

    def add_edge(self, frm, to, cost=0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

# uses dijkstra's algorithm to find the shortest path between two nodes in the graph
def shortest_distance(graph, start, end):
    # Check if start and end nodes exist
    if start not in graph.vert_dict or end not in graph.vert_dict:
        print("Invalid start or end node.")
        return None

    distances = {vertex: float("inf") for vertex in graph.vert_dict}
    previous = {vertex: None for vertex in graph.vert_dict}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_distance, current_vertex = heapq.heappop(queue)

        if current_vertex == end:
            break

        for neighbor in graph.vert_dict[current_vertex].get_connections():
            neighbor_id = neighbor.get_id()
            weight = graph.vert_dict[current_vertex].get_weight(neighbor)
            distance = current_distance + weight

            if distance < distances[neighbor_id]:
                distances[neighbor_id] = distance
                previous[neighbor_id] = current_vertex
                heapq.heappush(queue, (distance, neighbor_id))

    path = []
    current = end
    while current:
        path.insert(0, current)
        current = previous[current]
    if distances[end] == float("inf"):
        print("No path found.")
        return None
    return distances[end], path

# converts the path found by dijkstra's algorithm into human readable instructions
def path_to_instructions(path):
    import re
    if not path or len(path) < 2:
        return "No movement needed."
    steps = []
    i = 1
    while i < len(path):
        prev = path[i - 1]
        prev_letter, prev_floor = re.match(r"([A-F])(\d+)", prev).groups()
        curr = path[i]
        curr_letter, curr_floor = re.match(r"([A-F])(\d+)", curr).groups()
        if prev_letter == curr_letter and prev_floor != curr_floor:
            direction = "up" if int(curr_floor) > int(prev_floor) else "down"
            start_floor = int(prev_floor)
            end_floor = int(curr_floor)
            j = i
            while (
                j + 1 < len(path)
                and re.match(r"([A-F])(\d+)", path[j + 1]).groups()[0] == curr_letter
                and (
                    (direction == "up" and int(re.match(r"([A-F])(\d+)", path[j + 1]).groups()[1]) > int(re.match(r"([A-F])(\d+)", path[j]).groups()[1]))
                    or (direction == "down" and int(re.match(r"([A-F])(\d+)", path[j + 1]).groups()[1]) < int(re.match(r"([A-F])(\d+)", path[j]).groups()[1]))
                )
            ):
                end_floor = int(re.match(r"([A-F])(\d+)", path[j + 1]).groups()[1])
                j += 1
            step = f"Go {direction} to floor {end_floor} at stairwell {curr_letter}."
            steps.append((i, j, step))
            i = j + 1
        else:
            if prev_letter != curr_letter and prev_floor == curr_floor:
                step = f"Go to stairwell {curr_letter} on floor {curr_floor}."
            elif prev_letter != curr_letter and prev_floor != curr_floor:
                direction = "up" if int(curr_floor) > int(prev_floor) else "down"
                step = f"Go to stairwell {curr_letter} and {direction} to floor {curr_floor}."
            else:
                step = None
            if step:
                steps.append((i, i, step))
            i += 1
    if not steps:
        return "No movement needed."
    instructions = []
    if len(steps) == 1:
        instructions.append(steps[0][2])
    else:
        for idx, (start, end, step) in enumerate(steps):
            if idx == 0:
                instructions.append(f"First, {step}")
            elif idx == len(steps) - 1:
                instructions.append(f"Finally, {step}")
            else:
                instructions.append(f"Then, {step}")
    return "\n".join(instructions)

# function to find the path based on user input
def find_path():
    start = f"{start_dir.get()}{start_floor.get()}"
    end = f"{end_dir.get()}{end_floor.get()}"
    result = shortest_distance(g, start, end)
    if result is None:
        result_label.config(text="No path found or invalid nodes.")
    else:
        distance, path = result
        instructions = path_to_instructions(path)
        result_label.config(
            text=f"Shortest distance: {distance}\nInstructions:\n{instructions}"
        )

# main function to create the graph and edges of the school
if __name__ == "__main__":

    g = Graph()

    # floor 0 (basement)
    g.add_vertex("A0")
    g.add_vertex("B0")
    g.add_vertex("D0")
    g.add_vertex("E0")
    g.add_vertex("F0")

    # floor 0 connections
    g.add_edge("D0", "E0", 39)
    g.add_edge("E0", "F0", 43)
    g.add_edge("F0", "A0", 58)
    g.add_edge("A0", "B0", 40)

    # floor 1
    g.add_vertex("A1")
    g.add_vertex("B1")
    g.add_vertex("C1")
    g.add_vertex("D1")
    g.add_vertex("E1")
    g.add_vertex("F1")

    # floor 1 connections
    g.add_edge("B1", "C1", 50)
    g.add_edge("C1", "D1", 53)
    g.add_edge("D1", "E1", 39)
    g.add_edge("E1", "F1", 53)
    g.add_edge("F1", "A1", 58)
    g.add_edge("A1", "B1", 40)
    g.add_edge("C1", "F1", 39)

    # floor 2
    g.add_vertex("A2")
    g.add_vertex("B2")
    g.add_vertex("C2")
    g.add_vertex("D2")
    g.add_vertex("E2")
    g.add_vertex("F2")

    # floor 2 connections
    g.add_edge("B2", "C2", 50)
    g.add_edge("C2", "D2", 53)
    g.add_edge("D2", "E2", 39)
    g.add_edge("E2", "F2", 53)
    g.add_edge("F2", "A2", 58)
    g.add_edge("A2", "B2", 40)
    g.add_edge("C2", "F2", 39)

    # floor 3
    g.add_vertex("A3")
    g.add_vertex("B3")
    g.add_vertex("C3")
    g.add_vertex("D3")
    g.add_vertex("E3")
    g.add_vertex("F3")

    # floor 3 connections
    g.add_edge("B3", "C3", 50)
    g.add_edge("C3", "D3", 53)
    g.add_edge("D3", "E3", 39)
    g.add_edge("E3", "F3", 53)
    g.add_edge("F3", "A3", 58)
    g.add_edge("A3", "B3", 40)
    g.add_edge("C3", "F3", 39)

    # floor 4
    g.add_vertex("A4")
    g.add_vertex("B4")
    g.add_vertex("C4")
    g.add_vertex("D4")
    g.add_vertex("E4")
    g.add_vertex("F4")

    # floor 4 connections
    g.add_edge("B4", "C4", 50)
    g.add_edge("C4", "D4", 53)
    g.add_edge("D4", "E4", 39)
    g.add_edge("E4", "F4", 53)
    g.add_edge("F4", "A4", 58)
    g.add_edge("A4", "B4", 40)
    g.add_edge("C4", "F4", 39)

    # floor 5
    g.add_vertex("A5")
    g.add_vertex("B5")
    g.add_vertex("C5")
    g.add_vertex("D5")
    g.add_vertex("E5")
    g.add_vertex("F5")

    # floor 5 connections
    g.add_edge("B5", "C5", 50)
    g.add_edge("C5", "D5", 53)
    g.add_edge("D5", "E5", 39)
    g.add_edge("E5", "F5", 53)
    g.add_edge("F5", "A5", 58)
    g.add_edge("A5", "B5", 40)

    # floor 6
    g.add_vertex("A6")
    g.add_vertex("B6")
    g.add_vertex("C6")
    g.add_vertex("D6")
    g.add_vertex("E6")
    g.add_vertex("F6")

    # floor 6 connections
    g.add_edge("B6", "C6", 50)
    g.add_edge("C6", "D6", 53)
    g.add_edge("D6", "E6", 39)
    g.add_edge("E6", "F6", 53)
    g.add_edge("F6", "A6", 58)
    g.add_edge("A6", "B6", 40)
    g.add_edge("C6", "F6", 39)

    # floor 7
    g.add_vertex("A7")
    g.add_vertex("B7")
    g.add_vertex("C7")
    g.add_vertex("D7")
    g.add_vertex("E7")
    g.add_vertex("F7")

    # floor 7 connections
    g.add_edge("B7", "C7", 50)
    g.add_edge("C7", "D7", 53)
    g.add_edge("D7", "E7", 39)
    g.add_edge("E7", "F7", 53)
    g.add_edge("F7", "A7", 58)
    g.add_edge("A7", "B7", 40)
    g.add_edge("C7", "F7", 39)

    # floor 8

    g.add_vertex("C8")
    g.add_vertex("F8")

    # floor 8 connections
    g.add_edge("C7", "C8", 12)
    g.add_edge("F7", "F8", 12)
    g.add_edge("C8", "F8", 39)

    # stairs (change length later)

    # A stairs
    g.add_edge("A0", "A1", 12)
    g.add_edge("A1", "A2", 12)
    g.add_edge("A2", "A3", 12)
    g.add_edge("A3", "A4", 12)
    g.add_edge("A4", "A5", 12)
    g.add_edge("A5", "A6", 12)
    g.add_edge("A6", "A7", 12)

    # B stairs
    g.add_edge("B0", "B1", 12)
    g.add_edge("B1", "B2", 12)
    g.add_edge("B2", "B3", 12)
    g.add_edge("B3", "B4", 12)
    g.add_edge("B4", "B5", 12)
    g.add_edge("B5", "B6", 12)
    g.add_edge("B6", "B7", 12)

    # C stairs
    g.add_edge("C1", "C2", 12)
    g.add_edge("C2", "C3", 12)
    g.add_edge("C3", "C4", 12)
    g.add_edge("C4", "C5", 12)
    g.add_edge("C5", "C6", 12)

    # D stairs
    g.add_edge("D0", "D1", 12)
    g.add_edge("D1", "D2", 12)
    g.add_edge("D2", "D3", 12)
    g.add_edge("D3", "D4", 12)
    g.add_edge("D4", "D5", 12)
    g.add_edge("D5", "D6", 12)
    g.add_edge("D6", "D7", 12)

    # E stairs
    g.add_edge("E0", "E1", 12)
    g.add_edge("E1", "E2", 12)
    g.add_edge("E2", "E3", 12)
    g.add_edge("E3", "E4", 12)
    g.add_edge("E4", "E5", 12)
    g.add_edge("E5", "E6", 12)
    g.add_edge("E6", "E7", 12)

    # F stairs
    g.add_edge("F0", "F1", 12)
    g.add_edge("F1", "F2", 12)
    g.add_edge("F2", "F3", 12)
    g.add_edge("F3", "F4", 12)
    g.add_edge("F4", "F5", 12)
    g.add_edge("F5", "F6", 12)

    # Elevators (distance tbd)

    # student ones

    # floor 8 (to be added with 9th floor chorus room)

    for v in g:
        for w in v.get_connections():
            vid = v.get_id()
            wid = w.get_id()
            print("( %s , %s, %3d)" % (vid, wid, v.get_weight(w)))

    for v in g:
        print("g.vert_dict[%s]=%s" % (v.get_id(), g.vert_dict[v.get_id()]))



# using tkinter to create a UI
root = tk.Tk()
root.title("Path Finder")
root.minsize(350, 260)

font = ("Segoe UI", 14)

floors = [str(i) for i in range(9)]
dirs = [chr(ord("A") + i) for i in range(6)]

ttk.Label(root, text="Starting Floor:", font=font).grid(row=0, column=0, padx=10, pady=10, sticky="e")
start_floor = ttk.Combobox(root, values=floors, state="readonly", font=font, width=5)
start_floor.grid(row=0, column=1, padx=10, pady=10)
start_floor.current(0)

ttk.Label(root, text="Starting Direction:", font=font).grid(row=1, column=0, padx=10, pady=10, sticky="e")
start_dir = ttk.Combobox(root, values=dirs, state="readonly", font=font, width=5)
start_dir.grid(row=1, column=1, padx=10, pady=10)
start_dir.current(0)

ttk.Label(root, text="Ending Floor:", font=font).grid(row=2, column=0, padx=10, pady=10, sticky="e")
end_floor = ttk.Combobox(root, values=floors, state="readonly", font=font, width=5)
end_floor.grid(row=2, column=1, padx=10, pady=10)
end_floor.current(0)

ttk.Label(root, text="Ending Direction:", font=font).grid(row=3, column=0, padx=10, pady=10, sticky="e")
end_dir = ttk.Combobox(root, values=dirs, state="readonly", font=font, width=5)
end_dir.grid(row=3, column=1, padx=10, pady=10)
end_dir.current(0)

find_btn = ttk.Button(root, text="Find Path", command=find_path, style="Big.TButton")
find_btn.grid(row=4, column=0, columnspan=2, pady=10)

result_label = ttk.Label(root, text="", font=font, wraplength=320, justify="left")
result_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

style = ttk.Style()
style.configure("Big.TButton", font=font)

root.mainloop()


