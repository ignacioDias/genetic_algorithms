import random

RGB_MAX = 3
POPULATION_SIZE = 20
ITERATIONS = 80
CXPB = 0.8 # Probabilidad de cruce
MUTPB = 0.05 # Probabilidad de mutación
COLOR = (0, 0, 255) #RED DE INDEPENDENCIA

def generate_initial_population():
    return [generate_individual() for _ in range(POPULATION_SIZE)]

def generate_individual():
    return [random.randint(0, 255) for _ in range(RGB_MAX)]

def selection(population):
    k = 3
    selected = []
    for _ in range(POPULATION_SIZE):
        aspirants = random.sample(population, k)
        best = min(aspirants, key=fitness)
        selected.append(best)
    return selected

def fitness(individual):
    return abs(individual[0] - COLOR[0]) + abs(individual[1] - COLOR[1]) + abs(individual[2] - COLOR[2])

def crossover(individual1, individual2):
    if random.random() < CXPB:
        point = random.randint(1, RGB_MAX - 1)
        return individual1[:point] + individual2[point:], individual2[:point] + individual1[point:]
    return individual1, individual2

def mutate(individual):
    for i in range(RGB_MAX):
        if random.random() < MUTPB:
            individual[i] = random.randint(0, 255)
    return individual

def genetic_algorithm():
    population = generate_initial_population()
    for gen in range(ITERATIONS):
        population.sort(key=fitness, reverse=False)
        print_rgb(population[0])
        print(f"Gen {gen}: Mejor = {population[0]} Fitness = {fitness(population[0])}")
        next_gen = []
        selected = selection(population)
        for i in range(0, POPULATION_SIZE, 2):
            offspring1, offspring2 = crossover(selected[i], selected[i+1])
            next_gen.append(mutate(offspring1))
            next_gen.append(mutate(offspring2))
        population = next_gen
    return min(population, key=fitness)

def print_rgb(rgb):
    r, g, b = rgb
    print(f"\033[48;2;{r};{g};{b}m   \033[0m", rgb)

best = genetic_algorithm()
print(f"Mejor individuo encontrado: {best}, Fitness = {fitness(best)}")