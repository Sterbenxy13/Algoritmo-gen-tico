
from Individual import Individual

class Population:

    def importPopulation(self, pop: list[Individual]):
        self.__individualsList = pop
        self.__size = len(pop)

    def __init__(self, numberOfGenes: int, numberOfIndividuals: int, ) -> None:
        self.__individualsList = [Individual(numberOfGenes) for i in range(numberOfIndividuals)]
        self.__size = numberOfIndividuals

        self.__numberOfGenes = numberOfGenes

    def __crossOver(self, pop: list[Individual],  index: int) -> str:
        return pop[index].getFGene() + pop[index * (-1) - 1].getLGene()

    def __sortIndividuals(self) -> list[Individual]: #bubble sort
        sortedList = self.__individualsList

        # Traverse through all sortedListay elements
        for i in range(self.__size):
            swapped = False
            
            for j in range(0, self.__size - i - 1):
                
                if sortedList[j].getFitness() > sortedList[j+1].getFitness():
                    sortedList[j], sortedList[j+1] = sortedList[j+1], sortedList[j]
                    swapped = True

            if (swapped == False):
                break

        return [sortedList[i] for i in range(self.__size // 2)]
        

    def __select(self) -> list[Individual]:

        return [i for i in self.__sortIndividuals()]

    def reproduce(self) -> None:

        fitnessPopulation = self.__select()

        #print("fitnesspop: ", [i.getBinaryValue() for i in self.__sortIndividuals()])

        for i in range(self.__size // 2):
            # individual[i] = i, -i
            self.__individualsList[i] = Individual(self.__numberOfGenes, binary =
                self.__crossOver(fitnessPopulation, i)
            )
            
            # individual[-i] = -i, i
            self.__individualsList[(i + 1) * (-1)] = Individual(self.__numberOfGenes, binary =
                self.__crossOver(fitnessPopulation, (i + 1) * (-1))
            )
            
    def getPopulation(self) -> list[Individual]:
        return [i for i in self.__individualsList]

    def getPopulationBin(self) -> list[str]:
        return [i.getBinaryValue() for i in self.__individualsList]
    
    def getPopulationDec(self) -> list[str]:
        return [i.getDecimalValue() for i in self.__individualsList]





