import numpy as np
import matplotlib as plt
import pennylane as qml
from pennylane import numpy as np
# Import pygame module
import pygame

# Define constants
CELL_SIZE = 10 # Size of each cell in pixels
GRID_WIDTH = 10 # Number of cells in horizontal direction
GRID_HEIGHT = 10 # Number of cells in vertical direction
SCREEN_WIDTH = CELL_SIZE * GRID_WIDTH # Width of screen in pixels
SCREEN_HEIGHT = CELL_SIZE * GRID_HEIGHT # Height of screen in pixels
BLACK = (0, 0, 0) # Color for dead cells
WHITE = (255, 255, 255) # Color for alive cells

n_wires = 8 # number of qubits
shots = 32 # Shots to sample the circuit
u = np.zeros([2**3, 2**3]) #U matrix

# Initialize pygame and screen
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Conway's Game of Life")

# Define grid as a list of lists Initialize cells
grid = []
for i in range(GRID_HEIGHT):
    row = []
    for j in range(GRID_WIDTH):
        if j == GRID_HEIGHT/5:
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

dev = qml.device("default.qubit", wires= 12, shots = shots)
@qml.qnode(dev)
def circuit(x):

    for ii in range(len(x)):
            qml.RY(np.arccos(-2*x[ii]+1), ii)

    for ii in range(2**3):
        u[ii][ii-1] = 1

    for ii in range(8):
        qml.ControlledQubitUnitary(u, control_wires= ii, wires = [8,9,10])
    
    

    qml.ctrl(qml.Hadamard, (8,9,10), control_values=(0,0,1))(11)
    
    qml.ctrl(qml.Hadamard, (8, 9, 10), control_values=(0,1,0))(11)

    qml.ctrl(qml.PauliX, (8, 9, 10), control_values=(0,1,1))(11)
    
    qml.ctrl(qml.RY, (8,9,10), control_values=(1,0,0))(np.arccos(-0.6), 11)
    
    qml.ctrl(qml.RY, (8,9,10), control_values=(1,0,1))(np.arccos(-0.2), 11)
 
    qml.ctrl(qml.RY, (8,9,10), control_values=(1,1,0))(np.arccos(0.2), 11)

    qml.ctrl(qml.RY, (8,9,10), control_values=(1,1,1))(np.arccos(0.6), 11)
    
    return qml.counts(wires = 11)


def quantum_update():
    global grid     #Define global grid
    new_grid = []
    for i in range(GRID_HEIGHT):
        new_row = []
        for j in range(GRID_WIDTH):     
            cirq  = []      #Create circuit with adjacent cells
            for di in [-1, 0 ,1]: 
                for dj in [-1 ,0 ,1]:
                    if di == 0 and dj == 0: # Skip self
                        continue 
                    ni = i + di # Neighbor row index 
                    nj = j + dj # Neighbor column index 
                    if ni < 0 or ni >= GRID_HEIGHT or nj < 0 or nj >= GRID_WIDTH: # Skip out-of-bounds cells 
                        cirq.append(0)
                        continue 
                    cirq.append(grid[ni][nj])
            cell_state = circuit(cirq)      #Final state of the circuit
            keys = list(cell_state.keys())  #Check for keys in case of unique state 0 or 1
            if cell_state[keys[0]] > shots/2:
                cell_state = 0
            else: 
                cell_state = 1
            new_row.append(cell_state)
        new_grid.append(new_row)
    grid = new_grid     #Updated grid


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
        #get_neighbors()
        draw_grid() # Draw grid on screen
        quantum_update()
        #update_grid() # Update grid according to rules
        pygame.display.flip() # Update display

# Call main function
main()            