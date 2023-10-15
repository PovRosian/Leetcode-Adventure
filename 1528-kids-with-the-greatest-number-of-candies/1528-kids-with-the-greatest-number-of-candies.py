class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        maxCandies = max(candies)
        booleanOutput = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= maxCandies:
                booleanOutput.append(True)
            else:
                booleanOutput.append(False)
        return booleanOutput
        