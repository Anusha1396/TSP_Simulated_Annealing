# Travelling Salesman Problem
Overview: This code solves Traveling Salesman problem with Local Search algorithm Simulated Annealing 
Recursively. Moving from starting postion to another by evaluating the best neighbour until Stopping criteria is reached.

Project Structure:
├── Model
  ├── tsp_solver.py
├── Algo
  ├── sa.py
├── utils
  ├──util.py
├── Input
  ├──input/a280.tsp
├── Output
  ├── solution.csv

How to Execute:
-alg <SA> -time <cutoff_in_seconds> -seed <random_seed>
i.e.

$python3 tsp_solver.py -inst ./input/a280.tsp -alg SA -time 100 -seed 37

