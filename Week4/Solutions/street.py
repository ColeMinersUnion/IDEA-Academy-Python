class street:
    def __init__(self, length, nodes):
        self.length = length
        self.nodes = nodes
        self.name = ""
        self.buildings = []

    def __str__(self):
        return f"{self.name} St."

    
    
    