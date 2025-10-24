from algorithm_interface import IAlgorithm
from AlgorithmResult import AlgorithmResult
from graph_interfaces import IGraph, IVertex, IEdge
import time
from PriorityQueue import PriorityQueue
from typing import List

class GreedyBestFirstSearch(IAlgorithm):
    def __init__(self):
        self._name: str = "Greedy Best First Search"
    
    def find_path(
        self,
        graph: IGraph,
        start_vertex_name: str,
        destination_vertex_name: str,
        vertex_data: dict
    ) -> AlgorithmResult:
        
        start_time = time.time()
        vertices_explored = 0
        edges_evaluated = 0
        queue = PriorityQueue()
        explored: List[IVertex] = []
        distance = 0

        for vertex in graph.get_vertices():
            if vertex.get_name() == start_vertex_name:
                queue.add(vertex, abs(vertex_data[vertex.get_name()][0] - vertex_data[destination_vertex_name][0]) + abs(vertex_data[vertex.get_name()][1] - vertex_data[destination_vertex_name][1]))
                
        def evaluate_path(finished: bool) -> AlgorithmResult:
                execution_time = time.time() - start_time
                directions = f" -> ".join(item.get_name() for item in explored)
                return AlgorithmResult(directions, distance, vertices_explored, edges_evaluated, execution_time, True)
        
        while queue:
            vertices_explored += 1
            current = queue.pop()

            if len(explored) > 0:
                for edge in current.get_edges():
                    if edge.get_destination().get_name() == explored[-1].get_name():
                        distance += edge.get_weight()

            explored.append(current)

            if current.get_name() == destination_vertex_name:
                return evaluate_path(True)
                
            
            for edge in current.get_edges():
                edges_evaluated += 1
                neighbor = edge.get_destination()
                if neighbor not in explored:
                    queue.add(neighbor, abs(vertex_data[neighbor.get_name()][0] - vertex_data[destination_vertex_name][0]) + abs(vertex_data[neighbor.get_name()][1] - vertex_data[destination_vertex_name][1]))


        return evaluate_path(False)
    
        
        

    def get_name(self) -> str:
        return self._name