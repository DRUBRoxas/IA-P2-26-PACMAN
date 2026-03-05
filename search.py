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
from game import Directions
from typing import List

from util import Stack


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


def tinyMazeSearch(problem: SearchProblem) -> List[Directions]:
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    util.raiseNotDefined()


def breadthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


def uniformCostSearch(problem: SearchProblem) -> List[Directions]:
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


def nullHeuristic(state, problem=None) -> float:
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic) -> List[Directions]:
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


def exploration(problem):
    """
    Esta función implementa una estrategia de exploración. La idea es tocar todas las casillas al menos una vez.
    """
    # Se obtiene el estado inicial del problema, se inicializa un conjunto para las casillas visitadas y una lista para los movimientos realizados.
    estado_inicial = problem.getStartState()
    estado_actual = estado_inicial
    casillas_visitadas = set()
    pilaMovimientos = list()
    pilaEstados = list()
    pilaTotal = list()

    casillas_visitadas.add(estado_inicial)

    while not problem.isGoalState(estado_actual):
        sucesores= problem.getSuccessors(estado_actual)
        movimiento_realizado = False

        for sucesor,accion,coste in sucesores:
            if sucesor not in casillas_visitadas:
                # Avanzamos
                casillas_visitadas.add(sucesor)
                pilaEstados.append(estado_actual)
                pilaMovimientos.append(accion)
                pilaTotal.append(accion)

                estado_actual=sucesor
                movimiento_realizado=True
                print("Moviendo a estado:", estado_actual, "con acción:", accion)
                break
        if not movimiento_realizado:
            if len(pilaMovimientos) > 0:
                estado_actual=pilaEstados.pop()
                ultima_accion=pilaMovimientos.pop()
                accion_inversa = Directions.REVERSE[ultima_accion]
                pilaTotal.append(accion_inversa)
                print("Retrocediendo a estado:", estado_actual, "con acción inversa:", accion_inversa)
            else:
                print("Exploración completa. No hay más movimientos posibles.")
                break

    # Imprimir Estadisticas
    print("Número total de movimientos realizados:", len(pilaTotal))
    print("Número de casillas unicas visitadas:", len(casillas_visitadas))
    print("Ratio de repetición de casillas:", len(pilaTotal) / len(casillas_visitadas) if len(casillas_visitadas) > 0 else float('inf'))

    return pilaTotal
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
exp = exploration
