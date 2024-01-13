import graphviz
points = ['A', 'B', 'C', 'D', 'E','F','G','H', 'I', 'J']

graph = { 'A': [['B',2], ['D',3]], 
         'B': [['A',2], ['D',2],['E',8],['F',10],['C',7]],
         'C': [['B',7], ['F',1]],
         'D': [['A',3], ['B',2],['E',7], ['G',3]],
         'E': [['D',7], ['B',8],['F',3], ['G',6], ['H',1]],
         'F': [['C',1], ['B',10], ['E',3], ['H',5]],
         'G': [['E',6], ['D',3], ['H',1]],
         'H': [['G',1], ['E',1], ['F',5]],
         'I': [['J',3]],
         'J': [['I',3]],
         
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
    return [sign for sign in table if not table[sign][0]]


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

def find_index_of_path(graph, node_A, node_B):
    if node_A in graph and node_B in graph:
        edges_of_A = graph[node_A]
        for i, edge in enumerate(edges_of_A):
            if edge[0] == node_B:
                return i
    return -1

def all_conns(data, path):
    result = []
    for i in range(len(path)-1):
        index = find_index_of_path(data, path[i],path[i+1])
        result.append([path[i],path[i+1],data[path[i]][index][1]])
    for node, edges in data.items():
        for edge in edges:
            if [node, edge[0], edge[1]] not in result and [edge[0], node, edge[1]] not in result:
                result.append([node, edge[0], edge[1]])
    return result

def all_conns_greenOrBlack(data, path):
    result = []
    cons = all_conns(data, path)
    for i in range(len(cons)):
        if i < len(path)-1:
            result.append([cons[i][0],cons[i][1],cons[i][2],True])
        else:
            result.append([cons[i][0],cons[i][1],cons[i][2],False])
    return result

def draw_graph(data, path, info):
    conns = all_conns_greenOrBlack(data, path)
    dot = graphviz.Digraph('G', filename='graph', format='pdf', graph_attr={'rankdir': 'LR'})
    for conn in conns:
        if conn[3] == True :
            color = 'green'
        else:
            color = 'black'
        dot.edge(conn[0],conn[1],label=str(conn[2]),dir='both',color = color)
    dot.attr(label=info)
    dot.render('graph', format='png', cleanup=True)
    dot.view('graph')

predecessors = []

def returnShortestWayBetweenGivenPoints(startPoint, endPoint):
    findShortestWaysToEveryPoint(startPoint)        
    predecessors.append(endPoint)
    predecessor = table[endPoint][2]
    predecessors.append(predecessor)
    if predecessor == '-':
        print('Nie da się dojść do punktu ', endPoint, ' z punktu ', startPoint)
    else:
        while predecessor != startPoint :
            predecessor = table[predecessor][2]
            predecessors.append(predecessor)
            message = f"Najkrótsza droga z {startPoint} do {endPoint} wynosi {table[endPoint][1]} i jest ona postaci: {'-'.join(predecessors[::-1])}"
            draw_graph(graph,predecessors, message)
    

returnShortestWayBetweenGivenPoints('A','E')
# returnShortestWayBetweenGivenPoints('C','G')
# returnShortestWayBetweenGivenPoints('C','J')
# returnShortestWayBetweenGivenPoints('I','J')






        

