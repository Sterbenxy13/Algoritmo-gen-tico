
from random import randint

import fitness

class Individual:

    def __generateBinary(self, numberOfGenes: int) -> str:
        result = ""

        for d in range(numberOfGenes):
            result += str(randint(0, 1))

        return result

    def __convertDecimalToBinary(self) -> str:

        result = ""

        powerOfTwo = 0

        while self.__decimalValue - (2 ** (powerOfTwo + 1)) >= 0:
            powerOfTwo += 1

        decimal = self.__decimalValue

        while powerOfTwo >= 0:
            if decimal - (2 ** powerOfTwo) >= 0:
                result += "1"
                decimal -= (2 ** powerOfTwo)
            else:
                result += "0"

            if decimal == 0:
                break

            powerOfTwo -= 1

        while len(result) < self.__numberOfGenes:
            result = "0" + result
        
        return result

    def __convertBinaryToDecimal(self) -> int:
        result: int = 0

        powerOfTwo: int = len(self.__binaryValue) - 1

        for i in self.__binaryValue:
            result += int(i) * (2 ** (powerOfTwo))
            powerOfTwo -= 1

        return result

    def __init__(self, numberOfGenes: int, **kwargs) -> None:

        self.__numberOfGenes = numberOfGenes

        if "decimal" in kwargs:
            self.__decimalValue = kwargs["decimal"]
            self.__binaryValue = self.__convertDecimalToBinary()
            
        else:
            self.__binaryValue = kwargs["binary"] if "binary" in kwargs else self.__generateBinary(numberOfGenes)
            self.__decimalValue = self.__convertBinaryToDecimal()


        self.__fitness = fitness.getFitness(self.__decimalValue)

    def getDecimalValue(self) -> int:
        return self.__decimalValue
    
    def getBinaryValue(self) -> str:
        return self.__binaryValue
    
    def getFitness(self) -> int:
        return self.__fitness
    
    def getFGene(self) -> str:
        return "".join([self.__binaryValue[i] for i in range(len(self.__binaryValue) // 2)])
    
    def getLGene(self) -> str:
        return "".join([self.__binaryValue[i] for i in range(
            (len(self.__binaryValue) // 2), len(self.__binaryValue)
            )])
    
    def __len__(self) -> int:
        return len(self.__binaryValue)





def generatePopulation(numberOfDigits, NumberOfIndividuals):
    result = []

    for i in range(NumberOfIndividuals):
        result.append(Individual(numberOfDigits, True))

    return result


'''
@overload
    def __init__(self, decimal: int) -> None:
        self.__binaryValue = self.__convertDecimalToBinary()
        self.__decimalValue = decimal
        self.__fitness = fitness.getFitness(self.__decimalValue)

    @overload
    def _(self, binary: str) -> None:
        self.__binaryValue = binary
        self.__decimalValue = self.__convertBinaryToDecimal()
        self.__fitness = fitness.getFitness(self.__decimalValue)
'''



