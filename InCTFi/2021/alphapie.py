from warnings import warn
import heapq

game1 = []
game2 = []

class Node:
    """
    A node class for A* Pathfinding
    """

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position
    
    def __repr__(self):
      return f"{self.position} - g: {self.g} h: {self.h} f: {self.f}"

    # defining less than for purposes of heap queue
    def __lt__(self, other):
      return self.f < other.f
    
    # defining greater than for purposes of heap queue
    def __gt__(self, other):
      return self.f > other.f

def return_path(current_node):
    path = []
    current = current_node
    while current is not None:
        path.append(current.position)
        current = current.parent
    return path[::-1]  # Return reversed path


def astar(maze, start, end, allow_diagonal_movement = False):
    """
    Returns a list of tuples as a path from the given start to the given end in the given maze
    :param maze:
    :param start:
    :param end:
    :return:
    """

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Heapify the open_list and Add the start node
    heapq.heapify(open_list) 
    heapq.heappush(open_list, start_node)

    # Adding a stop condition
    outer_iterations = 0
    max_iterations = (len(maze[0]) * len(maze) // 2)

    # what squares do we search
    adjacent_squares = ((0, -1), (0, 1), (-1, 0), (1, 0),)
    if allow_diagonal_movement:
        adjacent_squares = ((0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1),)

    # Loop until you find the end
    while len(open_list) > 0:
        outer_iterations += 1

        if outer_iterations > max_iterations:
          # if we hit this point return the path such as it is
          # it will not contain the destination
          warn("giving up on pathfinding too many iterations")
          return return_path(current_node)       
        
        # Get the current node
        current_node = heapq.heappop(open_list)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            return return_path(current_node)

        # Generate children
        children = []
        
        for new_position in adjacent_squares: # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:
            # Child is on the closed list
            if len([closed_child for closed_child in closed_list if closed_child == child]) > 0:
                continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            if len([open_node for open_node in open_list if child.position == open_node.position and child.g > open_node.g]) > 0:
                continue

            # Add the child to the open list
            heapq.heappush(open_list, child)

    warn("Couldn't get a path to destination")
    return None

def find_pos(var, arr):
    x = 0
    y = 0

    for line in arr:
        y = 0
        for col in line:
            if col == var:
                return x, y
            y += 1
        x += 1
    print("error find pos")

def init_game(test):
    global game1
    global game2

    game1 = []
    game2 = []
    check = False

    for line in test:
        if len(line) > 0 and line[0] == '+':
            check = not check
            continue
        if check:
            game = [s.strip() for s in line.split('|')[1:-1] if not s.strip() == '']
            game2.append(game[len(game)//2:])
            game1.append(game[:len(game)//2])

def do_game():
    global game1
    global game2

    vars = []
    result = []

    for line in game1:
        for var in line:
            if not var == '0':
                vars.append(var)

    for var in vars:
        startx, starty = find_pos(var, game1)
        endx, endy = find_pos(var, game2)

        map = []

        for line in range(len(game1)):
            map.append([])
            for col in range(len(game1[line])):
                if game1[line][col] == '0':
                    map[-1].append(0)
                else:
                    map[-1].append(1)

        path = astar(map, (startx, starty), (endx, endy))
        game1[startx][starty] = '0'
        game1[endx][endy] = var
        
        for coord in range(len(path)):
            if coord == 0:
                continue
            result.append(f"{path[coord - 1][0]},{path[coord - 1][1]},{path[coord][0]},{path[coord][1]}")
    return result

file = open('nc.txt',mode='r') #Current level
data = file.read()
init_game(data.splitlines())
movs = do_game()

for test in movs:
    print(test)

print(len(movs))