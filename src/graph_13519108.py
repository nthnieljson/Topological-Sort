from vertex_13519108 import Vertex


class Graph:
    # data structure to represent a graph
    # a collection of vertex is called vertices, which is represented by an array
    # the vertices in the graph has a unique name

    def __init__(this):
        # default constructor for graph, the default vertices is empty

        this.vertices = []

    def isEmpty(this):
        # check if the graph is empty or not

        return len(this.vertices) == 0

    def vertexExist(this, name):
        # check if a vertex exist in the graph

        exist = False

        for vertex in this.vertices:

            exist = exist or (vertix.name == name)

        return exist

    def addVertex(this, vertex):
        # add new vertex to the graph, construct a new vertex

        this.vertices.append(vertex)

    def findVertex(this, name):
        # return a vertex with that have the same name
        # it is assumed that the vertex exist in the graph

        for vertex in this.vertices:

            if vertex.name == name:

                return vertex

    def findVerticesConnected(this, vertexOut):
        # return an array of vertex that has an vertex in with the same name
        # return an empty array if none are found

        return [
            vertex
            for vertex in this.vertices
            if (vertexOut.name in vertex.inVertexNames)
        ]

    def addVertexConnection(this, vertexIn, vertexOutName):
        # add a connection from a vertex to another vertex
        # the connection have direction,
        # which is diffrentiate with vertexIn and vertexOut
        # the vertexIn and vertexOut is assumed always exist in the graph

        vertexIn.addInVertex(vertexOutName)

    def removeVertices(this, verticesTarget):
        # remove a collection of vertex from the vertices
        # assumed that the vertex exist in the graph
        # adjust also with the vertex that is connected
        # adjusting by deleting the in vertex for the vertex connected

        for vertexTarget in verticesTarget:

            verticesConected = this.findVerticesConnected(vertexTarget)

            # remove the connected vertex
            for vertex in verticesConected:

                vertex.deleteInVertex(vertexTarget)

            # remove the vertex
            this.vertices = [
                vertex for vertex in this.vertices if (vertex.name != vertexTarget.name)
            ]

    def findZeroInDegreeVertices(this):
        # find all vertices that have zero in degree
        # return in a form of array of vertex

        return [vertex for vertex in this.vertices if (vertex.inDegree == 0)]

    def printAll(this):
        # print all vertices along with the info of the vertices

        for vertex in this.vertices:

            vertex.printInfo()
            print()
