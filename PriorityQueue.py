from graph_impl import IVertex
from typing import List

class PriorityQueue():
    def __init__(self) -> None:
        self._list: dict[IVertex, float] = {}
        self._values: dict[IVertex, float] = {}

    def add(self, item: IVertex, priority: float) -> None:
        if item in self._list.keys():
            if self._list[item] > priority:
                self._list[item] = priority
                self._values[item] = priority
        else:
            self._list[item] = priority
            self._values[item] = priority

    def get_value(self, key: IVertex) -> float: return self._values[key]
    def set_value(self, key: IVertex, value: float) -> None: self._values[key] = value

    def calculate_heuristic(self, item: IVertex, priority: float) -> float: 
        return priority

    def pop(self) -> IVertex:
        if  len(self._list) <= 0:
            raise IndexError("pop from empty PriorityQueue")
            
        next = []
        for k, v in self._list.items():
            if next == []:
                next = [k,v]
            elif next[1] > v:
                next = [k,v]
        del self._list[next[0]]

        return next[0]

    def __len__(self) -> int:
        return len(self._list)