class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
     
    
        result = n
        temp = range(n) # help list, 用于连接集合和查找index

        for edge in edges:
            if self.unite(edge[0], edge[1], temp):
                result -= 1

        return result

    def unite(self, start, end, temp):
        sid = self.find(start, temp)
        eid = self.find(end, temp)
        if sid == eid: # 同一个集合
            return False
        else: # 不同id，连接成一个集合
            temp[sid] = eid
            return True

    def find(self, start, temp):
        while temp[start] != start: # 假如不相同，意味着start已经被归入了集合
            temp[start] = temp[temp[start]] # 往下深入，寻找最终的id
            start = temp[start] # 
        return start