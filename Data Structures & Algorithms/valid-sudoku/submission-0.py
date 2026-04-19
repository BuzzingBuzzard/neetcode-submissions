class Solution:
    def checkCurr(self, board, row, col, hashmap) -> bool:
        curr = board[row][col]
        if curr == ".":
            return True
        hashmap[curr] = hashmap.get(curr, 0) + 1
        if hashmap[curr] > 1:
            return False
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hashmap = {}
        n = len(board)

        # Row check
        for row in range(n):
            hashmap = {}
            for col in range(n):
                isCurrValid = self.checkCurr(board, row, col, hashmap)
                if not isCurrValid:
                    return False
        hashmap = {}

        # Col check
        for col in range(n):
            hashmap = {}
            for row in range(n):
                isCurrValid = self.checkCurr(board, row, col, hashmap)
                if not isCurrValid:
                    return False
        
        # # Square check
        for square_row in range(1,4):
            hashmap = {}
            for square_col in range(1,4):
                hashmap = {}
                max_row = square_row * 3
                max_col = square_col * 3
                for row in range(max_row - 3, max_row):
                    for col in range(max_col - 3, max_col):
                        isCurrValid = self.checkCurr(board, row, col, hashmap)
                        if not isCurrValid:
                            return False
                
        return True


