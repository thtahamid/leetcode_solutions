class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        m = len(costs)
        ticket_duration = [1, 7, 30]

        def bisect_left(target, left):
            right = n
            while left < right:
                mid = left + (right - left) // 2
                if target <= days[mid]:
                    right = mid
                else:
                    left = mid + 1
            return left

        @cache
        def dp(i):
            if i >= n:
                return 0

            ans = inf
            for j in range(m):
                curr_ticket_cost = costs[j]
                curr_duration = ticket_duration[j]

                end_day = days[i] + curr_duration
                new_i = bisect_left(end_day, i)

                ans = min(ans, curr_ticket_cost + dp(new_i))
            return ans
        return dp(0)      