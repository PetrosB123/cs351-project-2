from typing import Optional, List
from graph_interfaces import IGraph, IVertex
from graph_impl import Graph, Vertex, Edge
from gbfs import GreedyBestFirstSearch
from dijkstra import Dijkstra
from A_Star import A_Star
from algorithm_interface import IAlgorithm

vertex_data = {}
def read_graph(file_path: str, file_path2: str) -> IGraph:  
    """Read the graph from the file and return the graph object"""
    with open(file_path) as f:
        with open(file_path2) as f2:
            graph = Graph()
            f.readline() # skip the first line (key line)
            f2.readline()
            for line in f:
                l = line.split(",")
                v1 = None
                v2 = None
                # Check if vertex is already made
                for vertex in graph.get_vertices():
                    if l[0] == vertex.get_name():
                        v1 = vertex 
                    if l[1] == vertex.get_name():
                        v2 = vertex
                
                # If vertex doesn't exist make it
                if v1 == None:
                    v1 = Vertex(l[0])
                    graph.add_vertex(v1)
                if v2 == None:
                    v2 = Vertex(l[1])
                    graph.add_vertex(v2)

                # Check if the 'weight' is convertable to a float
                try: float(l[3])
                except: raise TypeError(f"'{l[3]}' as a weight in the input file is not convertible to a float.")
                
                edge = Edge(l[2], v2, float(l[3]))
                v1.add_edge(edge)
                graph.add_edge(edge)
            
            # Store the vertices_v1.txt here
            for line in f2:
                l = line.split(",")
                vertex_data[l[0]] = [float(l[1]), float(l[2])]
    return graph


def main() -> None:
    graph: IGraph = read_graph("graph_v2.txt", "vertices_v1.txt")

    running = True
    algorithms: List[IAlgorithm] = [GreedyBestFirstSearch(), Dijkstra(), A_Star()]

    while running:
        start_vertex_name: str  = input("Enter the start vertex name: ")
        goal_vertex_name: str  = input("Enter the goal vertex name: ")
        start_name = False
        goal_name = False

        # Make sure input is actually valid vertices
        for vertex in graph.get_vertices():
            if vertex.get_name() == start_vertex_name:
                start_name = True
            if vertex.get_name() == goal_vertex_name:
                goal_name = True
            if start_name and goal_name: break;
        
        if not (start_name and goal_name):
            raise ValueError("Must input a valid vertex name")


        # run the input for all three algorithms and print them out
        for algorithm in algorithms:
            results = algorithm.find_path(graph, start_vertex_name, goal_vertex_name, vertex_data) # type: ignore
            print("\n")
            print(f"{algorithm.get_name()}:")
            print(results.textual_directions)
            print(f"Distance: {results.total_distance}")
            print(f"Time Taken: {results.execution_time}")
            print(f"Edges Evaluated: {results.edges_evaluated}")
            print(f"Vertices Explored: {results.vertices_explored}")

        if input("Run algorithms again?").lower() in ["n", "no"]:
            running = False


    


if __name__ == "__main__":
    main()