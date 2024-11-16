import random

#in this code each run will give you a different solution. If a solution is not displayed, please rerun

def createBoard():                                                #creates a random board configuration
    board = [random.randint(0, numberOfQueens-1) for _ in range(numberOfQueens)]
    return board

def calculateFitness(board):                                      #calculates fitness of a board configuration
    fitness = 0
    for i in range(numberOfQueens):
        for j in range(i+1, numberOfQueens):
            if board[i] == board[j] or abs(i - j) == abs(board[i] - board[j]):
                fitness += 1
    return fitness

def crossover(parent1, parent2):                                   #crossover operation
    crossoverPoint = random.randint(1, numberOfQueens-1)
    child1 = parent1[:crossoverPoint] + parent2[crossoverPoint:]
    child2 = parent2[:crossoverPoint] + parent1[crossoverPoint:]
    return child1, child2

def mutate(board):                                                 #mutation operation
    index = random.randint(0, numberOfQueens-1)
    newPos = random.randint(0, numberOfQueens-1)
    board[index] = newPos
    return board

def geneticAlgorithm(populationSize, generations):                 #genetic algorithm
    population = [createBoard() for _ in range(populationSize)]

    for _ in range(generations):
        parents = random.sample(population, 2)                     #select parents for crossover

        child1, child2 = crossover(parents[0], parents[1])         #performs crossover and mutation
        child1 = mutate(child1)
        child2 = mutate(child2)

        population.extend([child1, child2])                        #adds children to population

        population.sort(key=lambda x: calculateFitness(x))         #sorts population by fitness and keep top population_size individuals
        population = population[:populationSize]

        if calculateFitness(population[0]) == 0:                   #checks for solution
            return population[0]                                   #if no solution was found nothing will be retured

def drawBoard(board):                                              #represents the auto generated answer by drawing the board with queens
    for row in range(numberOfQueens):
        for col in range(numberOfQueens):
            if board[col] == row:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()

def main():                                                        #main function
    solution = geneticAlgorithm(populationSize=100, generations=1000)
    if solution:
        print("Solution found:")
        drawBoard(solution)
    else:
        print("No solution found.")

numberOfQueens = 8
main()
