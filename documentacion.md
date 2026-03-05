# Documentación de la práctica 2: Búsqueda  
  
---  
Autores:  
* Manuel Sánchez Salazar - mss00048  
* Priscila Cubillas Solana - pcs00027  
---  
  
## Documentación de la función exploration (search.py)  
  
### Resumen  

La función `exploration` implementa una estrategia de exploración para un `SearchProblem`. Su objetivo es visitar (tocar) todas las casillas alcanzables al menos una vez recorriendo el espacio de estados y retrocediendo cuando se llega a un callejón sin salida.  
  
### Planteamiento de la función  

```python
exploration(problem) -> List[Directions]  
```

- `problem`: instancia de `SearchProblem` que proporciona los métodos `getStartState()`, `isGoalState(state)` y `getSuccessors(state)`.  
- Devuelve una lista de acciones (`Directions`) que representan los movimientos que debe realizar el agente para explorar el entorno siguiendo la estrategia implementada.  
  
### Comportamiento y algoritmo 

1. Se obtiene el estado inicial con `problem.getStartState()` y se marca como visitado.  
2. Estructuras auxiliares para el algoritmo:  
   - `casillas_visitadas`: conjunto de casillas visitadas.  
   - `pilaEstados`: pila de estados anteriores (para la vuelta atrás).  
   - `pilaMovimientos`: pila de movimientos realizados para llegar a los estados en `pilaEstados`.  
   - `pilaTotal`: lista de acciones que se devuelve al final con todos los movimientos realizados.  
3. En cada iteración, se consulta los sucesores:
   - Si encuentra un sucesor no visitado, avanza a ese estado (al primero que encuentre). marca como visitado,guarda el estado actual y la acción usada, añade la acción a `pilaTotal` y continúa desde el nuevo estado.  
   - Si no encuentra sucesores no visitados (callejón), retrocede si hay movimientos en la pila: saca de la pila el último estado y la última acción, calcula la acción inversa mediante `Directions.REVERSE[ultima_accion]`, la añade a `pilaTotal` y actualiza el `estado_actual` con el estado al retroceder.  
4. La exploración termina cuando:  
   - `problem.isGoalState(estado_actual)` es True (Se ha encontrado el objetivo) o no quedan acciones en la pila para retroceder (se han agotado todas las rutas posibles).  
1. La función devuelve `pilaTotal`, la secuencia de acciones que recorren el espacio según la estrategia.  
  
### Notas de implementación  

- La estrategia que he seguido es una búsqueda basada en visitar todas las casillas posibles. Siempre coge la primera disponible hasta que no encuentra otro camino y retrocede.
- Al retroceder se usan las entradas de `Directions.REVERSE` para generar la acción inversa a la que nos llevó al callejón 
### Consideraciones  respecto a la implementación

- Si el estado inicial ya satisface `isGoalState`, la función terminará sin generar movimientos (o podría no entrar en el bucle) y devolverá la lista de acciones acumuladas hasta entonces.  
- Si hay ciclos en el laberinto, el conjunto `casillas_visitadas` evita bucles infinitos.  
  
### Ejemplo de uso  

Nosotros hemos llamado al explorador DoraLaExploradora:
```python
class DoraLaExploradora(SearchAgent):  
    def __init__(self):  
        super().__init__(fn='exp')
```

Para probar la exploración en el mazo grande:
```bash
python pacman.py -k 0 --pacman DoraLaExploradora --layout bigMaze -z 0.5
```

### Tabla de análisis de desempeño

| Laberinto  | Coste Acumulado | Total de Pasos | Numero de Casillas Exploradas | Ratio de Repetición |
| ---------- | --------------- | -------------- | ----------------------------- | ------------------- |
| smallMaze  | 76              | 76             | 47                            | 1.6170              |
| mediumMaze | 41              | 41             | 42                            | 0.9762              |
| BigMaze    | 612             | 612            | 401                           | 1.5261              |

