from queue import PriorityQueue

def best_first_search(width, height, player_position, starting_position):
    # Create a 2D array of cells
    grid = [[(i, j) for j in range(width)] for i in range(height)]
    
    # Define the heuristic function for best-first search
    def heuristic(cell):
        x, y = cell
        px, py = player_position
        return abs(x - px) + abs(y - py)  # Manhattan distance
    
    # Initialize the priority queue with the player's position
    pq = PriorityQueue()
    pq.put((heuristic(starting_position), starting_position))
    
    # Visited set to keep track of explored cells
    visited = set()
    
    while not pq.empty():
        _, current_cell = pq.get()
        
        if current_cell == player_position:
            return current_cell  # Found the player's position
        
        visited.add(current_cell)
        
        # Explore the neighboring cells
        x, y = current_cell
        neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        for neighbor in neighbors:
            nx, ny = neighbor
            if 0 <= nx < height and 0 <= ny < width and neighbor not in visited:
                pq.put((heuristic(neighbor), neighbor))
                visited.add(neighbor)
    
    return player_position
