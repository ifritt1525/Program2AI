import random

class dNA():
    def __init__(self):
        self.chromes = ''
        self.fitness = 0
        self.loadLBS = 0
        self.l1Norm = 0
        self.cumL1 = 0

    def setDNA(self, str):
        self.chromes = str
    
    def setFitness(self, number):
        self.fitness = number

    def setLoadLBS(self, number):
        self.loadLBS = number
    
    def setL1(self, number):
        self.l1Norm = number

    def getL1(self):
        return self.l1Norm
    
    def setCumL1(self, number):
        self.cumL1 = number

    def split(self, dNA, splitPoint):
        tempStr = ''
        if len(self.chromes) == len(dNA):
            for idx in range(0, len(dNA)):
                if idx < splitPoint:
                    tempStr += self.chromes[idx]
                else:
                    tempStr += dNA[idx]

        if len(tempStr) != len(dNA):
            print('Not enough chromes in DNA str')

        return tempStr

    def mutate(self):
        for idx in range(0, len(self.chromes)):
            rand = random.randrange(0, 10000, 1)
            if rand == 1:
                if self.chromes[idx] == '1':
                    self.chromes = self.chromes[:idx] + '0' + self.chromes[idx+1:]
                else:
                    self.chromes = self.chromes[:idx] + '1' + self.chromes[idx+1:]
            if len(self.chromes) != 400:
                print('ERROR MUTATED A dNA strand longer than 400 bits')
