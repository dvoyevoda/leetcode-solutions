class Solution:
    def judgeCircle(self, moves: str) -> bool:
        coordinates = [0,0]
        for move in moves:
            if move == "L":
                coordinates[0] -= 1
            if move == "R":
                coordinates[0] += 1
            if move == "U":
                coordinates[1] += 1
            if move == "D":
                coordinates[1] -= 1
        if coordinates[0] == 0 and coordinates[1] == 0:
            return True
        return False