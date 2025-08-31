from deap import base, creator, tools, algorithms
import random

import numpy as np

INDIVIDUAL_SIZE = 3
COLOR = (10,255,32)
# 1. Crear clase de fitness y clase de individuo
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)
# 2. Toolbox: atributos, individuos, población
toolbox = base.Toolbox()
# Atributo binario: 0 o 1
toolbox.register("attr_bool", random.randint, 0, 255)
# Un individuo es una lista de 20 bits
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, INDIVIDUAL_SIZE)
# Una población es una lista de individuos
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
# 3. Función de evaluación: 

def eval_color(individual):
    return (abs(individual[0] - COLOR[0]) + abs(individual[1] - COLOR[1]) + abs(individual[2] - COLOR[2]),)   # <-- tupla
def mut_rgb(individual):
    idx = random.randint(0, INDIVIDUAL_SIZE - 1)
    # Asignar un nuevo valor aleatorio entre 0 y 255
    individual[idx] = random.randint(0, 255)
    return (individual,)
toolbox.register("evaluate", eval_color)
# 4. Operadores genéticos
toolbox.register("mate", tools.cxOnePoint) # Cruce de 1 punto
toolbox.register("mutate", mut_rgb)
toolbox.register("select", tools.selTournament, tournsize=3) # Selección torneo
# 5. Algoritmo principal


def main():
    random.seed(42)
    pop = toolbox.population(n=400) # Población inicial
    algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.2, ngen=20, verbose=True)
    
    stats = tools.Statistics(lambda ind: ind.fitness.values[0])
    stats.register("avg", np.mean)
    stats.register("std", np.std)
    stats.register("min", np.min)
    stats.register("max", np.max)

    hof = tools.HallOfFame(1)  # guarda el mejor histórico

    pop, log = algorithms.eaSimple(pop, toolbox,
                                cxpb=0.5, mutpb=0.2,
                                ngen=20, stats=stats,
                                halloffame=hof, verbose=True)

    print("Mejor individuo:", hof[0], "Fitness:", hof[0].fitness.values[0])
    print_rgb(hof[0])

def print_rgb(rgb):
    r, g, b = rgb
    print(f"\033[48;2;{r};{g};{b}m   \033[0m", rgb)
if __name__ == "__main__":
    main()