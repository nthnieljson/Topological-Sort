from graph_13519108 import Graph
from vertex_13519108 import Vertex


def getClassPlan(g):
    # return an array of array of string which represent the optimal plan
    # optimal plan are based of the prerequisites of each class

    classGraph = g

    classPlan = []

    while not classGraph.isEmpty():

        # find all the zero degree vertices that we need to take this semester
        zeroInDegreeVertices = classGraph.findZeroInDegreeVertices()

        # remove all the zero in degree vertices from the graph
        classGraph.removeVertices(zeroInDegreeVertices)

        # add the class to the current semester in the class plan
        currentSemester = []
        for vertex in zeroInDegreeVertices:

            currentSemester.append(vertex.name)

        classPlan.append(currentSemester)

    return classPlan
