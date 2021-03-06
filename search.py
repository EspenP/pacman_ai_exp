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

def reconstruct_path(trace, start, end):
    solution = util.Queue() # The first added direction will be the last one pacman needs to take, since we are backtracking
    child = end
    while True:
        solution.push(trace[child][1]) # Push the direction onto the queue
        child = trace[child][0]
        if child == start:
            break
    return solution.list

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
        if problem.isGoalState(pos): # Reached the end
            print("End found")
            return True              # Triggers end of search
        elif visited[pos] >= 1:      # Reached an already visited node
            if moves_taken:
                moves_taken.pop()
            return False             # Triggers backtracking

        visited[pos] += 1                       # Marked node as visited
        # print("Visited nodes: ", visited)
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
    # Initialize stuff
    start = problem.getStartState()
    end = start      # Variable to hold end node
    node = start
    trace = {start : []}     # trace[child] = [parent_node, parent to child direction]
    visited = util.Counter()
    visited[node] = 1

    # Explore layers until we find the goal.
    # Keep track of parents
    queue = util.Queue()
    while True:
        successors = problem.getSuccessors(node) # List of lists [((x, y), Direction, Cost)...]
        for x in successors:
            if visited[x[0]] == 0:
                queue.push(x)   # Store a ((x, y), Direction, Cost) in queue
                visited[x[0]] = 1
                trace[x[0]] = [node, x[1]] # Store [parent_node, parent to child direction]

        if queue.isEmpty():
            print("ALL NODES EXPLORED, NO SOLUTION")
            break
        else:
            node = queue.pop()[0]

        if problem.isGoalState(node):
            end = node
            break
        ## END WHILE LOOP ##

    # Reconstruct Path
    return reconstruct_path(trace, start, end)



def uniformCostSearch(problem):
    # Initialize stuff
    start = problem.getStartState() # Single node (x, y)
    end = start      # Variable to hold end node
    visited = util.Counter()

    queue = util.PriorityQueue()
    queue.push((start, []), 0)
    trace = {start : [None, None, 0]}     # trace[child] = [parent_node, parent to child direction, path_cost]
    PARENT, DIRECTION, COST = (0, 1, 2)
    while not queue.isEmpty():
        node, direction = queue.pop()
        if visited[node]:
            continue
        visited[node] = 1
        path_cost = trace[node][COST]

        if problem.isGoalState(node):
            end = node
            break

        successors = problem.getSuccessors(node)
        for s in successors:
            s_node, s_direction, s_cost = s
            # print(s_node, s_direction, s_cost)
            step_cost = path_cost + s_cost

            # Is the cost for the path to this location less than another existing path?
            if s_node in trace and trace[s_node][COST] <= step_cost:
                continue
            elif s_node in trace:
                queue.update((s_node, s_direction), step_cost)
            else:
                queue.update((s_node, s_direction), step_cost)
            trace[s_node] = [node, s_direction, step_cost]



    # Reconstruct Path
    return reconstruct_path(trace, start, end)

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
     # Initialize stuff
    start = problem.getStartState() # Single node (x, y)
    end = start      # Variable to hold end node
    visited = util.Counter()

    queue = util.PriorityQueue()
    queue.push((start, []), heuristic(start, problem))
    trace = {start : [None, None, 0]}     # trace[child] = [PARENT, NODE, COST]
    PARENT, DIRECTION, COST = (0, 1, 2)
    while not queue.isEmpty():
        node, direction = queue.pop()
        if visited[node]:
            continue
        visited[node] = 1
        path_cost = trace[node][COST]

        if problem.isGoalState(node):
            end = node
            break

        successors = problem.getSuccessors(node)
        for s in successors:
            s_node, s_direction, s_cost = s
            # print(s_node, s_direction, s_cost)
            step_cost = path_cost + s_cost

            # Is the cost for the path to this location less than another existing path?
            if s_node in trace and trace[s_node][COST] <= step_cost:
                continue
            elif s_node in trace:
                queue.update((s_node, s_direction), step_cost  + heuristic(s_node, problem))
            else:
                queue.update((s_node, s_direction), step_cost + heuristic(s_node, problem))
            trace[s_node] = [node, s_direction, step_cost]

    # Reconstruct Path
    return reconstruct_path(trace, start, end)



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
