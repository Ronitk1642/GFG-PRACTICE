class Solution:
    def chooseSwap(self, s):
        mp = {}

        # Store all characters with (present, visited)
        for ch in s:
            mp[ch] = [True, False]

        i = 0
        y = '#'
        z = '#'
        check = False

        while i < len(s):
            c = s[i]

            # Iterate in sorted order like std::map
            for x in sorted(mp.keys()):
                a, b = mp[x]

                if x < c and a and not b:
                    y = x
                    z = s[i]
                    check = True
                    break

            if check:
                break

            mp[s[i]] = [True, True]
            i += 1

        if i >= len(s):
            return s

        s = list(s)

        for i in range(len(s)):
            if s[i] == y:
                s[i] = z
            elif s[i] == z:
                s[i] = y

        return "".join(s)