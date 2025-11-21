# Circular Deque, Sliding Window Max, and Winning Probability

This project implements a dynamic **CircularDeque** data structure and two algorithms that use it.

## Features

### 🔄 CircularDeque
A custom deque supporting:
- Push/remove from **front or back**
- Automatic **grow** (double capacity) and **shrink** (halve capacity)
- Access to:
  - `front_element()`
  - `back_element()`
  - `enqueue()`
  - `dequeue()`
  - `is_empty()`
- Tracks `size`, `capacity`, `front`, and `back`

Implementation: `solution.py` :contentReference[oaicite:0]{index=0}

### 📈 Sliding Window Maximum
`get_winning_numbers(numbers, size)`  
Returns the **maximum of each sliding window** using the deque for O(n) efficiency.

### 🎲 Winning Probability (DP)
`get_winning_probability(winning_numbers)`  
Computes the **maximum sum of non-adjacent values** using dynamic programming.

## Summary
A small project showcasing:
- A fully dynamic circular deque  
- An O(n) sliding-window max algorithm  
- A DP solution for choosing the best non-adjacent values  
All contained in `solution.py`.
