import os
from graph import Graph
from vertex import Vertex
from files import readInputFile, convertToGraph
from solutions import getClassPlan
from utils import printTitle, printClassPlan


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
