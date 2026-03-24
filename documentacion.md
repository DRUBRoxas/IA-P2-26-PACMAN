# Documentación de la práctica 2: Búsqueda  
  
---  
Autores:  
* Manuel Sánchez Salazar - mss00048  
* Priscila Cubillas Solana - pcs00027  
---  
# Indice

```toc
```
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

## Documentación de la función depthFirstSearch (search.py)

### Resumen

La función depthFirstSearch (DFS) implementa el algoritmo de Búsqueda en Profundidad para un SearchProblem. Su objetivo es expandir siempre el nodo más profundo en el árbol de búsqueda actual, explorando un camino hasta el final antes de retroceder para explorar otras ramas.

### Planteamiento de la función

```python
depthFirstSearch(problem) -> List[Directions]
```

Misma explicación que en el anterior, problem es la instancia de SearchProblem y devuelve una lista de acciones.

### Comportamiento del algoritmo

1. Se obtiene el estado inicial con `problem.getStartState()`
2.  Estructuras auxiliares:
	* `nodos_finales`: una pila (LIFO - Last In, First Out) instanciada con `util.Stack()`. Almacena tuplas compuestas por el estado actual y la lista de acciones tomadas hasta ese punto `(estado_actual,acciones)`
	* `casillas_visitadas`: Un conjunto set para registrar las casillas en las que ya has estado.
	* `movimientos_totales`: Para llevar la cuenta de movimientos que han tenido que realizarse.
3. Se inserta el estado inicial en la pila, junto a una lista de acciones vacía
4. En cada iteración del while:
	* Se extrae el último elemento insertado mediante el `pop()` 
	* Si el estado extraido es final, la búsqueda termina y se imprimen los datos por consola (Caso Base), además de devolver la lista de archivos
	* Si el estado no ha sido visitado, se añade a `casillas_visitadas` y se obtienen sus sucesores.
	* Por cada sucesor que no esté en `casillas_visitadas`, se incrementa el contador de movimientos, se actualiza el camino y se introduce en la pila para ser explorado después.
5. Si la pila se vacia y no se ha encontrado meta, la función devuelve una lista vacía

### Notas de implementación

* El uso de la estructura de datos util.Stack() es el núcleo del algoritmo, ya que dicta el comportamiento de la Búsqueda en profundidad. De hecho, si cambiásemos util.Stack() por util.Queue(), haríamos el BSF sin tener que tocar ni una linea más de código (Esto se ha implementado en la práctica también).
* El DFS no garantiza encontrar el camino más corto o de menor coste, devuelve el primer camino que encuentra hacia la meta.
### Ejemplo de uso  

Nosotros hemos llamado al explorador DoraLaExploradoradfs:
```python
class DoraLaExploradoradfs(SearchAgent):  
    def __init__(self):  
        super().__init__(fn='dfs')
```

Para probar la exploración en el mazo grande:
```bash
python pacman.py -k 0 --pacman DoraLaExploradoradfs --layout bigMaze -z 0.5
```


### Tabla de análisis de desempeño

| **Laberinto**    | **Coste Acumulado (Longitud)** | **Total de Movimientos Explorados** | **Número de Casillas Únicas Visitadas** | **Ratio de Repetición** | **Tiempo Total de Ejecución** | **Eficiencia** |
| ---------------- | ------------------------------ | ----------------------------------- | --------------------------------------- | ----------------------- | ----------------------------- | -------------- |
| testClassic      | 23                             | 37                                  | 23                                      | 1.61                    | 0.035350                      | 100%           |
| medium Classic   | 55                             | 91                                  | 74                                      | 1.23                    | 0.048977                      | 74,32%         |
| original Classic | 141                            | 241                                 | 211                                     | 1.14                    | 0.077237                      | 66.82%         |
### Fórmulas de Evaluación

Para analizar el rendimiento de los algoritmos, hemos utilizado las siguientes métricas:

**1. Ratio de Repetición (Redundancia del mapa)**
Mide el factor de ramificación útil, es decir, cuántos estados válidos se generan de media por cada casilla pisada. Un valor más alto indica un entorno con más intersecciones u opciones abiertas.

$$Ratio\ de\ Repetición = \frac{\text{Movimientos totales explorados}}{\text{Nodos únicos visitados}}$$

