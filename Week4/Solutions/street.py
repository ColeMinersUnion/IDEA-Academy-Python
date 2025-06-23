class street:
    def __init__(self, length, nodes: tuple[str, str]):
        self.length = length
        self.nodes = nodes
        self.name = ""

    def __str__(self):
        return f"{self.name} St."
    


    
    
    