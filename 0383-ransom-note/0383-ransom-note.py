class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote)>len(magazine):
            return False
        for a in ransomNote:
            if ransomNote.count(a) > magazine.count(a):
                return False
        return True