import numpy as np
import matplotlib as plt
import pennylane as qml
from pennylane import numpy as np
# Import pygame module
import pygame

# Define constants
CELL_SIZE = 10 # Size of each cell in pixels
GRID_WIDTH = 30 # Number of cells in horizontal direction
GRID_HEIGHT = 30 # Number of cells in vertical direction
SCREEN_WIDTH = CELL_SIZE * GRID_WIDTH # Width of screen in pixels
SCREEN_HEIGHT = CELL_SIZE * GRID_HEIGHT # Height of screen in pixels
BLACK = (0, 0, 0) # Color for dead cells
GRAY = (127, 127, 127) # Color of schrodinger cells
WHITE = (255, 255, 255) # Color for alive cells

n_wires = 8 # number of qubits

# Initialize pygame and screen
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Conway's Game of Life")

# Define grid as a list of lists Initialize cells
grid = []
for i in range(GRID_HEIGHT):
    row = []
    for j in range(GRID_WIDTH):
        if j == GRID_HEIGHT/2:
            row.append(1)
        row.append(0) # 0 means dead cell, 1 means alive cell
    grid.append(row)

# Define function to draw grid on screen
def draw_grid():
    """Draw grid on screen"""
    for i in range(GRID_HEIGHT):
        for j in range(GRID_WIDTH):
            if grid[i][j] == 0: # If dead cell
                color = BLACK 
            else: # If alive cell
                color = WHITE 
            pygame.draw.rect(screen, color, (j * CELL_SIZE, i * CELL_SIZE,
                                             CELL_SIZE - 1, CELL_SIZE - 1))

# Get neightbor cells by quantum sampling of 8 qubits
def get_neighbors():
    for i in range(GRID_HEIGHT):
        for j in range(GRID_WIDTH):
            if grid[i][j] == 1:
                               
                # Define device
                dev = qml.device("default.qubit", wires=n_wires,shots = 1)
                # Define QCA circuit 
                @qml.qnode(dev)
                def qca_circuit():
                    for i in range(n_wires):
                        qml.Hadamard(wires = i) 
                    return [qml.sample(qml.PauliZ(i)) for i in range(n_wires)]
                
                
                output = np.array(qca_circuit())
                M = (1 - output) / 2 #States of the adyascent pixels
                count = 0
                for di in [-1, 0 ,1]: 
                    for dj in [-1 ,0 ,1]:
                        if di == 0 and dj == 0: # Skip self
                            continue 
                        ni = i + di # Neighbor row index
                        nj = j + dj # Neighbor column index
                        if ni < 0 or ni >= GRID_HEIGHT or nj < 0 or nj >= GRID_WIDTH: # Skip out-of-bounds cells 
                            continue 
                        grid[ni][nj] == M[count][0]     #assign state to neighbors
                        count += 1
                        

# Define function to count neighbors of a cell
def count_neighbors(i, j):
    """Count neighbors of a cell at position (i,j)"""
    count = 0
    for di in [-1, 0 ,1]:
        for dj in [-1 ,0 ,1]:
            if di == 0 and dj == 0: # Skip self
                continue
            ni = i + di # Neighbor row index
            nj = j + dj # Neighbor column index
            if ni < 0 or ni >= GRID_HEIGHT or nj < 0 or nj >= GRID_WIDTH: # Skip out-of-bounds cells
                continue
            if grid[ni][nj] == 1: # If neighbor is alive
                count += 1 # Increase count by one
    return count # Return count


# Define function to update grid according to rules
def update_grid():
    """Update grid according to rules"""
    global grid # Use global variable grid 
    new_grid = [] # Create a new grid 
    for i in range(GRID_HEIGHT):
        new_row = []
        for j in range(GRID_WIDTH):
            state = grid[i][j] # Current state of cell 
            neighbors = count_neighbors(i, j) # Number of neighbors 
            if state == 0 and neighbors == 3: # Rule 1: Birth
                new_state = 1 # Cell becomes alive 
            elif state == 1 and (neighbors < 2): # Rule 2: Death
                new_state = 0 # Cell dies 
            else: # Rule 3: Survival
                new_state = state # Cell stays the same 
            new_row.append(new_state) # Add new state to new row 
        new_grid.append(new_row) # Add new row to new grid 
    grid = new_grid # Replace old grid with new grid 

# Define function to handle events
def handle_events():
    """Handle events"""
    for event in pygame.event.get(): # Loop through all events 
        if event.type == pygame.QUIT: # If user clicks close button 
            pygame.quit() # Quit pygame 
            exit() # Exit program 

# Define main loop
def main():
    """Main loop"""
    while True: # Loop forever
        handle_events() # Handle events
        get_neighbors()
        draw_grid() # Draw grid on screen
        update_grid() # Update grid according to rules
        pygame.display.flip() # Update display

# Call main function
main()            