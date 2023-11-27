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

    def contain_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("Empty Frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node


class QueueFrontier(StackFrontier):
    def remove(self):
        if self.empty():
            raise Exception("Empty Frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node


class Maze:
    def __init__(self, filename):
        with open(filename) as f:
            contents = f.read()

        if contents.count("A") != 1:
            raise Exception("Starting point must be one")

        if contents.count("B") != 1:
            raise Exception("Ending point must be one")

        contents = contents.splitlines()
        self.height = len(contents)
        self.width = max(len(line) for line in contents)

        self.walls = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                try:
                    if contents[i][j] == "A":
                        self.start = (i, j)
                        row.append(False)
                    elif contents[i][j] == "B":
                        self.goal = (i, j)
                        row.append(False)
                    elif contents[i][j] == " ":
                        row.append(False)
                    else:
                        row.append(True)

                except IndexError:
                    row.append(False)
            self.walls.append(row)

        self.Solution = None
        self.explored = {}  # Initialize explored set

    def print(self):
        Solution = self.Solution[1] if self.Solution is not None else None
        print()

        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):
                if col:
                    print("█", end="")
                elif (i, j) == self.start:
                    print("A", end="")
                elif (i, j) == self.goal:
                    print("B", end="")
                elif Solution is not None and (i, j) in Solution:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
        print()

    def neighbors(self, state):
        row, col = state

        # All Possible Action
        candidates = [
            ("up", (row - 1, col)),
            ("down", (row + 1, col)),
            ("left", (row, col - 1)),
            ("right", (row, col + 1)),
        ]

        # Ensure that action are valid
        result = []
        for action, (r, c) in candidates:
            try:
                if not self.walls[r][c]:
                    result.append((action, (r, c)))
            except IndexError:
                continue
        return result

    # The main Focus
    def Solve(self):
        """/find the solution if one exist in maze"""

        # Keep Track the number of step explored
        self.num_expl = 0

        # initialize the front to the start position
        start = Node(state=self.start, parent=None, action=None)
        choice = int(input("Enter 0 for BFS and 1 for DFS : "))
        if choice == 0:
            frontier = QueueFrontier()
        elif choice == 1:
            frontier = StackFrontier()
        else:
            print("You Entered the wrong choice so we go we DFS ")
            frontier = QueueFrontier()
        frontier.add(start)

        # initialize an explored set
        self.explored = set()

        # keep looping until solution found
        while True:
            # if nothing left in frontier then there is no solution
            if frontier.empty():
                raise Exception("NO SOLUTION")

            # choose a node from frontier
            node = frontier.remove()
            self.num_expl += 1  # Increment the number of explored nodes

            # Check Whether it's a goal
            if node.state == self.goal:
                action = []
                cells = []

                # Follow parent node to find the solution
                while node.parent is not None:
                    action.append(node.action)
                    cells.append(node.state)
                    node = node.parent

                action.reverse()
                cells.reverse()

                self.Solution = (action, cells)
                return

            # Mark the node as explored
            self.explored.add(node.state)

            # Add Neighbors to frontier
            for action, state in self.neighbors(node.state):
                if not frontier.contain_state(state) and state not in self.explored:
                    child = Node(state=state, parent=node, action=action)
                    frontier.add(child)

    def output_image(self, filename, show_solution=True, show_explored=False):
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
                elif solution is not None and show_explored and (i, j) in self.explored:
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
print("State Explored : ", m.num_expl)
print("Solution:")
m.print()
explored = int(input("Enter 1 to show explores path else 0 : "))
m.output_image("maze.png", show_solution=True, show_explored=bool(explored))
