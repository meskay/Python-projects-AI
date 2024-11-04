graph = {
    'A':['T','B'], # 'starting poingt' = [points connecting to the starting point]
    'T':['C','E'],
    'E':['G','D'],
    'B':['H'],
    'H':['F']
}

def bfs(graph, start, goal):
    visited = []                            #the points visited in order (without repetetion)
    queue = [[start]]                       #outter [] for the queue and inner [] are for the 'A'
    while queue:                            #while queue is not empty
        path = queue.pop(0)                 #choose the path on the left in the queue
        node = path[-1]                     #gets the last value on the list of the path
        if node in visited:                 #checks if node was already visited
            continue                        #skips the whole process to avoid repeating it with the same node
        visited.append(node)                #adds the current node to "visited"
        if node == goal:                    #checks if the current node is the goal
            return path                     #returns the final result after the goal is met
        else:
            adjNodes = graph.get(node,[])   #puts the values of the possible movements in adjNodes and if an adjacent node is not found it leaves it as []
            for node2 in adjNodes:          
                newPath = path.copy()       #we make a copy of the path so we can build different paths with the same start at the same time
                newPath.append(node2)       #creates the paths
                queue.append(newPath)       #adds the new paths to the queue

def dfs(graph, start, goal):
    visited = []                            
    queue = [[start]]                      
    while queue:                            
        path = queue.pop(0)                #same exact process but it takes the path on the right in the queue instead       
        node = path[-1]                    
        if node in visited:                 
            continue                        
        visited.append(node)                
        if node == goal:                    
            return path                     
        else:
            adjNodes = graph.get(node,[])  
            for node2 in adjNodes:          
                newPath = path.copy()       
                newPath.append(node2)       
                queue.append(newPath)

print(bfs(graph,'A','F'))
print(dfs(graph,'A','F'))