**2. Eficiencia de la Búsqueda (Certeza del algoritmo)**
Evalúa la proporción del esfuerzo del algoritmo que resultó útil para la ruta final, penalizando los rodeos y la exploración de caminos sin salida.

$$Eficiencia\ (\%) = \left( \frac{\text{Longitud del camino final}}{\text{Nodos únicos visitados}} \right) \times 100$$
### Entorno MultiAgente
En el entorno multiagente, la gran mayoría de veces, el agente acaba perdiendo ante los fantasmas que se cruzan en su camino, ya que el agente está diseñado para estar en un entorno mono-agente, este genera un problema y muere la mayoría de las veces. La estrategia de búsqueda y la toma de decisiones se queda igual ya que no tiene en cuenta a los otros agentes. En cuanto a la capacidad de alcanzar el objetivo, se ve muy afectado ya que en las ejecuciones realizadas (más o menos 10 por laberinto) no llegaba en más del 70% de las veces.


## Documentación de la función aStarSearch (search.py)

### Resumen
La función `aStarSearch` (A\*) implementa un algoritmo de búsqueda informada para un `SearchProblem`. Su objetivo es encontrar el camino óptimo hacia la meta evaluando los nodos mediante la función f(n)=g(n)+h(n), donde g(n) es el coste real acumulado desde el inicio, y h(n) es el coste estimado hasta la meta devuelto por una función heurística. A\* siempre expande primero el nodo con el menor coste total estimado f(n).

### Planteamiento de la función

Python

```
aStarSearch(problem, heuristic=nullHeuristic) -> List[Directions]
```

Misma explicación que en el anterior, `problem` es la instancia de `SearchProblem` y devuelve una lista de acciones. Adicionalmente, recibe el parámetro `heuristic`, que es la función que guiará la búsqueda.

### Comportamiento del algoritmo
1. Se obtiene el estado inicial con `problem.getStartState()` y se calcula su prioridad inicial evaluando la heurística.
2. Estructuras:
	* `nodos_finales`: Una cola de prioridad instanciada con `util.PriorityQueue()`. Almacena tuplas igual que antes, pero además contiene la prioridad.
	* `casillas_visitadas`: igual que el anterior
	* `movimientos_totales` igual que el anterior.
3. Se inserta el estado inicial en la cola de prioridad junto a una lista de acciones vacía y un coste de 0, asignándole como prioridad el valor heurístico.
4. En cada iteración del `while`:
	1. Se extrae el elemento con menor prioridad insertado mediante el `pop()`
	2. Si el estado extraido es final, la busqueda termina.
	3. Si el estado no ha sido visitado, se añade a `casillas_visitadas` y se obtienen los sucesores
	4. Por cada sucesor que no esté en `casillas_visitadas`, se incrementa el contador de movimientos, se actualiza el camino, se calcula su nuevo coste real g(n) sumando el coste del paso, y se introduce en la cola de prioridad. Su prioridad para ordenarse en la cola será la suma de su nuevo coste real más su valor heurístico: $f(n)=g(n)+h(n)$.
5. Si la cola de prioridad se vacía y no ha encontrado meta, se devuelve una lista vacía

### Notas de implementación

* El uso de `util.PriorityQueue()` permite ordenar automáticamente los nodos en base a su prioridad.
* A diferencia del DFS, A\* sí garantiza el camino más corto o de menor coste, siempre y cuando la heurística sea válida.
* Se ha usado la heurística Manhattan.
### Ejemplo de uso  

Nosotros hemos llamado al explorador DoraLaExploradorabae:
```python
class DoraLaExploradorabae(SearchAgent):  
    def __init__(self):  
        # Le pasamos la manhattan ya creada por el proyecto  
        super().__init__(fn='astar', heuristic='manhattanHeuristic')
```

Para probar la exploración en el mazo grande:
```bash
python pacman.py -k 0 --pacman DoraLaExploradorabae --layout bigMaze -z 0.5
```


### Tabla de análisis de desempeño

