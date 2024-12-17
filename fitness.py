
def getFitness(value: int) -> int:
    if value <= 27:
        return 27 - value
    else: 
        return value - 27 
