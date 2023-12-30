def is_safe(board, row, col, N):
    # 檢查同一列上是否有皇后
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # 檢查左上到右下的對角線上是否有皇后
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # 檢查左下到右上的對角線上是否有皇后
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_n_queens_util(board, row, N):
    if row == N:
        # 找到一个解决方案
        for i in range(N):
            for j in range(N):
                print(board[i][j], end=" ")
            print()
        print()
        return
    
    for col in range(N):
        if is_safe(board, row, col, N):
            # 在當前位置放置皇后
            board[row][col] = 1
            
            solve_n_queens_util(board, row + 1, N)
            
            # 回溯，撤回當前位置的皇后，繼續嘗試其他位置
            board[row][col] = 0

def solve_n_queens(N):
    board = [[0] * N for _ in range(N)]
    
    # 從第1行開始解決
    solve_n_queens_util(board, 0, N)

# 結果
solve_n_queens(8)
