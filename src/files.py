import os
from graph import Graph
from vertex import Vertex

TEST_CASE_DIRECTORY = "doc"


def readInputFile(filename):
    # read the input file and return an array of string (lines in the file)

    exactPath = f"{TEST_CASE_DIRECTORY}/{filename}"

    lines = []
    with open(exactPath) as f:

        lines = [line[:-2] for line in f.readlines()]

    return lines


def convertToGraph(lines):
    # convert the lines in the file into a graph format
    # the lines that is read is having a specific format

    graphResult = Graph()

    for line in lines:

        vertices = line.split(",")
        vertexIn = vertices[0]
        verticesOut = vertices[1:]

        newVertex = Vertex(vertexIn)

        for vertexOut in verticesOut:
            newVertex.addInVertex(vertexOut)

        graphResult.addVertex(newVertex)

    return graphResult
