class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        phone_map = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        result = [""]
        for digit in digits:
            letters = phone_map[int(digit)]
            new_result = []
            for combo in result:
                for letter in letters:
                    new_result.append(combo + letter)
            result = new_result
        return result
