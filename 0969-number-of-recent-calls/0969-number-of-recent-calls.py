class RecentCounter(object):

    def __init__(self):
        self.timestamps = []


    def ping(self, t):
        self.timestamps.append(t)

        while self.timestamps[0] < t-3000:
            self.timestamps.pop(0)

        return len(self.timestamps)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)