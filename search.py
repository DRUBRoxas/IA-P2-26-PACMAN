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
    # Vamos a guardar tuplas de (estado,lista de acciones)
    nodos_finales = util.Stack()

    estado_inicial = problem.getStartState()
    nodos_finales.push((estado_inicial,[]))

    # Para evitar repetidos
    casillas_visitadas = set()
    movimientos_totales=0

    while not nodos_finales.isEmpty():
        # Sacamos el último elemento
        estado_actual, acciones = nodos_finales.pop()

        if problem.isGoalState(estado_actual):
            print("--- DFS ---")
            print("Número total de movimientos explorados: ", movimientos_totales)
            print("Número de casillas únicas visitadas: ", len(casillas_visitadas))
            ratio = movimientos_totales / len(casillas_visitadas) if len(casillas_visitadas) > 0 else 0
            eficiencia = (len(acciones) / len(casillas_visitadas)) * 100 if len(casillas_visitadas) > 0 else 0
            print("Eficiencia del camino encontrado: {:.2f}%".format(eficiencia))
            print("Ratio de repetición de casillas: {:.2f}".format(ratio))
            print("Longitud del camino final encontrado:", len(acciones))
            return acciones

        if estado_actual not in casillas_visitadas:
            casillas_visitadas.add(estado_actual)
            sucesores = problem.getSuccessors(estado_actual)

            for sucesor,accion,coste in sucesores:
                if sucesor not in casillas_visitadas:
                    #Creamos el nuevo camino añadiendo la acción actual
                    movimientos_totales += 1
                    camino_hijo=acciones + [accion]
                    nodos_finales.push((sucesor,camino_hijo))
    # Devolución de la pila vacía si no hay meta
    return []

def breadthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """Search the shallowest nodes in the search tree first."""
    # Vamos a guardar tuplas de (estado,lista de acciones)
    nodos_finales = util.Queue()

    estado_inicial = problem.getStartState()
    nodos_finales.push((estado_inicial,[]))

    # Para evitar repetidos
    casillas_visitadas = set()
    movimientos_totales=0

    while not nodos_finales.isEmpty():
        # Sacamos el último elemento
        estado_actual, acciones = nodos_finales.pop()

        if problem.isGoalState(estado_actual):
            print("--- DFS ---")
            print("Número total de movimientos explorados: ", movimientos_totales)
            print("Número de casillas únicas visitadas: ", len(casillas_visitadas))
            ratio = movimientos_totales / len(casillas_visitadas) if len(casillas_visitadas) > 0 else 0
            eficiencia = (len(acciones) / len(casillas_visitadas)) * 100 if len(casillas_visitadas) > 0 else 0
            print("Eficiencia del camino encontrado: {:.2f}%".format(eficiencia))
            print("Ratio de repetición de casillas: {:.2f}".format(ratio))
            print("Longitud del camino óptimo encontrado:", len(acciones))
            return acciones

        if estado_actual not in casillas_visitadas:
            casillas_visitadas.add(estado_actual)
            sucesores = problem.getSuccessors(estado_actual)

            for sucesor,accion,coste in sucesores:
                if sucesor not in casillas_visitadas:
                    #Creamos el nuevo camino añadiendo la acción actual
                    movimientos_totales += 1
                    camino_hijo=acciones + [accion]
                    nodos_finales.push((sucesor,camino_hijo))
    # Devolución de la pila vacía si no hay meta
    return []


def uniformCostSearch(problem: SearchProblem) -> List[Directions]:
    """Search the node of least total cost first."""
    frontera = util.PriorityQueue()
    estado_inicial = problem.getStartState()

    # Cada nodo: (estado, acciones_desde_inicio, coste_acumulado)
    frontera.push((estado_inicial, [], 0), 0)
    mejor_coste = {estado_inicial: 0}

    while not frontera.isEmpty():
        estado_actual, acciones, coste_actual = frontera.pop()

        # Si este nodo ya no es el mejor conocido para su estado, lo ignoramos.
        if coste_actual > mejor_coste.get(estado_actual, float('inf')):
            continue

        if problem.isGoalState(estado_actual):
            return acciones

        for sucesor, accion, coste_paso in problem.getSuccessors(estado_actual):
            nuevo_coste = coste_actual + coste_paso
            if nuevo_coste < mejor_coste.get(sucesor, float('inf')):
                mejor_coste[sucesor] = nuevo_coste
                frontera.push((sucesor, acciones + [accion], nuevo_coste), nuevo_coste)

    return []

