class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):

        if len(flowerbed) == 1 and flowerbed[0] == 0:
            return True

        numFlowersCanPlace = 0
        for i in range(len(flowerbed)):

            isFlowerPossibleHere = False
            if flowerbed[i] == 0:
                if i == 0:
                    if flowerbed[i+1] == 0:
                        isFlowerPossibleHere = True
                elif i == len(flowerbed) - 1:
                    if flowerbed[i-1] == 0:
                        isFlowerPossibleHere = True
                elif flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    isFlowerPossibleHere = True
                if isFlowerPossibleHere == True:    
                    flowerbed[i] = 1
                    numFlowersCanPlace += 1
        if numFlowersCanPlace >= n:
            return True
        else:
            return False



        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        