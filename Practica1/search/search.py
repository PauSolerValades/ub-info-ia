# -*- coding: utf-8 -*-
#
# search.py
# ---------
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
    
    #axiò és un dfs que funciona, però falta gestionar les direccions
    
    """
    visitats = []
    aVisitar = util.Stack()
    aVisitar.push(problem.getStartState)
    direccions=[]
    
    while not aVisitar.isEmpty():
        nodeActual = aVisitar.pop()
        coordNode = nodeActual[0]
        dirNode = nodeActual[1]
            
        if coordNode in visitats: continue
        visitats.append(coordNode)

        direccions[coordNode]=dirNode
        for i in problem.getSuccessors(coordNode):
            aVisitar.push(i)

        if problem.isGoalState(coordNode):
            break
            
    for i in visitats:
        direccions.append(i[1][1])
        
    return direccions
    
    """
    
    aVisitar = util.Stack()
    visitats = []
    direccions = []
    startNode = (problem.getStartState(),visitats,direccions) #a cada node guardem TOTA la llista de direccions i tots els pares dels que venim, aixi quan trobem el node de desti nomes hem de retornar les direccions del mateix node.
    
    aVisitar.push(startNode)
    
    while not aVisitar.isEmpty():
        (node, visitats, direccions) = aVisitar.pop()
        
        if problem.isGoalState(node):
            return direccions
        
        for successor, direccio, cost in problem.getSuccessors(node) :
            if successor not in visitats:
                newNode = (successor, visitats+[successor], direccions+[direccio]) #es guarden dins de cada node
                aVisitar.push(newNode)
        
def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    
    #Com que no canviem la depth al explorar, no ens hem de guardar cada vistats dins de cada node, nomes fa falta tenir una llista general, ja que amb els pops ens assegurem ja que visitem la mateix depth.
    
    aVisitar = util.Queue()
    visitats = []
    direccions = []
    startNode = (problem.getStartState(),direccions) #a cada node guardem TOTA la llista de direccions i tots els pares dels que venim, aixi quan trobem el node de desti nomes hem de retornar les direccions del mateix node.
    
    aVisitar.push(startNode)
    
    while not aVisitar.isEmpty():
        (node, direccions) = aVisitar.pop()
        
        if problem.isGoalState(node):
            return direccions
        
        visitats.append(node);
        for successor, direccio, cost in problem.getSuccessors(node) :
            if successor not in visitats:
                visitats.append(successor);
                newNode = (successor, direccions+[direccio]) #es guarden dins de cada node
                aVisitar.push(newNode)

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
                
    aVisitar = util.PriorityQueue()
    visitats = []
    direccions = []
    costTotal = 0
    prediccio = 0+heuristic(problem.getStartState(), problem)
    # ((3,4), [west, south], 54) ()
    # (on soc, camí absolut, cost mínim per arribar)
    # Node = (Coordenades, Path, Prediction)
    startNode = (problem.getStartState(), direccions, costTotal) #a cada node guardem TOTA la llista de direccions i tots els pares dels que venim, aixi quan trobem el node de desti nomes hem de retornar les direccions del mateix node.
    
    aVisitar.push(startNode, prediccio)
    
    while not aVisitar.isEmpty():
        
        nodeCoord, direccions, costRecorregut = aVisitar.pop()
        
        if problem.isGoalState(nodeCoord):
            return direccions
        
        if nodeCoord in visitats: continue
    
        visitats.append(nodeCoord)
        
        for fillCoord, direccio, cost in problem.getSuccessors(nodeCoord):
            if fillCoord not in visitats:
                newNode = (fillCoord, direccions+[direccio],costRecorregut+cost) #es guarden dins de cada node
                aVisitar.push(newNode, costRecorregut + cost + heuristic(fillCoord,problem))

  


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
