#Word Search


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for y in xrange(len(board)):
            for x in xrange(len(board[0])):
                if self.exit(board, word, x, y, 0):
                    return True
        return False

    def exit(self, board, word, x, y, i):
        if i == len(word):
            return True
        if x < 0 or x >= len(board[0]) or y < 0 or y >= len(board):
            return False
        if board[y][x] != word[i]:
            return False
        board[y][x] = board[y][x].swapcase()
        isexit = self.exit(board, word, x + 1, y, i + 1) or self.exit(board, word, x, y + 1, i + 1) or self.exit(board,
                 word, x - 1,y, i + 1) or self.exit(board, word, x, y - 1, i + 1)
        board[y][x] = board[y][x].swapcase()
        return isexit