points = ['A', 'B', 'C', 'D', 'E','F','G','H']

graph = {'A': [['B',2], ['D',3]], 
         'B': [['A',2], ['D',2],['E',8],['F',10],['C',7]],
         'C': [['B',7], ['F',1]],
         'D': [['A',3], ['B',2],['E',7], ['G',3]],
         'E': [['D',7], ['B',8],['F',3], ['G',6], ['H',1]],
         'F': [['C',1], ['B',10], ['E',3], ['H',5]],
         'G': [['E',6], ['D',3], ['H',1]],
         'H': [['G',1], ['E',1], ['F',5]],
         }

## punkt , czy odwiedzony? , waga , poprzednik
def starterTable(points):
    starter = {letter: [False, float('inf'), '-'] for letter in points}
    return starter

table = starterTable(points)

def markGivenPointAsExplored(point):
    table[point][0] = True

def inputDistanceToGivenPoint(point, distance):
    table[point][1] = distance

def inputPredecessor(point, predecessor):
    table[point][2] = predecessor

def markDistanceAndPredecessorToNeighbors(point):
    neighbors = graph[point]
    currentDistance = table[point][1]
    for neighbor in neighbors:
        neighborSign = neighbor[0]
        distanceToNeighbor = neighbor[1]
        distance = currentDistance + distanceToNeighbor 
        if(distance < table[neighborSign][1]):
            inputDistanceToGivenPoint(neighborSign, distance)
            inputPredecessor(neighborSign, point)

def returnUnexploredPoints():
    listOfUnexploredPoints = []
    for sign in table:
        if not table[sign][0]: 
            listOfUnexploredPoints.append(sign) 
    return listOfUnexploredPoints

def returnUnexploredPointWithTheShortestDistance():
    unexploredPoints = returnUnexploredPoints()
    distances = [table[sign][1] for sign in unexploredPoints]
    lowestDistance = min(distances)
    indexOfLowest = distances.index(lowestDistance)
    return unexploredPoints[indexOfLowest]
    
def visit(point):
    markGivenPointAsExplored(point)
    markDistanceAndPredecessorToNeighbors(point)


def everyPointHasBeenVisited():
    for sign in table:
        if table[sign][0] == False:
            return False
    return True

def findShortestWaysToEveryPoint(starterPoint):
    inputDistanceToGivenPoint(starterPoint, 0)
    visit(starterPoint)
    nextPoint = returnUnexploredPointWithTheShortestDistance()
    while True:
        visit(nextPoint)
        if(everyPointHasBeenVisited() or table[nextPoint][1] == float('inf')):
            break
        else:
            nextPoint = returnUnexploredPointWithTheShortestDistance()


def returnShortestWayBetweenGivenPoints(startPoint, endPoint):
    findShortestWaysToEveryPoint(startPoint)
    if(table[endPoint][1]==float('inf')):
        print('Nie da się dojść do punktu ', endPoint, ' z punktu ', startPoint)
    predecessors = []
    predecessors.append(endPoint)
    predecessor = table[endPoint][2]
    predecessors.append(predecessor)
    while predecessor != startPoint :
        predecessor = table[predecessor][2]
        predecessors.append(predecessor)
    print('Najkrótsza droga z ', startPoint, ' do ', endPoint, ' wynosi ', table[endPoint][1], 
          ' i jest ona postaci: ', ' --> '.join(predecessors[::-1]))

returnShortestWayBetweenGivenPoints('A','E')
# returnShortestWayBetweenGivenPoints('C','G')

