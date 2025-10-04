from typing import List

class Solution:
    def __init__(self):
        self.ans = []

    def dfs(self, s: str, target: int, idx: int, curVal: int, lastVal: int, expr: str):
        if idx == len(s):
            if curVal == target:
                self.ans.append(expr)
            return

        for j in range(idx, len(s)):
            if j > idx and s[idx] == '0':
                break

            part = s[idx:j+1]
            num = int(part)

            if idx == 0:
                self.dfs(s, target, j + 1, num, num, part)
            else:
                self.dfs(s, target, j + 1, curVal + num, num, expr + "+" + part)
                self.dfs(s, target, j + 1, curVal - num, -num, expr + "-" + part)
                self.dfs(s, target, j + 1, curVal - lastVal + lastVal * num, lastVal * num, expr + "*" + part)

    def findExpr(self, s: str, target: int) -> List[str]:
        self.ans = []
        self.dfs(s, target, 0, 0, 0, "")
        self.ans.sort()
        return self.ans
