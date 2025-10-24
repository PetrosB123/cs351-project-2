from typing import Protocol
from AlgorithmResult import AlgorithmResult
from graph_interfaces import IGraph, IVertex, IEdge

class IAlgorithm(Protocol):
    def find_path(
        self,
        graph: IGraph,
        start_vertex_name: str,
        destination_vertex_name: str
    ) -> AlgorithmResult:
        ...
    
    def get_name(self) -> str:
        ...