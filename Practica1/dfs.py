#axiò és un dfs que funciona, però falta gestionar les direccions
direccions=[]
while not aVisitar.isEmpty():
    nodeActual = aVisitar.pop()
    coordNode = nodeActual[0]
    dirNode = nodeActual[1]
         
    if coordNode in visitats: continue
    visitats.append(coordNode)

    direccions[coordNode]=dirNode
    for i in problem.getSuccessors(coordNode):
        aVisitar.push(i)

    if problem.isGoalState(coordNode):
        break
        
for i in visitats:
    direccions.append(i[1][1])
    
return direccions

