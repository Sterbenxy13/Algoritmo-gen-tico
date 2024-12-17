
from Population import Population

from Individual import Individual

def massiveTest(population: Population) -> None:

    avpop = population.getPopulationBin()

    for i in range(50):

        if avpop == population.getPopulationBin():
            print("population: ", population.getPopulationBin())
            print("Decimal Values: ", population.getPopulationDec())
            print("Fitness: ", [i.getFitness() for i in population.getPopulation()])

            print("-----")

        population.reproduce()

        if avpop == population.getPopulationBin() and i != 0:
            print("gen: ", i + 1)
            break
        

        avpop = population.getPopulationBin()
        
    else:
        print("gen: ", 50)


#p = Population(6, 10)

# ngen = 5

# p = Population(ngen, 0)

# dec = [
#     13,
#     27,
#     15,
#     21
# ]

# p.importPopulation([Individual(5, decimal = i) for i in dec])

# print([i.getBinaryValue() for i in (p.getPopulation())])
        
p = Population(8, 100)

massiveTest(p)









