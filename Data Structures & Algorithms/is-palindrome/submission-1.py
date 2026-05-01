class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = ''.join(char for char in s if char.isalnum()).lower()
        if s == '':
            return True
        
        l = 0
        r = len(new_string) - 1

        while l < r:
            if new_string[l] != new_string[r]:
                return False
            l += 1
            r -= 1
        return True
