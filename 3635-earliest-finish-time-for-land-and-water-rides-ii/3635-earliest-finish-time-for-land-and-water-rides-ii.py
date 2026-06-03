class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        """
        :type landStartTime: List[int]
        :type landDuration: List[int]
        :type waterStartTime: List[int]
        :type waterDuration: List[int]
        :rtype: int
        """
        def calc(start1, dur1, start2, dur2):
            # 1. Earliest possible finish time for the first ride type
            min_end = min(s + d for s, d in zip(start1, dur1))
            
            # 2. Earliest possible finish time for the second ride type
            return min(max(s, min_end) + d for s, d in zip(start2, dur2))
            
        # Try Land first, then Water
        land_first = calc(landStartTime, landDuration, waterStartTime, waterDuration)
        
        # Try Water first, then Land
        water_first = calc(waterStartTime, waterDuration, landStartTime, landDuration)
        
        # Return whichever path gets us out of the park first
        return min(land_first, water_first)