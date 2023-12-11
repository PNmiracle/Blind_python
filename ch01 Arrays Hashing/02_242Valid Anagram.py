#  错误原因：试图增加或减少 hashMap[e] 的值时，如果 e 不在字典中，这将导致 KeyError。
#  在对字典 hashMap 进行操作前，您需要先检查键是否存在，如果不存在，应当先将其初始化为0。
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hashMap = {}
        for e in s:
            hashMap[e] += 1
        for e in t:
            hashMap[e] -= 1
        for i, e in enumerate(hashMap):
            if (e != 0):
                return False
        return True

# if来先将其初始化为0。
class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        hashMap = {}
        for e in s:
            if e in hashMap:
                hashMap[e] += 1
            else:
                hashMap[e] = 1
        for e in t:
            if e in hashMap:
                hashMap[e] -= 1
            else:
                hashMap[e] = -1
        for key in hashMap:
            if hashMap[key] != 0:
                return False
        return True
# 答案
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t)

        # return Counter(s) == Counter(t)
        if len(s) != len(t):
            return False

        counts, countT = {}, {}

        for i in range(len(s)):
            counts[s[i]] = 1 + counts.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for c in counts:
            if counts[c] != countT.get(c, 0):
                return False

        return True


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        countST = {}
        for i in range(len(s)):
            countST[s[i]] = countST.get(s[i], 0) + 1
            countST[t[i]] = countST.get(t[i], 0) - 1
        for c in countST:
            if countST[c] != 0:
                return False
        return True
