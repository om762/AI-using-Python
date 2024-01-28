import sys
from PIL import Image, ImageDraw

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
        if self.is_empty() is True:
            raise Exception("Stack is Empty")
        node = self.frontier[-1]
        self.frontier = self.frontier[:-1]
        return node

class QueueFrontier(StackFrontier):
    def remove(self):
        if self.is_empty() is True:
            raise Exception("Queue is Empty")
        node = self.frontier[0]
        self.frontier = self.frontier[1:]
        return node

class Maze:
    def __init__(self, mazeFile):
        with open(mazeFile) as f:
            content = f.read()
        
        if content.count("A") != 1:
            raise Exception("Maze must contain one Starting point")
        if content.count("B") != 1:
            raise Exception("Maze must contain one Ending point")
        
        content = content.splitlines()
        self.height = len(content)
        self.width = max(len(row) for row in content)
        self.walls = []
        self.Solution = None
        self.Explored = set()
        
        for i in range(self.height):
            row = []
            for j in range(self.width):
                try:
                    if content[i][j] == "A":
                        self.start = (i, j)
                        row.append(False)
                    elif content[i][j] == "B":
                        self.goal = (i, j)
                        row.append(False)
                    elif content[i][j] == " ":
                        row.append(False)
                    else:
                        row.append(True)
                except IndexError:
                    row.append(False)
            self.walls.append(row)
    
    def neighbore_states(self, state):
        row, col = state
        result = []
        candidate = [
            ("up", (row - 1, col)),
            ("down", (row + 1, col)),
            ("left", (row, col - 1)),
            ("right", (row, col + 1))
        ]
        
        for action, (r, c) in candidate:
            try:
                if not self.walls[r][c]:
                    result.append((action, (r, c)))
            except IndexError:
                continue
        return result
    
    def makeSolution(self, node):
        actions = []
        cells = []
        
        while node.parent is not None:
            actions.append(node.action)
            cells.append(node.state)
            node = node.parent
        
        actions.reverse()
        cells.reverse()
        
        return (actions, cells)
    
    def Solve(self):
        self.cost = 0
        self.Explored = {tuple}
        
        while True:
            choice = int(input("Enter 0 for DFS and 1 for BFS: "))
            if choice == 0:
                frontier = StackFrontier()
                break
            elif choice == 1:
                frontier = QueueFrontier()
                break
            else:
                print("Wrong choice! Try again")
        
        node = Node(state=self.start, parent=None, action=None)
        frontier.add(node)
        
        while True:
            if frontier.is_empty() is True:
                raise Exception("No Solution")
            node = frontier.remove()
            if node.state == self.goal:
                self.Solution = self.makeSolution(node)
                return
            
            self.cost = self.cost + 1
            self.Explored.add(node.state)
            
            for action, state in self.neighbore_states(node.state):
                if frontier.is_contain(state) is False and state not in self.Explored:
                    newNode = Node(state= state, parent= node, action= action)
                    frontier.add(newNode)
    
    def print(self):
        
        solution = self.Solution[1] if self.Solution is not None else None
        print()
        for i in range(self.height):
            for j in range(self.width):
                if (i, j) == self.start:
                    print("A", end="")
                elif (i, j) == self.goal:
                    print("B", end="")
                elif self.walls[i][j]:
                    print("█", end="")
                elif solution is not None and (i, j) in solution:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
        print()
    
    def output_image(self, show_solution=True, show_explored=False):
        cell_size = 50
        cell_border = 2
        
        # Create a blank canvas
        img = Image.new(
            "RGBA", (self.width * cell_size, self.height * cell_size), "black"
        )
        draw = ImageDraw.Draw(img)
        
        solution = self.Solution[1] if self.Solution is not None else None
        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):
                # Walls
                if col:
                    fill = (40, 40, 40)
                    
                # Start
                elif (i, j) == self.start:
                    fill = (255, 0, 0)
                    
                # Goal
                elif (i, j) == self.goal:
                    fill = (0, 171, 28)
                    
                # Solution
                elif solution is not None and show_solution and (i, j) in solution:
                    fill = (220, 235, 113)
                    
                # Explored
                elif solution is not None and show_explored and (i, j) in self.Explored:
                    fill = (212, 97, 85)
                    
                # Empty cell
                else:
                    fill = (237, 240, 252)
                    
                # Draw cell
                draw.rectangle(
                    (
                        [
                            (j * cell_size + cell_border, i * cell_size + cell_border),
                            (
                                (j + 1) * cell_size - cell_border,
                                (i + 1) * cell_size - cell_border,
                            ),
                        ]
                    ),
                    fill=fill,
                )
        image_name = input("Enter a name for image : ")
        img.save(image_name + ".png")
        img.show()

if len(sys.argv) != 2:
    sys.exit("Usage: python maze.py maze.txt")

m = Maze(sys.argv[1])
print("MAZE:")
m.print()
print("Solving")
m.Solve()
print("State Explored : ", m.cost)
print("Solution: ")
m.print()
explored = int(input("Enter 1 to show explores path else 0 : "))
m.output_image(show_solution=True, show_explored=bool(explored))