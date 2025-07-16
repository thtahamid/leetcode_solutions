class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        # Step 1: Initialize counters
        even_count = 0
        odd_count = 0
        alt_even = 0
        alt_odd = 0

        # Step 2: Loop through each number
        for num in nums:
            p = num % 2  # Step 2: Check if number is even or odd

            # Step 3: Update counters
            if p == 0:
                even_count += 1            # Same-parity subsequence of evens
                alt_even = alt_odd + 1     # Alternating sequence ending in even
            else:
                odd_count += 1             # Same-parity subsequence of odds
                alt_odd = alt_even + 1     # Alternating sequence ending in odd

        # Step 4 & 5: Return the maximum of all options
        return max(even_count, odd_count, alt_even, alt_odd)