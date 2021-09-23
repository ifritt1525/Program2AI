from dNA import dNA
from randomGen import randomGen
from fitnessAssessor import fitnessAssessor
from generation import Generation

bestDNA = dNA()
assessor = fitnessAssessor()
randGen = randomGen()
generation = Generation()
newGen = Generation()
percentPick = 5
genSize = 1000
dNASize = 400
genAvgFitRecord = []
generation.population = randGen.genGeneration(genSize, dNASize, percentPick)
keepGoing = True

of = open("output.txt", "a")
of.write('-----------------------------------------------------'+ '\n')
of.write('genSize: ' + str(genSize) + '   dNASize: '+ str(dNASize) + '   percentPicked: ' + str(percentPick) + '\n')
of.write('-----------------STARTING NEW RUN--------------------' + '\n')
#for gensToSim in range(0, 1000):
gensSimmed = 0
while keepGoing:
    gensSimmed += 1
    generationFITAVG = 0
    for idx in range(0, len(generation.population)):
        
        loadScore, loadLBS = assessor.fitnessScore(generation.population[idx].chromes)
        generation.population[idx].setFitness(loadScore)
        generation.population[idx].setLoadLBS(loadLBS)
                
        if loadScore > generation.MAXFIT.fitness:
            generation.MAXFIT = generation.population[idx]
        
        generationFITAVG += generation.population[idx].fitness
    generationFITAVG = round((generationFITAVG/len(generation.population)), 1)
    generation.AVGFIT = generationFITAVG
    genAvgFitRecord.append(generation.AVGFIT)
    if generation.MAXFIT.fitness > bestDNA.fitness:
        bestDNA = generation.MAXFIT

    generation.l1normalization()
    of.write('Generation #' + str(gensSimmed) + ' MaxFit: ' + str(generation.MAXFIT.fitness) + ' AvgFit: ' + str(generation.AVGFIT) + '\n')

    newGen.sexxyTime(generation)
    generation.reset()
    generation.copyPop(newGen.population)
    newGen.reset()
    if gensSimmed > 10:
        if genAvgFitRecord[gensSimmed - 10] < generationFITAVG:
            tempDif = generationFITAVG - genAvgFitRecord[gensSimmed - 10]
            onePercent = 0.01*genAvgFitRecord[gensSimmed - 10]
            if tempDif < onePercent:
                keepGoing = False

print('Best List Produced: (fScore = ' + str(bestDNA.fitness) + ')')
itemList = []
for idx in range(0, len(bestDNA.chromes)):
    if bestDNA.chromes[idx] == '1':
        itemList.append(str(idx))
print('Items picked:')
print(itemList)
of.write('Best List Produced: (fScore = ' + str(bestDNA.fitness) + ')' + '\n')
of.write(bestDNA.chromes + '\n')
of.close()