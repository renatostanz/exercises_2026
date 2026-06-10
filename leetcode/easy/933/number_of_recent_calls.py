class RecentCounter:

    def __init__(self):
        self.ls = []
    
    def ping(self, t: int) -> int:
        self.ls.append(t)

        for i in range(len(self.ls) - 2, -1, -1):
            if self.ls[i] < t - 3000:
                return len(self.ls) - (i + 1)

        return len(self.ls)



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
