from deap import base, creator, tools, algorithms
import random
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

if __name__ == "__main__":
    main()