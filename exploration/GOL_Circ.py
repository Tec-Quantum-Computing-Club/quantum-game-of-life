import numpy as np
import matplotlib as plt
import pennylane as qml
from pennylane import numpy as np
# Import pygame module

u = np.zeros([2**3, 2**3])

dev = qml.device("default.qubit", wires= 12, shots = 1024)

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
    
    return qml.counts(wires = [8,9,10])

result = circuit([0,1,1,1,1,0,1,1])
print(result)