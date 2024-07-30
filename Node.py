class Node:
    def __init__(self, parent, action):
        self.parent = parent
        self.children = []
        self.times_visited = 0
        self.incoming_action = action
        self.total_simulation_reward = 0
        
        
    def calculate_UCB1(self):
        pass