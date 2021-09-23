

class fitnessAssessor():
    itemRating = []
    itemLBS = []
    def __init__(self):
        f = open("data.txt")
        data = f.readlines()
        for line in data:
            rating, lbs = line.split()
            self.itemRating.append(round(float(rating.strip()), 1))
            self.itemLBS.append(round(float(lbs.strip()), 1))
        f.close()

    def fitnessScore(self, dNA):
        fitnessScore = 0.0
        totalLBS = 0.0
        if len(dNA) == len(self.itemRating):
            for idx in range(0, len(dNA)):
                if dNA[idx] == '1':
                    fitnessScore += self.itemRating[idx]
                    totalLBS += self.itemLBS[idx]
        if totalLBS > 500:
            fitnessScore = 1.0
        return round(fitnessScore, 1), round(totalLBS, 1)