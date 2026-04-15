class Solution:
    def URLify(self, s):
        res = ""
        for ch in s:
            if ch == ' ':
                res += '%20'
            else:
                res += ch
        return res