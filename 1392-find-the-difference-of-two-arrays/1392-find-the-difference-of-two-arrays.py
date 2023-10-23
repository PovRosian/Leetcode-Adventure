class Solution(object):
    def findDifference(self, nums1, nums2):
        
        result1 = set()
        result2 = set()

        for num in nums1:
            if num not in nums2:
                result1.add(num)

        for num in nums2:
            if num not in nums1:
                result2.add(num)

        return [list(result1),list(result2)]