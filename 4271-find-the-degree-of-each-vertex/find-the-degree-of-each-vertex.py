class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        degreeList = []
        for vertex in matrix:
            degree = 0
            for edge in vertex:
                if edge == 1:
                    degree += 1
            degreeList.append(degree)

        return degreeList