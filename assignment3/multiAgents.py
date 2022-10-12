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
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [
            index for index in range(len(scores)) if scores[index] == bestScore
        ]
        chosenIndex = random.choice(bestIndices)  # Pick randomly among the best

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

        "*** YOUR CODE HERE ***"
        return successorGameState.getScore()


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

    def __init__(self, evalFn="scoreEvaluationFunction", depth="2"):
        self.index = 0  # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)


class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"

        # Initialize bestScore to negative infinity
        bestScore = -float('inf')
        bestAction = None
        for action in gameState.getLegalActions(0):
            successorGameState = gameState.generateSuccessor(0, action)
            successorScore = self.minValue(successorGameState, 1, 0)

            # Check if this state is better than the best state so far
            if successorScore > bestScore:
                bestScore = successorScore
                bestAction = action

        return bestAction

    def maxValue(self, gameState, currentDepth=0):
        if currentDepth == self.depth or gameState.isWin() or gameState.isLose():
            return self.evaluationFunction(gameState)

        # Initialize bestScore to negative infinity
        bestScore = -float('inf')
        for action in gameState.getLegalActions(0):
            successorGameState = gameState.generateSuccessor(0, action)
            successorScore = self.minValue(successorGameState, 1, currentDepth)

            # Check if this state is better than the best state so far
            if successorScore > bestScore:
                bestScore = successorScore

        return bestScore

    def minValue(self, gameState, agentIndex, currentDepth=0):
        if gameState.isWin() or gameState.isLose():
            return self.evaluationFunction(gameState)

        # Initialize bestScore to positive infinity
        bestScore = float('inf')
        for action in gameState.getLegalActions(agentIndex):
            successorGameState = gameState.generateSuccessor(agentIndex, action)

            # If this is the last ghost, call maxValue to give Pacman the next move
            if agentIndex == gameState.getNumAgents() - 1:
                successorScore = self.maxValue(successorGameState, currentDepth + 1)
            else:
                successorScore = self.minValue(successorGameState, agentIndex + 1, currentDepth)

            # Check if this state is better than the best state so far
            if successorScore < bestScore:
                bestScore = successorScore

        return bestScore



class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"

        # Same idea as MinimaxAgent, but with alpha-beta pruning

        bestAction = None
        bestScore = -float('inf')

        # Initialize alpha to negative infinity
        alpha = -float('inf')

        for action in gameState.getLegalActions(0):
            successorGameState = gameState.generateSuccessor(0, action)
            successorScore = self.minValue(successorGameState, 1, alpha)
            
            if successorScore > bestScore:
                bestAction = action
                bestScore = successorScore

            # Update alpha to enable pruning
            if bestScore > alpha:
                alpha = bestScore

        return bestAction
            

    def maxValue(self, gameState, alpha=-float('inf'), beta=float('inf'), currentDepth=0):
        if gameState.isWin() or gameState.isLose() or currentDepth == self.depth:
            return self.evaluationFunction(gameState)

        bestScore = -float('inf')
        for action in gameState.getLegalActions(0):
            successorGameState = gameState.generateSuccessor(0, action)
            successorScore = self.minValue(successorGameState, 1, alpha, beta, currentDepth)
            
            if successorScore > bestScore:
                bestScore = successorScore
               
            # Update alpha to enable pruning
            if bestScore > alpha:
                alpha = bestScore

            # Prune if possible
            if beta < alpha:
                break

        return bestScore

    def minValue(self, gameState, agentIndex=1, alpha=-float('inf'), beta=float('inf'), currentDepth=0):
        if gameState.isWin() or gameState.isLose():
            return self.evaluationFunction(gameState)

        bestScore = float('inf')
        for action in gameState.getLegalActions(agentIndex):
            successorGameState = gameState.generateSuccessor(agentIndex, action)
            if agentIndex == gameState.getNumAgents() - 1:
                successorScore = self.maxValue(successorGameState, alpha, beta, currentDepth + 1)
            else:
                successorScore = self.minValue(successorGameState, agentIndex + 1, alpha, beta, currentDepth)

            if successorScore < bestScore:
                bestScore = successorScore

            # Update beta to enable pruning
            if bestScore < beta:
                beta = bestScore

            # Prune if possible
            if beta < alpha:
                break

        return bestScore

        

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
    Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()


def betterEvaluationFunction(currentGameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviation
better = betterEvaluationFunction
