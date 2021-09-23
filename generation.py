from dNA import dNA
import random

class Generation():
    
    def __init__(self):
        self.MAXFIT = dNA()
        self.AVGFIT = 0
        self.population = []

    def l1normalization(self):
        totFitScore = 0
        if len(self.population) == 0:
            print('Err: L1 normalization called with 0 population.')
        for idx in range(0, len(self.population)):
            totFitScore += self.population[idx].fitness
        for idx in range(0, len(self.population)):
            self.population[idx].setL1(self.population[idx].fitness/totFitScore)
        self.sortL1()
        for idx in range(0, len(self.population)):
            if idx == 0:
                self.population[idx].setCumL1(self.population[idx].l1Norm)
            else:
                self.population[idx].setCumL1(self.population[idx-1].cumL1 + self.population[idx].l1Norm)

    def sortL1(self):
        self.population.sort(key=dNA.getL1)

    def getDNAL1(self):
        randomSelection = random.random()
        for idx in range(0, len(self.population)):
            if randomSelection <= self.population[idx].cumL1:
                return self.population[idx]
        
        print('we never picked a DNA strand')

    def sexxyTime(self, gen):
        for idx in range(0, len(gen.population)):
            daddy = gen.getDNAL1()
            mommy = gen.getDNAL1()
            newDNA = daddy.split(mommy.chromes, random.randrange(0, len(daddy.chromes), 1))
            tempDNA = dNA()
            tempDNA.setDNA(newDNA)
            tempDNA.mutate()
            self.population.append(tempDNA)

    def reset(self):
        self.population.clear()
        self.MAXFIT = dNA()
        self.AVGFIT = 0
    
    def copyPop(self, pop):
        self.population = pop.copy()




            

