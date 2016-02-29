from MyTake.src.chapter9.adjacencyList import Graph


def dfs(currentVert):
    currentVert.setVisited()
    print("Visited: " + str(currentVert.getVertexID()))
    for nbr in currentVert.getConnections():
        if not nbr.isVisited:
            dfs(nbr)


def DFSTraversal(G):
    for vertex in G:
        if not vertex.isVisited():
            dfs(vertex)


def dfsWithVisited(currentVert, visited):
    visited[currentVert.getVertexID()] = True  # mark the visited node
    print("traversal: " + currentVert.getVertexID())
    for nbr in currentVert.getConnections():  # take a neighbouring node 
        if nbr.getVertexID() not in visited:  # condition to check whether the neighbour node is already visited
            dfsWithVisited(nbr, visited)  # recursively traverse the neighbouring node


def DFSTraversalWithVisited(G):
    visited = {}  # Dictionary to mark the visited nodes 
    for currentVert in G:  # G contains vertex objects
        if currentVert.getVertexID()  not in visited:  # Start traversing from the root node only if its not visited
            dfsWithVisited(currentVert, visited)  # For a connected graph this is called only once
    return visited


if __name__ == '__main__':
    from pprint import pprint

    G = Graph()
    G.addVertex('a')
    G.addVertex('b')
    G.addVertex('c')
    G.addVertex('d')
    G.addVertex('e')
    G.addVertex('f')
    G.addEdge('a', 'b', 1)
    G.addEdge('a', 'c', 1)
    G.addEdge('b', 'd', 1)
    G.addEdge('b', 'e', 1)
    G.addEdge('c', 'd', 1)
    G.addEdge('c', 'e', 1)
    G.addEdge('d', 'e', 1)
    G.addEdge('e', 'a', 1)
    print('Graph data:')
    pprint(G.getEdges())

    print(DFSTraversalWithVisited(G))
