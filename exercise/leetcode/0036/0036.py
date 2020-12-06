
from typing import List


from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        blocks = [set() for _ in range(9)]

        for i in range(len(board)):
            line = board[i]
            for j in range(len(line)):
                val = line[j]
                if val == '.':
                    continue
                val = int(val)

                # in row ?
                if val in rows[i]:
                    return False
                rows[i].add(val)

                # in col ?
                if val in cols[j]:
                    return False
                cols[j].add(val)

                # in block ?
                block_idx = i // 3 + 3 * (j // 3)
                if val in blocks[block_idx]:
                    return False
                blocks[block_idx].add(val)
        return True