def nullHeuristic(state, problem=None) -> float:
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic) -> List[Directions]:
    """Search the node that has the lowest combined cost and heuristic first."""
    # Usamos cola de prioridad
    nodos_finales = util.PriorityQueue()
    estado_inicial = problem.getStartState()

    prioridad_inicial= 0 + heuristic(estado_inicial,problem)
    nodos_finales.push((estado_inicial,[],0),prioridad_inicial)

    casillas_visitadas = set()
    movimientos_totales = 0
    while not nodos_finales.isEmpty():
        estado_actual, acciones, coste = nodos_finales.pop()

        #Si es meta, imprimimos
        if problem.isGoalState(estado_actual):
            print("--- A* ---")
            print("Número total de movimientos explorados:", movimientos_totales)
            print("Número de casillas únicas visitadas:", len(casillas_visitadas))
            ratio = movimientos_totales / len(casillas_visitadas) if len(casillas_visitadas) > 0 else 0
            eficiencia = (len(acciones) / len(casillas_visitadas)) * 100 if len(casillas_visitadas) > 0 else 0
            print("Eficiencia del camino encontrado: {:.2f}%".format(eficiencia))
            print("Ratio de repetición de casillas: {:.2f}".format(ratio))
            print("Longitud del camino óptimo encontrado:", len(acciones))
            print("Coste real total del camino:", coste)
            return acciones
        if estado_actual not in casillas_visitadas:
            casillas_visitadas.add(estado_actual)
            sucesores = problem.getSuccessors(estado_actual)
            for sucesor, accion, coste_sucesor in sucesores:
                if sucesor not in casillas_visitadas:
                    movimientos_totales += 1
                    # Coste desde el inicial hasta el sucesor
                    nuevo_coste = coste + coste_sucesor
                    camino_hijo = acciones + [accion]
                    # f(n) = g(n) + h(n)
                    prioridad = nuevo_coste + heuristic(sucesor, problem)
                    nodos_finales.push((sucesor, camino_hijo, nuevo_coste), prioridad)
    return []



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


def greedySearch(problem: SearchProblem, heuristic=nullHeuristic) -> List[Directions]:
    """Busca el nodo con el menor valor heurísitco."""
    frontera = util.PriorityQueue()
    estado_inicial = problem.getStartState()

    # En Greedy, la prioridad inicial es exclusivamente el valor heurístico h(n)
    prioridad_inicial = heuristic(estado_inicial, problem)

    frontera.push((estado_inicial, []), prioridad_inicial)

    casillas_visitadas = set()
    movimientos_totales = 0

    while not frontera.isEmpty():
        estado_actual, acciones = frontera.pop()

        if problem.isGoalState(estado_actual):
            print("--- Greedy Best-First Search ---")
            print("Número total de movimientos explorados:", movimientos_totales)
            print("Número de casillas únicas visitadas:", len(casillas_visitadas))
            ratio = movimientos_totales / len(casillas_visitadas) if len(casillas_visitadas) > 0 else 0
            eficiencia = (len(acciones) / len(casillas_visitadas)) * 100 if len(casillas_visitadas) > 0 else 0
            print("Eficiencia del camino encontrado: {:.2f}%".format(eficiencia))
            print("Ratio de repetición de casillas: {:.2f}".format(ratio))
            print("Longitud del camino encontrado:", len(acciones))
            # Nota: Greedy no garantiza el camino óptimo, por eso decimos "camino encontrado"
            return acciones

        if estado_actual not in casillas_visitadas:
            casillas_visitadas.add(estado_actual)
            sucesores = problem.getSuccessors(estado_actual)

            for sucesor, accion, coste_sucesor in sucesores:
                if sucesor not in casillas_visitadas:
                    movimientos_totales += 1
                    camino_hijo = acciones + [accion]
                    # f(n) = h(n)
                    prioridad = heuristic(sucesor, problem)
                    frontera.push((sucesor, camino_hijo), prioridad)

    return []


def iterativeDeepeningSearch(problem: SearchProblem) -> List[Directions]:
    """
    Busca los nodos mas profundos con una profundiad limitada, incrementando el limite hasta encontrar la meta. Es una combinación de DFS y BFS.
    """
    def depthLimitedSearch(limit: int) -> List[Directions]:
        frontera = util.Stack()
        frontera.push((problem.getStartState(), []))

        visitados = {}

        while not frontera.isEmpty():
            estado_actual, acciones = frontera.pop()
            profundidad_actual = len(acciones)
            if problem.isGoalState(estado_actual):
                return acciones
            # Comprobamos si el estado ya fue visitado en una profundidad menor o igual
            if estado_actual in visitados and visitados[estado_actual] <= profundidad_actual:
                continue
            visitados[estado_actual] = profundidad_actual
            if profundidad_actual < limit:
                for sucesor, accion, coste in problem.getSuccessors(estado_actual):
                    camino_hijo = acciones + [accion]
                    frontera.push((sucesor, camino_hijo))

        return None
    # Bucle principal de IDDFS
    limite_profundidad = 0
    while True:
        resultado = depthLimitedSearch(limite_profundidad)
        if resultado is not None:  # Se encontró la meta
            return resultado
        limite_profundidad += 1


# Abreviaciones
iddfs = iterativeDeepeningSearch
greedy=greedySearch
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
exp = exploration
