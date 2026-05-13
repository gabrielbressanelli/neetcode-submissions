class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_of_t = {}
        hash_of_s = {}

        for char in s:
            hash_of_s[char] = hash_of_s.get(char, 0) + 1

        for char in t:
            hash_of_t[char] = hash_of_t.get(char, 0) + 1

        if hash_of_t == hash_of_s:
            return True

        if hash_of_t != hash_of_s:
            return False
