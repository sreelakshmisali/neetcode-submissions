class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def isRepeatedBox():
            for i in range(0,9,3):
                for j in range(0,9,3):
                    visited=set()

                    for x in range(i, i+3):
                        for y in range(j, j+3):

                            value = board[x][y]

                            if value == ".":
                                continue
                            if value in visited:
                                return False
                            visited.add(value)

            return True

        def isRepeatingRow():
            for row in board:
                visited = set()

                for value in row:
                    if value == ".":
                        continue
                    if value in visited:
                        return False

                    visited.add(value)
            return True

        def isRepeatingCol():
            for col in range(9):
                visited = set()

                for row in range(9):
                    value = board[row][col]

                    if value == ".":
                        continue

                    if value in visited:
                        return False

                    visited.add(value)
            return True

        if not isRepeatingRow():
            return False

        if not isRepeatingCol():
            return False
        
        if not isRepeatedBox():
            return False

        return True
        