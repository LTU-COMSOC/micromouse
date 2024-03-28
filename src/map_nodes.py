class node:
    def _init_(self, adjacent_nodes, value, next=0):
        self.value = value
        self.next = next
        self.adjacent_nodes = adjacent_nodes

    def get_adjacent_nodes(self):
        return adjacent_nodes
    
    def set_adjacent_nodes(self, adjacent_nodes):
        self.adjacent_nodes = adjacent_nodes

    def get_value(self):
        return self.value
    
    def get_next(self):
        return self.next

    def set_value(self, value):
        self.value = value

    def set_next(self, next):
        self.next = next

    def __str__(self):
        return str(self.value)