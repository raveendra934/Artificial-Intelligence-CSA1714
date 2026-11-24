
import random

N = 8

def fitness(chromosome):
    conflicts = 0

    for i in range(N):
        for j in range(i + 1, N):
            if abs(chromosome[i] - chromosome[j]) == abs(i - j):
                conflicts += 1

    return 28 - conflicts

def crossover(p1, p2):
    point = random.randint(1, N - 1)
    child = p1[:point] + p2[point:]
    return child

def mutation(chromosome):
    pos = random.randint(0, N - 1)
    chromosome[pos] = random.randint(0, N - 1)
    return chromosome

population = [
    random.sample(range(N), N) for _ in range(10)
]

for generation in range(1000):
    population.sort(key=fitness, reverse=True)

    best = population[0]

    if fitness(best) == 28:
        break

    print("Generation:", generation)
    print("Chromosome:", best)
    print("Fitness:", fitness(best))

    new_population = population[:2]

    while len(new_population) < 10:
        p1, p2 = random.sample(population[:5], 2)

        child = crossover(p1, p2)
        print("Crossover:", child)

        if random.random() < 0.3:
            child = mutation(child)
            print("Mutation:", child)

        new_population.append(child)

    population = new_population

print("\nFinal Solution:")
print("Chromosome:", best)
print("Fitness:", fitness(best))
