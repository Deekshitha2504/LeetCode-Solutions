class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def calculate_waviness(x: int) -> int:
            digits = str(x)
            n = len(digits)
            
            if n < 3:
                return 0
                
            waviness = 0
            for i in range(1, n - 1):
                current = digits[i]
                left = digits[i - 1]
                right = digits[i + 1]
                
                if current > left and current > right:
                    waviness += 1
                elif current < left and current < right:
                    waviness += 1
                    
            return waviness

        return sum(calculate_waviness(x) for x in range(num1, num2 + 1))