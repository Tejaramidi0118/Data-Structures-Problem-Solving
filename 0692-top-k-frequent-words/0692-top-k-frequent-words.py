class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        freq = {}

        for i in words:
            freq[i] = freq.get(i,0) + 1

        freq_sorted_values = dict(sorted(freq.items(), key = 
                                lambda item: item[1], reverse=True))
        
        res = {}
        for u, v in freq_sorted_values.items():
            if v not in res:
                res[v] = [u]
            else:
                res[v].append(u)
        
        output = []
        flag = False
        i = 0
        for r in res.values():
            r.sort()
            for nr in r:
                if i < k:
                    output.append(nr)
                    i += 1
                else:
                    flag = True
                    break
            
            if flag:
                break
                
        return output