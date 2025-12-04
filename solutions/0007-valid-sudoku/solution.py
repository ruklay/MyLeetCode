def isValidSudoku(board):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    subgrids = [set() for _ in range(9)]
    
    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num != '.':
                # Check for duplicates in the current row
                if num in rows[i]:
                    return False
                rows[i].add(num)
                
                # Check for duplicates in the current column
                if num in cols[j]:
                    return False
                cols[j].add(num)
                
                # Check for duplicates in the current 3x3 subgrid
                subgrid_index = (i // 3) * 3 + (j // 3)
                if num in subgrids[subgrid_index]:
                    return False
                subgrids[subgrid_index].add(num)
    
    return True