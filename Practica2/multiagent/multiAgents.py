# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
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

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
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
        """
        
        def miniMax(gameState, agent, depth):
            result = []

            if not gameState.getLegalActions(agent) or depth == self.depth: #si l'agent no te mes accions hem acabat.
                return self.evaluationFunction(gameState), 0

            if agent == gameState.getNumAgents() - 1:
                depth += 1 #si s'han calculat tots els fantasmes, incrementem la profunditat.

            """---------------------------
                    Calcular nextAgent
            ---------------------------"""
            
            
            if agent == gameState.getNumAgents() - 1:
                nextAgent = self.index
            else:
                nextAgent = agent + 1

            #per a cada estat seguent cridem el minmax
            for action in gameState.getLegalActions(agent):

                if not result: #guardem sempre el primer estat ja que necessitem la llista una miqueta plena.
                    nextValue = miniMax(gameState.generateSuccessor(agent, action), nextAgent, depth)

                    result.append(nextValue[0])
                    result.append(action)
                else:

                    previousValue = result[0] # Keep previous value. Minimax
                    nextValue = miniMax(gameState.generateSuccessor(agent, action), nextAgent, depth)

                    #comprovem que els seguents siguin millors.
                    
                    #Pacman MAX
                    if agent == self.index:
                        if nextValue[0] > previousValue:
                            result[0] = nextValue[0]
                            result[1] = action

                    #Ghost MIN
                    else:
                        if nextValue[0] < previousValue:
                            result[0] = nextValue[0]
                            result[1] = action
                            
            return result
        
        #comencem l'algorisme amb el gameState per defecte, profunditat 0 i l'index de pacman.
        return miniMax(gameState, self.index, 0)[1]
        
class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
          
          Es igual que el minmax pero guardes dos enters que 
        """
        
        def alphabeta(gameState,agent,depth,a,b):
            result = []

            if not gameState.getLegalActions(agent) or depth == self.depth:
                return self.evaluationFunction(gameState),0

            if agent == gameState.getNumAgents() - 1:
                depth += 1

            """---------------------------
                    Calcular nextAgent
            ---------------------------"""

            if agent == gameState.getNumAgents() - 1:
                nextAgent = self.index
            else:
                nextAgent = agent + 1

            for action in gameState.getLegalActions(agent):
                if not result:
                    nextValue = alphabeta(gameState.generateSuccessor(agent, action), nextAgent, depth, a, b)

                    result.append(nextValue[0])
                    result.append(action)

                    #canvi significatiu: el valor que l'algorisme usara per poda es el minim/maxim entre el que te i a, depenent si fantasmes o pacman
                    if agent == self.index:
                        a = max(result[0],a)
                    else:
                        b = min(result[0],b)
                else:
                    #comprovem si minmax es millor que els anteriors. Si ho es no evaluem certs nodes.
                    if result[0] > b and agent == self.index:
                        return result

                    if result[0] < a and agent != self.index:
                        return result

                    previousValue = result[0] # Keep previous value
                    nextValue = alphabeta(gameState.generateSuccessor(agent, action), nextAgent, depth, a, b)

                    if agent == self.index:
                        if nextValue[0] > previousValue:
                            result[0] = nextValue[0]
                            result[1] = action

                            a = max(result[0],a)

                    else:
                        if nextValue[0] < previousValue:
                            result[0] = nextValue[0]
                            result[1] = action

                            b = min(result[0],b)
            return result

        # Cridem alphabeta depth 0 i -inf i inf per aplha i beta respectivament.
        return alphabeta(gameState, self.index, 0, -float("inf"), float("inf"))[1]
        

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
          
          Fer que la poda alpha beta falli a posta a vegades o que
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

