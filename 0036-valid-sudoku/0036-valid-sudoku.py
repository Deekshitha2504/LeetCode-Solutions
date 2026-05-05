class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        visited=set()
        for r in range(9):
            for c in range(9):
                num=board[r][c]
                if num!='.':
                    rowKey=(num,r)
                    colKey=(c,num)
                    boxKey=(c//3,r//3,num)
                    if rowKey in visited or colKey in visited or boxKey in visited:
                        return False
                    visited.add(rowKey)    
                    visited.add(colKey)
                    visited.add(boxKey)
        return True        