from dataclasses import dataclass

@dataclass
class AlgorithmResult:
    textual_directions: str
    total_distance: float
    vertices_explored: int
    edges_evaluated: int
    execution_time: float
    path_found: bool
