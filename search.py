# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

# P2-1
def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    
    "[Project 2] YOUR CODE HERE"
    
    from game import Directions
    
    s_start = problem.getStartState()
    if problem.isGoalState(s_start): return []
    
    visited = {}
    states = []
    s_iter = []
    actions = []
    s_nbs = {}
    
    visited[s_start] = True
    states.append(s_start)
    s_iter.append(0)
    s_nbs[s_start] = problem.getSuccessors(s_start)
    
    while len(states) > 0:
        s = states[-1]
        nbs = s_nbs[s]
        nb_used = False
        for i in range(s_iter[-1], len(nbs)):
            nb = nbs[i]
            s_iter[-1] = s_iter[-1] + 1
            if visited.has_key(nb[0]): continue
            visited[nb[0]] = True
            states.append(nb[0])
            s_iter.append(0)
            actions.append(nb[1])
            if problem.isGoalState(nb[0]): return actions
            s_nbs[nb[0]] = problem.getSuccessors(nb[0])
            nb_used = True
            break
        
        if nb_used == False:
            states.pop()
            s_iter.pop()
            if len(actions) > 0: actions.pop() # if s = start state then actions = empty
    
    return actions


# P2-2
def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    
    "[Project 2] YOUR CODE HERE"    
    
    from game import Directions
    
    s_start = problem.getStartState()
    
    visited = {}
    prv = {}
    states = util.Queue()
    
    visited[s_start] = True
    states.push(s_start)
    while not states.isEmpty():
        qs = states.pop()
        if (problem.isGoalState(qs)): break
        nbs = problem.getSuccessors(qs)
        for nb in nbs:
            if visited.has_key(nb[0]): continue
            visited[nb[0]] = True
            states.push(nb[0])
            prv[nb[0]] = (qs, nb[1])
    
    act_rev = []
    s = qs
    while s != s_start:
        act_rev.append(prv[s][1])
        s = prv[s][0]
    
    return act_rev[::-1]
    
#    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

# P2-3
def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "print heuristic(problem.getStartState(), problem)"
    
    "[Project 2] YOUR CODE HERE"
    
    from game import Directions
    
    s_start = problem.getStartState()
    
    expanded = {}
    min_g = {}
    prv = {}
    states = util.PriorityQueue()
    min_goal_s = (0, 0)
    min_goal_g = None
    
    min_g[s_start] = 0
    states.push(s_start, 0)
    while not states.isEmpty():
        qs = states.pop()
        qg = min_g[qs]
        if expanded.has_key(qs): continue
        expanded[qs] = True
        if problem.isGoalState(qs):
            if min_goal_g == None or qg < min_goal_g:
                min_goal_g = qg
                min_goal_s = qs
            break  # assuming only one goal
        nbs = problem.getSuccessors(qs)
        for nb in nbs:
            ng = qg + nb[2]
            nh = heuristic(nb[0], problem)
            if min_g.has_key(nb[0]) == False or ng < min_g[nb[0]]: 
                min_g[nb[0]] = ng
                states.push(nb[0], ng + nh)
                prv[nb[0]] = (qs, nb[1])
    
    print('astar finished')
    
    act_rev = []
    s = min_goal_s
    while s != s_start:
        act_rev.append(prv[s][1])
        s = prv[s][0]
    
    return act_rev[::-1]
     
    util.raiseNotDefined()


# Abbreviations
astar = aStarSearch
bfs = breadthFirstSearch
dfs = depthFirstSearch
ucs = uniformCostSearch
