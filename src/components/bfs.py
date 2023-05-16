

class Rocket:

  def __init__(self, width, height, player_position):
    # Create a 2D array to represent the frame.
    self.grid = [[0 for i in range(10)] for j in range(10)]

    # Calculate the cell that the player is currently in.
    self.cell_x = player_position.x // width
    self.cell_y = player_position.y // height

    # Set the cell that the player is currently in to 1.
    self.grid[self.cell_x][self.cell_y] = 1

  def wait(self, seconds):
    # Wait for the specified number of seconds.
    pygame.time.wait(seconds * 1000)

  def find_path(self):
    # Use best-first search to find the path from the old cell to the new cell.
    return bfs(self.grid, self.cell_x, self.cell_y, self.new_cell_x, self.new_cell_y)

  def get_last_cell(self, path):
    # Return the last cell in the path.
    return path[-1]

def bfs(grid, start_x, start_y, end_x, end_y):
  # Create a queue to store the cells that have not been visited yet.
  queue = []

  # Add the start cell to the queue.
  queue.append((start_x, start_y))

  # While the queue is not empty, do the following:
  while queue:
    # Get the next cell from the queue.
    cell = queue.pop(0)

    # If the cell is the end cell, return the path to the cell.
    if cell[0] == end_x and cell[1] == end_y:
      return get_path(cell)

    # For each neighbor of the cell, do the following:
    for neighbor in get_neighbors(cell):
      # If the neighbor has not been visited yet, do the following:
      if grid[neighbor[0]][neighbor[1]] == 0:
        # Mark the neighbor as visited.
        grid[neighbor[0]][neighbor[1]] = 1

        # Add the neighbor to the queue.
        queue.append(neighbor)

  # The end cell was not found.
  return []

def get_neighbors(cell):
  # Get the possible neighbors of the cell.
  neighbors = [(cell[0] - 1, cell[1]), (cell[0] + 1, cell[1]), (cell[0], cell[1] - 1), (cell[0], cell[1] + 1)]

  # Remove any neighbors that are outside of the frame.
  neighbors = [neighbor for neighbor in neighbors if 0 <= neighbor[0] < 10 and 0 <= neighbor[1] < 10]

  # Return the neighbors.
  return neighbors

def get_path(cell):
  # Create a list to store the path.
  path = []

  # While the cell is not the start cell, do the following:
  while cell != (0, 0):
    # Add the cell to the path.
    path.append(cell)

    # Get the parent cell of the current cell.
    cell = cell[2]

  # Reverse the path.
  path.reverse()

  # Return the path.
  return path