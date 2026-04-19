class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}
        for char in s:
            dict_s[char] = dict_s.get(char, 0) + 1
        for char in t:
            dict_t[char] = dict_t.get(char, 0) + 1
        if len(dict_s) != len(dict_t):
            return False
        for s_key in dict_s.keys():
            if dict_s[s_key] != dict_t.get(s_key, 0):
                return False
        return True