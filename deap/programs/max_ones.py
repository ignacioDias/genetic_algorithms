from deap import base, creator, tools, algorithms
import random

import numpy as np
# 1. Crear clase de fitness y clase de individuo
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)
# 2. Toolbox: atributos, individuos, población
toolbox = base.Toolbox()
# Atributo binario: 0 o 1
toolbox.register("attr_bool", random.randint, 0, 1)
# Un individuo es una lista de 20 bits
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, 20)
# Una población es una lista de individuos
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
# 3. Función de evaluación: contar 1's
def eval_maxones(individual):
    return sum(individual),
toolbox.register("evaluate", eval_maxones)
# 4. Operadores genéticos
toolbox.register("mate", tools.cxTwoPoint) # Cruce de 2 puntos
toolbox.register("mutate", tools.mutFlipBit, indpb=0.05) # Mutación bit flip
toolbox.register("select", tools.selTournament, tournsize=3) # Selección torneo
# 5. Algoritmo principal
def main():
    random.seed(42)
    pop = toolbox.population(n=50) # Población inicial
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

if __name__ == "__main__":
    main()
    