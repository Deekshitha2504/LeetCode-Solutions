class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        counts = Counter(s)
        sorted_chars = sorted(counts.keys(), key=lambda x: counts[x], reverse=True)
        
        if counts[sorted_chars[0]] > (n + 1) // 2:
            return ""

        res = [""] * n
        index = 0
        
        for char in sorted_chars:
            for _ in range(counts[char]):
                res[index] = char
                index += 2  
                
                if index >= n:
                    index = 1
                    
        return "".join(res)