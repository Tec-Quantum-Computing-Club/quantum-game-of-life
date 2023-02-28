# Quantum Game of Life

This project consists of a Quantum Cellular Automata based heavily on Jhon Conway's Game of Life, the process consists on a variable sized grid where each pixel represents a cell that can be either dead or alive, the process of dying and coming to life depends on the neighboring cells, so each snapshot is based on the last one following a certain set of rules. But this is _Quantum_ Game of life so cells can be Death *AND* Alive. The superposition of states allows for a dynamic system that is very different and much more random. Our program follows this other set of rules based on probabilities.

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

## Emerging Complexity

One of the main studied qualities of the original game of life is the emergence of complexity, which is the emergence of complex behaviour from simple parts, an important detail is that one could not predict the complex behaviour from knowing the rules that govern the smaller parts.
In this project we want to discover the change in the cellular automata's behaviour and the different dynamics that arise from allowing the natural "randomness" of quantum computing take the spotlight. Complex organized behaviour in this mondel is not perceivable because due to the probability based rules, a single initial state may lead to multiple outcomes, but the interactions between simple objects and complex dynamics as a result is there.

## The repository

Most 

