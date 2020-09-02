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
    util.pause()
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):

    # Initialize start state and counter
    start = problem.getStartState() # Get start position
    visited = util.Counter()  # Create a system for keeping track of visited vertices

    # Initialize stack and a list of moves taken
    stack = util.Stack()
    print(stack.list)
    moves_taken = [] # Holds the moves taken along a path

    # Define our recursive function
    def DFS(pos):
        print("Position ", pos)
        if problem.isGoalState(pos): # Reached the end
            print("End found")
            return True              # Triggers end of search
        elif visited[pos] >= 1:      # Reached an already visited node
            if moves_taken:
                moves_taken.pop()
            return False             # Triggers backtracking

        visited[pos] += 1                       # Marked node as visited
        # print("Visited nodes: ", visited)
        print("Found new pos", pos)
        successors = util.Stack() # Introduce new nodes to the stack
        adjacent = problem.getSuccessors(pos)
        for x in adjacent:
            if visited[x] == 0:
                successors.push(x)

        while True:
            if successors.isEmpty():
                if moves_taken:
                    moves_taken.pop()
                return False # Triggers backtracking
            print("Valid moves", successors.list)
            move = successors.pop()
            moves_taken.append(move[1]) # Append the direction
            if DFS(move[0]):
                return True

    if DFS(start):
        print("Maze solved")
        return moves_taken
    else:
        print("Error solving maze")
        print(moves_taken)
        return


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
