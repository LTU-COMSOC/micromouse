class node:
    def _init_(self, adjacent_nodes, value, next=0, accessible = -1, start_state = False, goal_state = False, degree_45_combo = False, straight_line_combo = False, corner_node = False):
        self.value = value
        self.next = next
        self.adjacent_nodes = adjacent_nodes
        self.accessible = accessible
        self.start_state = start_state
        self.goal_state = goal_state
        self.degree_45_combo = degree_45_combo
        self.straight_line_combo = straight_line_combo
        self.corner_node = corner_node

    def degree_45_combo_check(self):
        #hi
        return self.degree_45_combo

    def straight_line_combo_check(self):
        return self.straight_line_combo
    
    def corner_node_check(self):
        return self.corner_node

    def get_adjacent_nodes(self):
        return self.adjacent_nodes
    
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
        
    def check_goal_state(self):
        # Returns value if the current node is a goal state or not
        return self.goal_state
        
    def accessible_check(self):
        # Can be used to create a map full of available nodes, removing the inaccessible nodes,
        # potentially reducing compute time
        
        # Checks to see if there are adjacent nodes
        # If value is -1, then it is unknown.
        # 0 is False - Not accessible
        # 1 is True - Accessible
        check_val = False
        if self.adjacent_nodes != None:
            check_val = True
        return check_val

    def __str__(self):
        return str(self.value)