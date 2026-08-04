class Solution:

    def encode(self, strs):
        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s

        return res

    def decode(self, s):
        res = []
        i = 0

        while i < len(s):
            j = s.index("#", i)
            length = int(s[i:j])

            i = j + 1
            res.append(s[i:i + length])

            i += length

        return res