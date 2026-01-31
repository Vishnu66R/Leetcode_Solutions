class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = [""] * numRows
        row = 0
        down = False
        for char in s:
            rows[row] += char
            if row == 0 or row == numRows - 1:
                down = not down
            if down:
                row += 1
            else:
                row -= 1
        return "".join(rows)
