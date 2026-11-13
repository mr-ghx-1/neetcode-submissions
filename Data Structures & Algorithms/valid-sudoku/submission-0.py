class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # valid rows
        for i in board:
            tally = dict()
            for j in i:
                if j != ".":
                    if j not in tally:
                        tally[j] = 1
                    else:
                        return False
            # print(tally)

        # valid cols
        for i in range(0, 9):
            tally = dict()
            for j in board:
                if j[i] != ".":
                    if j[i] not in tally:
                        tally[j[i]] = 1
                    else:
                        return False
            # print(tally)

        # valid grids
        for k in range(0, 9):
            tally = dict()
            quot, rem = divmod(k, 3)
            for i in range(0, 3):
                for j in range(0, 3):
                    val = board[quot * 3 + i][rem * 3 + j]
                    if val != ".":
                        if val not in tally:
                            tally[val] = 1
                        else:
                            return False
            # print(tally)
        
        return True

