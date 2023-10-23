class Solution(object):
    def uniqueOccurrences(self, arr):

        countDict = {}
        for num in arr:
            if num not in countDict:
                countDict[num] = 1
            else:
                countDict[num] += 1

        values_set = set()

        for val in countDict.values():
            values_set.add(val)
        
        if len(values_set) == len(countDict):
            return True
        else:
            return False
        