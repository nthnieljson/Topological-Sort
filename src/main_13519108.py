import os
from graph_13519108 import Graph
from vertex_13519108 import Vertex
from files_13519108 import readInputFile, convertToGraph
from solutions_13519108 import getClassPlan
from utils_13519108 import printTitle, printClassPlan


printTitle()

try:

    filename = str(input("Please input the filename: "))

    print()

    lines = readInputFile(filename)
    classGraph = convertToGraph(lines)
    classPlan = getClassPlan(classGraph)

    print("Your class plan :")
    print("-------------------")

    printClassPlan(classPlan)

except:

    print("Filename not found, please input an existing filename")
