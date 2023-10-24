class Solution(object):
    def canVisitAllRooms(self, rooms):
        n = len(rooms)
        visited = set()

        def dfs(room):
            visited.add(room)
            for key in rooms[room]:
                if key not in visited:
                    dfs(key)

        dfs(0)
        return len(visited) == n

        





        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        