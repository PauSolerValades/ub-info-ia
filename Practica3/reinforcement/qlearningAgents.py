# -*- coding: utf-8 -*-
# qlearningAgents.py
# ------------------
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


from game import *
from learningAgents import ReinforcementAgent
from featureExtractors import *

import random,util,math

class QLearningAgent(ReinforcementAgent):
    """
      Q-Learning Agent

      Functions you should fill in:
        - computeValueFromQValues (Q1)
            - Break ties randomly for better behavior with random.choice()
            - Actions your agent HAS NOT SEEN before have a Q-value of 0.
            - Actions your agent HAS SEEN have a negative Q-value
        - computeActionFromQValues (Q1)
            - Only acces Q-values with getQValue
        - getQValue (Q1)
            - Only acces Q-values with getQValue
        - getAction
        - update

      Instance variables you have access to
        - self.epsilon (exploration prob)
        - self.alpha (learning rate)
        - self.discount (discount rate)

      Functions you should use
        - self.getLegalActions(state)
          which returns legal actions for a state
    """
    def __init__(self, **args):
        "You can initialize Q-values here..."
        ReinforcementAgent.__init__(self, **args)

        self.q_values = util.Counter()

    def getQValue(self, state, action):
        """
          Returns Q(state,action)
          Should return 0.0 if we have never seen a state
          or the Q node value otherwise
        """

        if not self.q_values.has_key((state, action)):
            self.q_values[(state, action)] = 0.0 #si no hem vist l'estat el posem al diccionari i el posem a 0

        return self.q_values[(state, action)]


    def computeValueFromQValues(self, state):
        """
          Returns max_action Q(state,action)
          where the max is over legal actions.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return a value of 0.0.

          ESCULL EL VALOR DEL DICCIONARI Q_VALUES
        """
        accions_legals = self.getLegalActions(state)

        if not accions_legals:
            return 0.0

        q_list = [self.getQValue(state, action) for action in accions_legals]


        """
        Se de sobres que aquesta manera no es la mes optima ja que recorres diveses vegades la llista, pero no em sembla massa rellevant ja que la llista no sera mai massa gran
        """

        m = max(q_list)


        #PERQUE PUTES SI POSES UN RANDOM QUE ES COM HA D'ANAR NO PUTES PASSA L'AUTRGRADER SUICIDEU-VOS BERKELEY
        largest = [j for i, j in enumerate(q_list) if j == m]

        return random.choice(largest)


    def computeActionFromQValues(self, state):
        """
          Compute the best action to take in a state.  Note that if there
          are no legal actions, which is the case at the terminal state,
          you should return None.

          ACTUALITZA EL VALOR DEL DICCIONARI
        """
        "*** YOUR CODE HERE ***"

        accions_legals = self.getLegalActions(state)

        if not accions_legals:
            return None

        q_actions = util.Counter()
        for action in accions_legals:
            q_actions[action] = self.getQValue(state, action)

        #Counter is numpy, so i can use argMax :)

        return q_actions.argMax()

    def getAction(self, state):
        """
          Compute the action to take in the current state.  With
          probability self.epsilon, we should take a random action and
          take the best policy action otherwise.  Note that if there are
          no legal actions, which is the case at the terminal state, you
          should choose None as the action.

          HINT: You might want to use util.flipCoin(prob)
          HINT: To pick randomly from a list, use random.choice(list)
        """
        # Pick Action
        legalActions = self.getLegalActions(state)
        action = None
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

        return action

    def update(self, state, action, nextState, reward):
        """
          The parent class calls this to observe a
          state = action => nextState and reward transition.
          You should do your Q-Value update here

          NOTE: You should never call this function,
          it will be called on your behalf
        """

        aprox = reward + self.discount * self.computeValueFromQValues(nextState)
        self.q_values[(state, action)] = (1 - self.alpha)*self.getQValue(state, action) + self.alpha*aprox


    def getPolicy(self, state):
        return self.computeActionFromQValues(state)

    def getValue(self, state):
        return self.computeValueFromQValues(state)


class PacmanQAgent(QLearningAgent):
    "Exactly the same as QLearningAgent, but with different default parameters"

    def __init__(self, epsilon=0.05,gamma=0.8,alpha=0.2, numTraining=0, **args):
        """
        These default parameters can be changed from the pacman.py command line.
        For example, to change the exploration rate, try:
            python pacman.py -p PacmanQLearningAgent -a epsilon=0.1

        alpha    - learning rate
        epsilon  - exploration rate
        gamma    - discount factor
        numTraining - number of training episodes, i.e. no learning after these many episodes
        """
        args['epsilon'] = epsilon
        args['gamma'] = gamma
        args['alpha'] = alpha
        args['numTraining'] = numTraining
        self.index = 0  # This is always Pacman
        QLearningAgent.__init__(self, **args)

    def getAction(self, state):
        """
        Simply calls the getAction method of QLearningAgent and then
        informs parent of action for Pacman.  Do not change or remove this
        method.
        """
        action = QLearningAgent.getAction(self,state)
        self.doAction(state,action)
        return action
