# Pacman-1
Introduction to Artificial Intelligence, Spring 2017, National Chiao Tung University

Assignment 1: Simple Agents, DFS, BFS, A*


## Notes

- Cannot run into both the current and next location of Ghosts


## Commands

### Simple Agents

Implemented in [`searchAgents.py`](searchAgents.py).

- P1-1 CleanerAgent  
```bash
python pacman.py -p CleanerAgent -l P1-1
```
- P1-2 FroggerAgent
```bash
python pacman.py -p FroggerAgent -l P1-2 -g StraightRandomGhost
```
- P1-3 SnakeAgent
```bash
python pacman.py -p SnakeAgent -l P1-3 -g StraightRandomGhost
```
- P1-4 DodgeAgent
```bash
python pacman.py -p DodgeAgent -l P1-4
```

### DFS, BFS, A*

Implemented in [`search.py`](search.py).

- P2-1 Depth-First-Search  
```bash
python pacman.py -l mediumMaze -p SearchAgent -a fn=dfs
```
- P2-2 Breadth-First Search  
```bash
python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
```
- P2-3 A* Search  
```bash
python pacman.py -l mediumMaze -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
```
