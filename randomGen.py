import random
from dNA import dNA

class randomGen():

    def genDNA(self, size, percentPick):
        dNA = ''
        for idx in range(0, size):
            randNumber = random.randrange(0, 100, 1)
            if(randNumber > percentPick):
                dNA += '0'
            else:
                dNA += '1'
        return dNA
            
    def genGeneration(self, sizeOfGen, sizeOfDNA, percentPick):
        dNAstr = ''
        gen = []
        for idx in range(0, sizeOfGen):
            dNAstr = self.genDNA(sizeOfDNA, percentPick)
            dNALoad = dNA()
            dNALoad.setDNA(dNAstr)
            gen.append(dNALoad)
        
        return gen