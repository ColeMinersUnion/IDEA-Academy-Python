from building import building
from street import street

class roadmap:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node: building):
        if str(node) not in self.nodes:
            self.nodes[str(node)] = node
    
    def find_path(self, start: str, end: str):
        # Implement djikstras algorithm

        pass

    