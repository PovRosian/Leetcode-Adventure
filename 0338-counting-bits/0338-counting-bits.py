class Solution(object):
    def countBits(self, n):
        bits = []
        for i in range(n+1):
            bits.append(bin(i).count("1"))
        return bits

        """
        :type n: int
        :rtype: List[int]
        """
        