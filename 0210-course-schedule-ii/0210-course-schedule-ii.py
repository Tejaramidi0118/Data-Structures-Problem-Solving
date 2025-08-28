class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = defaultdict(list)

        indegree = [0] * numCourses

        for u,v in prerequisites:
            g[v].append(u)
            indegree[u] += 1
        
        q = deque([i for i in range(numCourses) if indegree[i] == 0])
        r = []
        count = 0
        while q:
            course = q.popleft()
            r.append(course)

            count += 1

            for neighbour in g[course]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    q.append(neighbour)
        

        if count == numCourses:
            return r
        else:
            return []

