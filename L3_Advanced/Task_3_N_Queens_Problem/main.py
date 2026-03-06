

class NQueens:
    def n_queens_solution(self, n: int):
        
        def is_safe(board, row, col, n):

            for i in range(n):
                if board[row][i] == "Q":
                    return False

            for j in range(n):
                if board[j][col] == "Q":
                    return False 

            i = row 
            j = col 

            while i>=0 and j>=0:
                if board[i][j] == "Q":
                    return False
                i-=1
                j-=1

            
            i = row
            j = col 

            while i>=0 and j<n:
                if board[i][j] == "Q":
                    return False
                i-=1
                j+=1
            
            return True 


        def n_queens(board: list, row: int, n: int, ans: list):
            if row == n:
                ans.append(["".join(item) for item in board])
                return None 

            for j in range(n):
                if is_safe(board, row, j, n):
                    board[row][j] = "Q"
                    n_queens(board, row+1, n, ans)
                    board[row][j] = "."


        board = [["."]*n for _ in range(n)]
        # print(board)
        ans = []

        n_queens(board, 0, n, ans)
        # print(ans)
        return ans
        

print(NQueens().n_queens_solution(5))
