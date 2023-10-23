class Solution(object):
    def pivotIndex(self, nums):
        for pivot in range(len(nums)):
            sumLeft = sum(nums[:pivot])  # Sum of elements to the left of the pivot
            sumRight = sum(nums[pivot + 1:])  # Sum of elements to the right of the pivot

            if sumLeft == sumRight:
                return pivot  # Return the index if sums are equal

        return -1  # If no pivot index is found, return -1
        