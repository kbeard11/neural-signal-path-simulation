# Neural Signal Path Simulation

## Overview
This project simulates how a neural signal travels through a grid of neurons that progressively fail over time. The model introduces random failures, probability‑based degradation, and adaptive rerouting behaviour (sideways and diagonal movement) to mimic how biological neural pathways compensate for damage. The simulation outputs whether the signal successfully reaches the end of the pathway or becomes blocked due to neuron loss.

## Features
- 10×10 neuron matrix representing a simplified neural pathway
- Random neuron failure each year
- Probability‑based degradation that increases over time
- Forward, sideways, and diagonal signal movement
- Signal strength reduction based on rerouting
- Memory success/failure outcome
- Clear console output showing yearly degradation

## How It Works
The simulation runs over multiple “years.”

Each year includes:
1. Random failure: One neuron is randomly selected and set to failed.
2. Probability failure: Each neuron has a chance to fail based on a growing probability.
3. Signal propagation:
    - The signal attempts to move forward through the matrix.
    - If blocked, it tries sideways movement.
    - If still blocked, it attempts diagonal movement.
    - If no valid path exists, memory retrieval fails.
    
The model demonstrates how increasing neuron loss affects the ability of a signal to reach its destination.

## Future Improvements
Planned enhancements include:
- Gene expression noise affecting neuron susceptibility
- Partial neuron degradation (not just binary alive/dead)
- Neuroplasticity modelling (strengthening alternative pathways)
- Statistical logging across multiple runs
- Monte Carlo analysis
- Heatmaps of neuron failure
- Visualisation of signal paths

## Why I Built This
This project explores how biological systems degrade and adapt under stress. It also serves as a platform for learning Python simulation design, stochastic modelling, and data analysis.

## License
- MIT License
