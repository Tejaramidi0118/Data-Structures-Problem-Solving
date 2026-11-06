class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key = lambda a:a[1])

        sorted_queries = sorted(
            [(q,i) for i, q in enumerate(queries)]
        )

        freq = {}
        ans = [0 for _ in range(len(queries))]

        l, r = 0, 0

        for q, i in sorted_queries:
            start = q-x

            while r < len(logs) and logs[r][1] <= q:
                server = logs[r][0]
                freq[server] = freq.get(server,0) + 1
                r += 1
            
            while l < r and logs[l][1] < start:
                server = logs[l][0]
                freq[server] -= 1

                if freq[server] == 0:
                    del freq[server]
                
                l += 1

            ans[i] = n - len(freq)
        
        return ans