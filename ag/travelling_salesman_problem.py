import random
from graph import Graph
POPULATION_SIZE = 20
ITERATIONS = 4000
CXPB = 0.8 # Probabilidad de cruce
MUTPB = 0.05 # Probabilidad de mutación

GRAPH = Graph()

# Triángulo base
GRAPH.insert_path(0, 1, 5)
GRAPH.insert_path(1, 2, 2)
GRAPH.insert_path(0, 2, 1)

# Columna central hacia el destino
GRAPH.insert_path(2, 3, 1)
GRAPH.insert_path(3, 5, 1)

# Camino alternativo por 4
GRAPH.insert_path(3, 4, 1)
GRAPH.insert_path(4, 5, 1)

# Ramas extra para crear más variantes
GRAPH.insert_path(2, 6, 2)
GRAPH.insert_path(6, 5, 4)
GRAPH.insert_path(1, 6, 3)

GRAPH.insert_path(0, 7, 4)
GRAPH.insert_path(7, 3, 2)
GRAPH.insert_path(7, 4, 5)

GRAPH.insert_path(2, 8, 3)
GRAPH.insert_path(8, 5, 2)

GRAPH.starting_node = 0
GRAPH.final_node = 5

STARTING_POINT = GRAPH.starting_node
FINISH_POINT = GRAPH.final_node
INDIVIDUAL_SIZE = len(GRAPH.nodes) + 1

def genetic_algorithm():
    population = generate_initial_population()
    for gen in range(ITERATIONS):
        population.sort(key=fitness, reverse=False)
        print(f"Gen {gen}: Mejor = {population[0]} Fitness = {fitness(population[0])}")
        next_gen = []
        selected = selection(population)
        for i in range(0, POPULATION_SIZE, 2):
            offspring1, offspring2 = crossover(selected[i], selected[i+1])
            next_gen.append(mutate(offspring1))
            next_gen.append(mutate(offspring2))
        population = next_gen
    return min(population, key=fitness)

def generate_initial_population():
    return [generate_individual() for _ in range(POPULATION_SIZE)]

def generate_individual():
    nodes = GRAPH.nodes[:]                # copia de los nodos
    extra = random.choice(nodes)          # elegimos un nodo para repetir
    nodes.append(extra)                   # lo agregamos de nuevo
    random.shuffle(nodes)                 # mezclamos todo
    return nodes

def fitness(individual):
    if individual[0] != STARTING_POINT:
        return 100000
    if individual[-1] != STARTING_POINT:
        return 10000
    marked = set()
    starting_node_appareances = 0
    for i in range(INDIVIDUAL_SIZE - 1):
        u = individual[i]
        v = individual[i + 1]
        if u == STARTING_POINT:
            starting_node_appareances += 1
            if starting_node_appareances > 2:
                return 10000
        if not GRAPH.is_neighbour(u, v):
            return 10000
        if u in marked and u != GRAPH.starting_node:
            return 10000
        else:
            marked.add(u)
    return GRAPH.calculate_cost(individual)

def selection(population):
    k = 3
    selected = []
    for _ in range(POPULATION_SIZE):
        aspirants = random.sample(population, k)
        best = min(aspirants, key=fitness)
        selected.append(best)
    return selected

def crossover(individual1, individual2):
    if random.random() < CXPB:
        point = random.randint(1, INDIVIDUAL_SIZE - 1)
        return individual1[:point] + individual2[point:], individual2[:point] + individual1[point:]
    return individual1, individual2


def mutate(individual):
    if(random.random() < MUTPB):
        i = random.randint(0, INDIVIDUAL_SIZE - 1)
        j = random.randint(0, INDIVIDUAL_SIZE - 1)
        individual[i], individual[j] = individual[j], individual[i]
    return individual

genetic_algorithm()
#print(fitness([0, 7, 4, 3, 2, 8, 5, 6, 1, 0]))