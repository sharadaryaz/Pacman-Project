# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
        newGhostPositions = successorGameState.getGhostPositions()
        newNumFood = successorGameState.getNumFood()
        newRemCapsules = successorGameState.getCapsules()
        "*** YOUR CODE HERE ***"
        #print "Successor Game State: ",successorGameState
        #print "New Position:  ", newPos
        #print "New Food ", newFood
        #print "New Ghost State ", newGhostStates
        #print "New Scared Times ", newScaredTimes
        #print "Ghost Positions", newGhostPositions
        
        """Calculating Distance to nearest food"""

        food_List = newFood.asList()
        if food_List:
          dis_closest_food = find_closest_item(newPos, food_List)

        """Calculating Distance to nearest ghost state"""
        if newGhostPositions:
          dis_closest_ghost = find_closest_item(newPos, newGhostPositions)
        if dis_closest_ghost==0:
          return float("-inf")

        """CALCULATING TOTAL Scraed Time"""
        total_scared_time = 0
        if newScaredTimes:
          for ScaredTime in newScaredTimes:
            total_scared_time += ScaredTime 

        """Calculating Distance from nearest Capsule"""
        if newRemCapsules:
          dis_closest_capsule = find_closest_item(newPos, newRemCapsules)
        eval_value = 100
        # print "Closest Food: ", dis_closest_food
        # print "Closest Ghost: ", dis_closest_ghost
        # print "Closest Capsule: ", dis_closest_capsule 
        # if newRemCapsules:
        #   eval_value = (10/dis_closest_food)+(10/dis_closest_capsule)+dis_closest_ghost/10+total_scared_time/20
        # else:
        #   eval_value = (10/dis_closest_food)+dis_closest_ghost/10+total_scared_time/20
        if food_List:
          eval_value = successorGameState.getScore() +  (1/dis_closest_food) + dis_closest_ghost  + total_scared_time
        return eval_value

def find_closest_item(position, corners):
    if len(corners) == 0:
        return None
    man_distance_list = []
    for corner in corners:
        man_distance = manhattanCornerHeuristic(position, corner)
        man_distance_list.append(man_distance)
    return min(man_distance_list)

def manhattanCornerHeuristic(position, corner):
    "The Manhattan distance heuristic for a CornersProblem"
    xy1 = position
    xy2 = corner
    return abs(xy1[0] - xy2[0]) + abs(xy1[1] - xy2[1])


def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState):
      def min_value(gameState, ghostID, depth):
        if depth> self.depth or gameState.isWin() or gameState.isLose():
          return self.evaluationFunction(gameState)
        min_eval_value = float('inf')
        legalActions = gameState.getLegalActions(ghostID)
        for action in legalActions:
          if ghostID == numGhosts:
            eval_value = max_value(gameState.generateSuccessor(ghostID, action), depth+1)
          else:
            eval_value = min_value(gameState.generateSuccessor(ghostID, action), ghostID+1, depth)
          min_eval_value =  min(eval_value, min_eval_value)
        return min_eval_value

      def max_value(gameState, depth):
        if depth> self.depth or gameState.isWin() or gameState.isLose():
          return self.evaluationFunction(gameState)
        max_eval_value = float('-inf')
        legalActions = gameState.getLegalActions(0)
        for action in legalActions:
          eval_value = min_value(gameState.generateSuccessor(0, action), 1, depth)
          max_eval_value =  max(eval_value, max_eval_value)
        return max_eval_value       
        
      depth = self.depth
      legalActions = []
      bestMove = None
      numGhosts = gameState.getNumAgents() - 1
      legalMoves = gameState.getLegalActions(0)
      for legalMove in legalMoves:
        if legalMove != Directions.STOP:
          legalActions.append(legalMove)

      minValues = {}
      for action in legalActions:
        minValues[action] = min_value(gameState.generateSuccessor(0, action),1,1)
      bestMove = max(minValues, key=minValues.get)

      #print "Minmax value is: ",max(minValues.values())
      return bestMove

      util.raiseNotDefined()

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
      def min_value(gameState, ghostID, depth, alpha, beta):
        if depth> self.depth or gameState.isWin() or gameState.isLose():
          return self.evaluationFunction(gameState)
        min_eval_value = float('inf')
        legalActions = gameState.getLegalActions(ghostID)
        for action in legalActions:
          if ghostID == numGhosts:
            eval_value = max_value(gameState.generateSuccessor(ghostID, action), depth+1, alpha, beta)
          else:
            eval_value = min_value(gameState.generateSuccessor(ghostID, action), ghostID+1, depth, alpha, beta)
          min_eval_value =  min(eval_value, min_eval_value)
          if alpha>min_eval_value:
            return min_eval_value
          beta = min(beta, min_eval_value)

        return min_eval_value

      def max_value(gameState, depth, alpha, beta):
        if depth> self.depth or gameState.isWin() or gameState.isLose():
          return self.evaluationFunction(gameState)
        max_eval_value = float('-inf')
        legalActions = gameState.getLegalActions(0)
        for action in legalActions:
          eval_value = min_value(gameState.generateSuccessor(0, action), 1, depth, alpha, beta)
          max_eval_value =  max(eval_value, max_eval_value)

          if max_eval_value>beta:
            return max_eval_value
          alpha = max(alpha, max_eval_value)
        return max(eval_value, max_eval_value)        
      
      alpha = float('-inf')
      beta = float('inf')
      depth = self.depth
      legalActions = []
      bestMove = None
      numGhosts = gameState.getNumAgents() - 1
      legalMoves = gameState.getLegalActions(0)
      for legalMove in legalMoves:
        if legalMove != Directions.STOP:
          legalActions.append(legalMove)
      minValues = {}
      for action in legalActions:
        minValues[action] = min_value(gameState.generateSuccessor(0, action),1,1, alpha, beta)
      bestMove = max(minValues, key=minValues.get)
      #print "Minmax value is: ",max(minValues.values())
      return bestMove



# Abbreviation
better = betterEvaluationFunction

