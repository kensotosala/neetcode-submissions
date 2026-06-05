from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        # Frequency map for characters in t
        dict_t = Counter(t)

        # Number of unique characters in t that need to be present in the window
        required = len(dict_t)

        # Left and right pointers
        left, right = 0, 0

        # To keep track of the number of characters in the current window that match the desired frequency in t
        formed = 0

        # Dictionary to count characters in the current window
        window_counts = {}

        # Result tuple: (window length, left, right)
        ans = float("inf"), None, None

        while right < len(s):
            # Add character at right pointer to the window
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1

            # If the frequency of the current character matches its required count in t, increment the formed count
            if char in dict_t and window_counts[char] == dict_t[char]:
                formed += 1

            # Try to shrink the window until it ceases to be valid
            while left <= right and formed == required:
                char = s[left]

                # Update the result if this window is smaller than the previously found smallest window
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)

                # Remove the character at the left pointer from the window
                window_counts[char] -= 1
                if char in dict_t and window_counts[char] < dict_t[char]:
                    formed -= 1

                # Move the left pointer to shrink the window
                left += 1

            # Expand the window by moving the right pointer
            right += 1

        # Return the smallest window or an empty string if no valid window was found
        return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]
