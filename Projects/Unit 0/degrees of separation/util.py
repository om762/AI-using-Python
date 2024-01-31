class Node:
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action

class StackFrontier:
    def __init__(self):
        self.frontier = []
    
    def add(self, node):
        self.frontier.append(node)
    
    def is_contain(self, state):
        return any(node.state == state for node in self.frontier)
    
    def is_empty(self):
        return len(self.frontier) == 0
    
    def remove(self):
        if self.is_empty():
            raise Exception("Stack is Empty")
        node =  self.frontier[-1]
        self.frontier = self.frontier[:-1]
        return node

class QueueFrontier(StackFrontier):
    def remove(self):
        if self.is_empty():
            raise Exception("Queue is Empty")
        node = self.frontier[0]
        self.frontier = self.frontier[1:]
        return node
