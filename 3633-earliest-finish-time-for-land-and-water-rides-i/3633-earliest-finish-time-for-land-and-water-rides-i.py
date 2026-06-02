class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        """
        :type landStartTime: List[int]
        :type landDuration: List[int]
        :type waterStartTime: List[int]
        :type waterDuration: List[int]
        :rtype: int
        """
        # Helper function to compute the earliest finish time for a specific order
        def calc(start1, dur1, start2, dur2):
            # Step 1: Find the absolute earliest we can finish the first ride type
            min_end = min(s + d for s, d in zip(start1, dur1))
            
            # Step 2: Use that end time to evaluate the best second ride type
            # max(s, min_end) handles waiting for the ride to open if we finish early
            return min(max(s, min_end) + d for s, d in zip(start2, dur2))
            
        # Try Scenario A: Land first, then Water
        land_first = calc(landStartTime, landDuration, waterStartTime, waterDuration)
        
        # Try Scenario B: Water first, then Land
        water_first = calc(waterStartTime, waterDuration, landStartTime, landDuration)
        
        # Return whichever scenario finishes earliest
        return min(land_first, water_first)