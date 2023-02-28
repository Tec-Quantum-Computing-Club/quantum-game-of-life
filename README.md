# Quantum Game of Life

This project consists of a Quantum Cellular Automata based heavily on Jhon Conway's Game of Life, the process in the original program consists on a variable sized grid where each pixel represents a cell that can be either dead or alive, the process of dying and coming to life depends on the neighboring cells, so each snapshot is based on the last one following a certain set of rules. But this is _Quantum_ Game of life so cells can be Death *AND* Alive. The superposition of states allows for a dynamic system that is very different and much more random. Our program follows this other set of rules based on probabilities.

### Too few
- 0 neighbors   ->  A living cell dies off     - 100% probability
- 1 neighbor    ->  A living cell dies off     - 50 % probability

### Goldilocks
- 2 neighbors   ->  A death cell comes to life - 50 % probability
- 3 neighbors   ->  A death cell comes to life - 100 % probability

### Too many
- 4 neighbors   ->  A living cell dies off     - 20 % probability
- 5 neighbors   ->  A living cell dies off     - 40 % probability
- 6 neighbors   ->  A living cell dies off     - 60 % probability
- 7 neighbors   ->  A living cell dies off     - 80 % probability
- 8 neighbors   ->  A living cell dies off     - 100% probability

## Superposition
First we planned on applying a treshold on this probabilities to see if the cell was death or alive, but then we realized that it would be much more fun if we just allow the superposition to thrive. Cells are ranked in a death-alive scale that is mapped to a grayscale. With this broken paradygm we realized that this is great visualization of superposition and the complexity that it introduces when a system is big enough. Thanks to this we also realized the potential that quantum computing has to simulate thermodynamic stochastic systems, with further work, this project will be analyzed in limits states and see what kind of result it gives in a muich bigger timelapse.

## Emerging Complexity

One of the main studied qualities of the original game of life is the emergence of complexity, which is the emergence of complex behaviour from simple parts, an important detail is that one could not predict the complex behaviour from knowing the rules that govern the smaller parts.
In this project we want to discover the change in the cellular automata's behaviour and the different dynamics that arise from allowing the intrinsic probabilistic nature of quantum computing take the spotlight. Complex organized behaviour in this mondel is not perceivable because due to the probability based rules, a single initial state may lead to multiple outcomes, but the interactions between simple objects and complex dynamics as a result is there.

# The repository

The final submission is the notebook QuantumGameOfLife.ipynb, the gif file is an example made with a 16 by 16 grid and the exploration folder has a lot of scrapped ideas and previous versions of the final code.
