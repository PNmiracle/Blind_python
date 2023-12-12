# 答案！！
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        # to avoid a KeyError if you try to access or modify an item with
        # a key that does not exist.
        # can automatically create a new list for a new key
        # if the key is not already present in the dictionary.
        res = defaultdict(list)  # mapping charCount to list of Anagrams

        for s in strs:
            count = [0] * 26  # a list to store the count of characters

            for c in s:
                # full name is ordinal
                count[ord(c) - ord("a")] += 1  # increment the count for the character 'c'
            # lists are unhashale because they are mutable, so we need to change
            # a list to a tuple.
            res[tuple(count)].append(s)  # append the string 's' to the list of its character count

        return list(res.values())  # return the grouped anagrams



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

    def groupAnagrams(self, strS):
        """
        :type strS: List[str]
        :rtype: List[List[str]]
        """
        res_list = []
        checked = set()  # Keep track of the strings that have been grouped

        for i in range(len(strS)):
            if strS[i] not in checked:
                mid_list = [strS[i]]
                # Iterate over the remaining strings
                for j in range(i + 1, len(strS)):
                    if self.isAnagram(strS[i], strS[j]):
                        mid_list.append(strS[j])
                        checked.add(strS[j])  # Add to checked set
                res_list.append(mid_list)
                checked.add(strS[i])  # Add the current string to the checked set

        return res_list


    # def groupAnagrams(self, strS):
    #     """
    #     :type strS: List[str]
    #     :rtype: List[List[str]]
    #     """
    #     # when strs is not null？
    #     res_list = []
    #     while strS:
    #         temp = strS[0]
    #         strS.remove(temp)
    #         for e in strS:
    #             # 为啥要用self才能调用呢？
    #             mid_list = [temp]
    #             if self.isAnagram(temp, e):
    #                 mid_list.append(e)
    #                 # 列表如何删除元素？
    #                 strS.remove(e)
    #         res_list.append(mid_list)
    #     return res_list


