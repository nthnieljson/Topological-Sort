class Vertex:
    # name
    # inDegree
    # inVertexNames

    def __init__(this, name):
        # default vertex constructor with inDegree is 0 and no inVertex yet

        this.name = name
        this.inDegree = 0
        this.inVertexNames = []

    def addInVertex(this, name):
        # method to add vertex that goes in to the current vertex

        this.inVertexNames.append(name)
        this.inDegree += 1

    def deleteInVertex(this, vertex):
        # method to delete a vertex that goes in to the current vertex
        # will check first if the in vertex did really goes in to the current vertex
        # if found, it will delete and decrement the inDegree, if not then it will stays the same

        if vertex.name in this.inVertexNames:

            this.inVertexNames.remove(vertex.name)
            this.inDegree -= 1

    def printInfo(this):

        print(f"name = {this.name}")
        print(f"in degree = {this.inDegree}")

        for name in this.inVertexNames:
            print(f"- {name}")
