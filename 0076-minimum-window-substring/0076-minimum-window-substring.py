class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ""

        dict_t = Counter(t)
        required_unique = len(dict_t)

        filtered_s = []
        for i, char in enumerate(s):
            if char in dict_t:
                filtered_s.append((i, char))

        if not filtered_s:
            return ""

        window_counts = {}
        formed = 0
        left = 0
        ans = (float("inf"), None, None)

        for right in range(len(filtered_s)):
            right_idx, char = filtered_s[right]
            window_counts[char] = window_counts.get(char, 0) + 1

            if window_counts[char] == dict_t[char]:
                formed += 1

            while left <= right and formed == required_unique:
                left_idx, left_char = filtered_s[left]

                current_len = right_idx - left_idx + 1
                if current_len < ans[0]:
                    ans = (current_len, left_idx, right_idx)

                window_counts[left_char] -= 1
                if window_counts[left_char] < dict_t[left_char]:
                    formed -= 1
                
                left += 1

        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]