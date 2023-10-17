class Solution(object):
    def reverseVowels(self, s):
        vowels = "aeiouAEIOU"

        def reverse_helper(s_list, left, right):
            if left >= right:
                return ''.join(s_list)

            while left < right and s_list[left] not in vowels:
                left += 1
            while left < right and s_list[right] not in vowels:
                right -= 1

            s_list[left], s_list[right] = s_list[right], s_list[left]
            return reverse_helper(s_list, left + 1, right - 1)

        s_list = list(s)
        return reverse_helper(s_list, 0, len(s_list) - 1)
