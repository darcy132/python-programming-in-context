from createCentroids import *
from createClusters import *
from readFile import *
from edulidD import *

def main(dataFile):
    examDict = readFile(dataFile)
    examCentroids = createCentroids(5,examDict)
    createClusterss(5,examCentroids,examDict,3)

if __name__ == "__main__":
    main('./chapter_7/cs150exams.txt')
    