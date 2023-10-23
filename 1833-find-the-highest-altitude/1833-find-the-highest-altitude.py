class Solution(object):
    def largestAltitude(self, gain):
        altitudes = []
        altitudes.append(0)
        initialAlt = 0
        for alt in gain:
            initialAlt += alt
            altitudes.append(initialAlt)
        return max(altitudes)

        