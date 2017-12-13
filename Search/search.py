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

def depthFirstSearch(problem):

    # print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    # print "Start's successors:", problem.isGoalState(successor[1])

    ds_fringe = util.Stack()
    startState = (problem.getStartState(), 'X', 0)
    #goal = problem.goal
    visited = []
    ds_fringe.push(startState)
    count = 0
    parent_map = {}
    """Pushing items to stack till stack is found empty"""
    while ds_fringe:
        #print 'round', count
        #count +=1
        node = ds_fringe.pop()
        """If node has not been extended, append it to the close list"""
        if node not in visited:
            visited.append(node)
            """If Goal state found, return the path of actions from start to goal state"""
            if problem.isGoalState(node[0]):
                #print ' got true'
                path = []
                curr = node
                #Looking for parent_map which stores parent node of each expanded node
                while(curr[1]!='X'):
                    path = [curr[1]]+path
                    curr = parent_map[curr]
                new_path = path
                #print new_path
                return new_path
            else:
                successor = problem.getSuccessors(node[0])
                #print 'successor not in visited ',[x for x in successor[0:] if x not in visited]
                for x in successor:
                    #Pushing each succesor in Stack and storing their parent in a dictionary
                    if x[0] not in [k[0] for k in visited[0:]]:
                        #print 'visited ', visited[0]
                        #print 'pushing in stack ', x
                        parent_map[x] = node
                        ds_fringe.push(x)

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
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    ds_fringe = util.Queue()
    startState = (problem.getStartState(), 'X', 0)
    #goal = problem.goal
    visited = []
    ds_fringe.push(startState)
    count = 0
    parent_map = {}
    while ds_fringe:
        #print 'round', count
        count +=1
        node = ds_fringe.pop()

        if node not in visited:
            visited.append(node)
            if problem.isGoalState(node[0]):
                #print ' got true'
                path = []
                curr = node
                while(curr[1]!='X'):
                    #print curr[1]
                    #path.append(curr[1])
                    path = [curr[1]]+path
                    curr = parent_map[curr]
                new_path = path
                #print new_path
                return new_path
            else:
                successor = problem.getSuccessors(node[0])
                #print 'successor not in visited ',[x for x in successor[0:] if x not in visited]
                for x in successor:
                    if x[0] not in [k[0] for k in visited[0:]]:
                        #print 'visited ', visited[0]
                        #print 'pushing in stack ', x
                        parent_map[x] = node
                        ds_fringe.push(x)
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    ds_fringe = util.PriorityQueue()
    #ds_fringe = util.PriorityQueue()
    startState = (problem.getStartState(), 'X', 0)
    #goal = problem.goal
    visited = []
    ds_fringe.push(startState,0)
    count = 0
    parent_map = {}
    while ds_fringe:
        #print 'round', count
        count +=1
        node = ds_fringe.pop()

        if node not in visited:
            visited.append(node)
            if problem.isGoalState(node[0]):
                #print ' got true'
                path = []
                curr = node
                while(curr[1]!='X'):
                    #print curr[1]
                    #path.append(curr[1])
                    path = [curr[1]]+path
                    curr = parent_map[curr]
                new_path = path
                #print new_path
                return new_path
            else:
                successor = problem.getSuccessors(node[0])
                #print 'successor not in visited ',[x for x in successor[0:] if x not in visited]
                for x in successor:
                    if x[0] not in [k[0] for k in visited[0:]]:
                        #print 'visited ', visited[0]
                        #print 'pushing in stack ', x
                        parent_map[x] = node
                        path = []
                        curr = x
                        while(curr[1]!='X'):
                            path = [curr[1]]+path
                            curr = parent_map[curr]
                        cost = problem.getCostOfActions(path)
                        ds_fringe.push(x,cost)
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
    ds_fringe = util.PriorityQueue()
    #ds_fringe = util.PriorityQueue()
    startState = (problem.getStartState(), 'X', 0)
    #goal = problem.goal
    visited = []
    ds_fringe.push(startState,0)
    count = 0
    parent_map = {}
    while ds_fringe:
        #print 'round', count
        count +=1
        node = ds_fringe.pop()

        if node not in visited:
            visited.append(node)
            if problem.isGoalState(node[0]):
                #print ' got true'
                path = []
                curr = node
                while(curr[1]!='X'):
                    #print curr[1]
                    #path.append(curr[1])
                    path = [curr[1]]+path
                    curr = parent_map[curr]
                new_path = path
                #print new_path
                return new_path
            else:
                successor = problem.getSuccessors(node[0])
                #print 'successor not in visited ',[x for x in successor[0:] if x not in visited]
                for x in successor:
                    if x[0] not in [k[0] for k in visited[0:]]:
                        #print 'visited ', visited[0]
                        #print 'pushing in stack ', x
                        parent_map[x] = node
                        path = []
                        curr = x
                        while(curr[1]!='X'):
                            path = [curr[1]]+path
                            curr = parent_map[curr]
                        cost = problem.getCostOfActions(path) + heuristic(x[0], problem)
                        ds_fringe.push(x,cost)
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
