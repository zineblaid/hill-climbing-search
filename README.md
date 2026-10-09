# Hill Climbing Search Algorithm

## Overview

This project implements the Hill Climbing algorithm in Python to maximize a discrete objective function \(F(n)\) over a set of 16 states.

Starting from an initial state, the algorithm evaluates neighboring states and moves to the neighbor with the highest objective-function value if it improves the current value. It stops when no neighbor offers a better value, indicating that a local optimum has been reached.

## Objectives

- Define a discrete objective function.
- Represent neighboring states.
- Implement the Hill Climbing optimization algorithm.
- Evaluate neighboring states and select the best one.
- Detect when a local optimum has been reached.
- Display the search process step by step.

## Technologies

- Python 3

## Algorithm

1. Initialize the current state.
2. Evaluate the objective function at the current state.
3. Identify the neighboring states.
4. Select the neighbor with the highest objective-function value.
5. If the best neighbor does not improve the current value, stop.
6. Otherwise, move to the best neighbor and repeat.

## Objective Function

The function \(F(n)\) is defined for integer states from 1 to 16. Each state is assigned a predefined value stored in a Python dictionary.

## Neighborhood Definition

Each state is connected to its adjacent states:

- State 1 has neighbor 2.
- State 16 has neighbor 15.
- Every other state \(n\) has neighbors \(n-1\) and \(n+1\).

## How to Run

Make sure Python 3 is installed, then run:

```bash
python main.py
```

The program starts the search from state 1 and prints the current state, its objective-function value, and a message when no better neighboring state exists.

## Limitations

- The algorithm performs local search and does not guarantee finding the global optimum.
- The search depends on the initial state.
- The objective function and neighborhood are predefined.
- The implementation uses simple Hill Climbing without random restarts or backtracking.

## Possible Improvements

- Allow the initial state to be entered by the user.
- Visualize the objective function and the search path.
- Compare different initial states.
- Implement variants such as Steepest-Ascent Hill Climbing and Random-Restart Hill Climbing.

## License

Add a license file if you intend to specify how others may use, modify, and distribute this project.
