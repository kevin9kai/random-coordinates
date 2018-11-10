import random

numberOfCoordiantes = 100

vertexOne = [0,0]
vetexTwo = [100,100]

newRandomCoordinateList = []

for x in range(numberOfCoordinates):
    newRandomCoordinate = [random.randint(vertexOne[0],vertexTwo[0]),random.randint(vertexOne[1],vertexTwo[1])]
    newRandomCoordinateList.append(newRandomCoordinate)
    
np.savetxt('RandomCoordinates.txt', newRandomCoordinateList, delimiter='\n')