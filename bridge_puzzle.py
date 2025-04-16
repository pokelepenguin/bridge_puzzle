import networkx as nx
import matplotlib.pyplot as plt


# Step 1: Create a graph
def create_graph():
    G = nx.Graph()
    print("Interactive Königsberg Bridge Problem")
    print("Enter vertices (e.g., A, B, C, D). Type 'done' to finish:")

    # Add vertices
    while True:
        vertex = input("Vertex: ").strip()
        if vertex.lower() == 'done':
            break
        G.add_node(vertex)

    print("Enter edges in format 'A B' to connect vertices. Type 'done' to finish:")

    # Add edges
    while True:
        edge = input("Edge (e.g., A B): ").strip()
        if edge.lower() == 'done':
            break
        try:
            v1, v2 = edge.split()
            G.add_edge(v1, v2)
        except ValueError:
            print("Invalid format. Try again!")

    return G


# Step 2: Check Eulerian Path/Circuit
def analyze_graph(graph):
    # Check degrees
    odd_degree_nodes = [node for node in graph.nodes if len(graph[node]) % 2 != 0]
    print("\nAnalysis:")
    print(f"Vertices with odd degree: {odd_degree_nodes}")

    # Determine Eulerian path or circuit
    if nx.is_connected(graph):
        if len(odd_degree_nodes) == 0:
            print("This graph has an Eulerian Circuit (all vertices have even degrees).")
        elif len(odd_degree_nodes) == 2:
            print("This graph has an Eulerian Path (exactly 2 vertices have odd degrees).")
        else:
            print("This graph does not have an Eulerian Path or Circuit.")
    else:
        print("This graph is disconnected and cannot have an Eulerian Path or Circuit.")


# Step 3: Visualize the Graph
def display_graph(graph):
    plt.figure(figsize=(8, 6))
    nx.draw(graph, with_labels=True, node_color="lightblue", edge_color="gray", font_weight="bold")
    plt.show()


# Step 4: Run the Demo
def interactive_demo():
    graph = create_graph()
    display_graph(graph)
    analyze_graph(graph)


interactive_demo()