class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        from collections import Counter
        
        # Count occurrences of each power value
        cnt = Counter(power)
        
        # Get unique sorted values
        unique = sorted(cnt.keys())
        n = len(unique)
        
        if n == 0:
            return 0
        
        # dp[i] = max damage using first i unique values
        # For each unique value, we either skip it or take all occurrences
        # If we take it, we can't take values within ±2
        
        dp = [0] * (n + 1)
        
        # For each unique value, find the last valid index we can use
        j = 0  # pointer for binary search optimization
        
        for i in range(n):
            val = unique[i]
            damage = val * cnt[val]
            
            # Find the latest j where unique[j] < val - 2
            # Binary search for efficiency
            left, right = 0, i
            while left < right:
                mid = (left + right) // 2
                if unique[mid] < val - 2:
                    left = mid + 1
                else:
                    right = mid
            
            # left is the first index where unique[left] >= val - 2
            # So the last valid index is left - 1
            prev_idx = left  # Actually we want dp[left] which is dp from indices 0..left-1
            
            # Take this value: dp[prev_idx] + damage
            # Skip this value: dp[i]
            dp[i + 1] = max(dp[i], dp[prev_idx] + damage)
        
        return dp[n]