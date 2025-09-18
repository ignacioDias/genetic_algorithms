import random

INDIVIDUAL_SIZE = 10
POPULATION_SIZE = 20
ITERATIONS = 40
CXPB = 0.8 # Probabilidad de cruce
MUTPB = 0.05 # Probabilidad de mutación

def generate_initial_population():
    return [generate_individual() for _ in range(POPULATION_SIZE)]

def generate_individual():
    return [random.randint(0, 1) for _ in range(INDIVIDUAL_SIZE)]

def selection(population):
    k = 3
    selected = []
    for _ in range(POPULATION_SIZE):
        aspirants = random.sample(population, k)
        best = max(aspirants, key=fitness)
        selected.append(best)
    return selected

def fitness(individual):
    return sum(individual)

def crossover(individual1, individual2):
    if random.random() < CXPB:
        point = random.randint(1, INDIVIDUAL_SIZE - 1)
        return individual1[:point] + individual2[point:], individual2[:point] + individual1[point:]
    return individual1, individual2

def mutate(individual):
    for i in range(INDIVIDUAL_SIZE):
        if random.random() < MUTPB:
            individual[i] = 1 - individual[i]
    return individual

def genetic_algorithm():
    population = generate_initial_population()
    for gen in range(ITERATIONS):
        population.sort(key=fitness, reverse=True)
        print(f"Gen {gen}: Mejor = {population[0]} Fitness = {fitness(population[0])}")
        next_gen = []
        selected = selection(population)
        for i in range(0, POPULATION_SIZE, 2):
            offspring1, offspring2 = crossover(selected[i], selected[i+1])
            next_gen.append(mutate(offspring1))
            next_gen.append(mutate(offspring2))
        population = next_gen
    return max(population, key=fitness)


best = genetic_algorithm()
print(f"Mejor individuo encontrado: {best}, Fitness = {fitness(best)}")