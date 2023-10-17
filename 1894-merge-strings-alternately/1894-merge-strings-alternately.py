class Solution(object):
    def mergeAlternately(self, word1, word2):
        if len(word1) == 0 and len(word2) == 0:
            return ""
        elif len(word1) == 0 and len(word2) != 0:
            return word2
        elif len(word2) == 0 and len(word1) != 0:
            return word1
        else:
            return word1[0] + word2[0] + self.mergeAlternately(word1[1:], word2[1:])
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        