| **Laberinto**    | **Coste Acumulado (Longitud)** | **Total de Movimientos Explorados** | **Número de Casillas Únicas Visitadas** | **Ratio de Repetición** | **Tiempo Total de Ejecución** | **Eficiencia** |
| ---------------- | ------------------------------ | ----------------------------------- | --------------------------------------- | ----------------------- | ----------------------------- | -------------- |
| testClassic      | 7                              | 14                                  | 7                                       | 2.00                    | 0.028600                      | 100%           |
| medium Classic   | 17                             | 42                                  | 33                                      | 1.27                    | 0.062251                      | 51.32%         |
| original Classic | 37                             | 86                                  | 75                                      | 1.15                    | 0.045996                      | 49.33%         |
> Se asumen las mismas formulas que en el DFS
### Entorno MultiAgente

En el entorno multiagente, esta vez el fantasma pierde menos veces, ya que al ir directo al sitio, recorre menos casillas y la probabilidad de encontrarse con un fantasma baja bastante.
En lo demás tenemos el mismo problema que el DFS, no está preparado para un entorno multiagente.

## Comparativa de los algoritmos de búsqueda

| **Laberinto**       | **Algoritmo** | **Coste (Longitud)** | **Casillas Visitadas** | **Tiempo (s)** | **Eficiencia** |
| ------------------- | ------------- | -------------------- | ---------------------- | -------------- | -------------- |
| **testClassic**     | DFS           | 23                   | 23                     | 0.035          | 100%           |
|                     | A*            | 7                    | 7                      | 0.028          | 100%           |
| **mediumClassic**   | DFS           | 55                   | 74                     | 0.048          | 74.32%         |
|                     | A*            | 17                   | 33                     | 0.062          | 51.32%         |
| **originalClassic** | DFS           | 141                  | 211                    | 0.077          | 66.82%         |
|                     | A*            | 37                   | 75                     | 0.045          | 49.33%         |

* **Calidad de la solución**: A\* demuestra que la solución que devuelve es óptima ya que si vemos el coste de la solución, el A\* es mucho más bajo que el DFS
* **Espacio de búsqueda**: El espacio de búsqueda en A\* es muy inferior, ya que una busqueda es informada y la otra no, por lo que el A\* debe mirar menos casillas.
* **Tiempos de Ejecucion:** Aunque internamente A\* realiza operaciones más complejas, el hecho de que explore muchos menos nodos hace que sea mucho más rapido.
* **Sobre la Eficiencia**: Si observamos los porcentajes, DFS parece tener mayor eficiencia en mapas grandes (66.82% frente al 49.33% de A\*). Esto se debe a cómo calculamos la eficiencia, el camino del DFS es tán largo, que abarca casi todas las casillas que visitó. A\* sin embargo, explora las casillas para asegurar matemáticamente que la ruta es efectivamente la más corta.  A\* Sacrifica eficiencia para garantizar la solución óptima.

## Dificultades y posibles soluciones

La principal debilidad de estos algoritmos de búsqueda es que son algoritmos de planificación estática, es decir, no tienen en cuenta un entorno multiagente, y se calculan antes de realizar las acciones.

Ambos algoritmos calculan la ruta desde el estado inicial hasta la meta antes de dar el primer paso. Esto vuelve al agente incapaz de ver los problemas que pueden surgir en el camino.

### Posibles soluciones

#### A. Estrategia de Evasión de Fantasmas

La solución más inmediata es darle al agente la capacidad de reaccionar o replanificar su ruta. En lugar de calcular toda la ruta y ejecutarla a ciegas, el agente debería recalcular el árbol cada vez que da un paso (o cuando detecte a un fantasma a cierta distancia siguiendo Manhattan) 

Ejemplo de implementación:
* Si un fantasma entra en un "area de alerta", el agente cambia a modo escape, donde se aleja del fantasma o recalcula una ruta evitando las casillas cercanas al mismo.

#### B. Adaptación de la Búsqueda para evitar zonas peligrosas

Solución para el A\*, si una casilla pasa por un camino del fantasma, el coste aumenta mucho, haciendo ese camino menos viable para la búsqueda.

Implementación:
* Se modifica la función de sucesores para que el coste de pisar una casilla dependa de la proximidad de los fantasmas. Si una casilla está a 1 paso de un fantasma el coste pasa a ser 1000 en vez de uno, por ejemplo.

#### C. Uso de heurísticas mejoradas en BAE para optimizar rutas

Se puede utilizar una heurística compuesta. en lugar de que h(n) devuelva solo la distancia hacia la meta, podría evaluar un balance entre acercarse a la meta y alejarse de los fantasmas. 

