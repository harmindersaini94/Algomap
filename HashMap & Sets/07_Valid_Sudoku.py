def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        """
        My Approach
        1. Initialize a dicy
        2. Loop on each row, for each row, Initialize the dict again to find duplicate
        3. Same loop thing on Column
        4. Same thing for each 3*3 grid
        """

        # Row Checking
        for row in board:
            r_set = set()
            #print(row)
            for i in row:
                if i == ".":
                    continue
                elif i in r_set:
                    return False
                else: r_set.add(i)

        #print("Hello")

        # Row Checking
        r_len = len(board)
        c_len = len(board[0])
        for c in range(c_len):
            c_set = set()
            for r in range(r_len):
                if board[r][c] == ".":
                    continue
                elif board[r][c] in c_set:
                    return False
                else: c_set.add(board[r][c])

        # 3X3 Checing
        # COl 0 1 2
        # Row 1-9
        r_len = len(board)

        grid = set()
        for r in range(r_len):
            if r < 3:
                for c in range(0,3):
                    if board[r][c] == ".":
                        continue
                    elif board[r][c] in grid:
                        return False
                    else: grid.add(board[r][c])

                if r == 2: grid = set()
            elif r < 6:
                for c in range(0,3):
                    if board[r][c] == ".":
                        continue
                    elif board[r][c] in grid:
                        return False
                    else: grid.add(board[r][c])

                if r == 5: grid = set()
            elif r >= 6:
                for c in range(0,3):
                    if board[r][c] == ".":
                        continue
                    elif board[r][c] in grid:
                        return False
                    else: grid.add(board[r][c])

        grid = set()
        for r in range(r_len):
            if r < 3:
                for c in range(3,6):
                    if board[r][c] == ".":
                        continue
                    elif board[r][c] in grid:
                        return False
                    else: grid.add(board[r][c])

                if r == 2: grid = set()
            elif r < 6:
                for c in range(3,6):
                    if board[r][c] == ".":
                        continue
                    elif board[r][c] in grid:
                        return False
                    else: grid.add(board[r][c])

                if r == 5: grid = set()
            elif r >= 6:
                for c in range(3,6):
                    if board[r][c] == ".":
                        continue
                    elif board[r][c] in grid:
                        return False
                    else: grid.add(board[r][c])

        grid = set()
        for r in range(r_len):
            if r < 3:
                for c in range(6,9):
                    if board[r][c] == ".":
                        continue
                    elif board[r][c] in grid:
                        return False
                    else: grid.add(board[r][c])

                if r == 2: grid = set()
            elif r < 6:
                for c in range(6,9):
                    if board[r][c] == ".":
                        continue
                    elif board[r][c] in grid:
                        return False
                    else: grid.add(board[r][c])

                if r == 5: grid = set()
            elif r >= 6:
                for c in range(6,9):
                    if board[r][c] == ".":
                        continue
                    elif board[r][c] in grid:
                        return False
                    else: grid.add(board[r][c])
        #print(grid)
        return True

        