class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def condition(m):
            time = 0
            for b in piles:
                # we need to round up because: If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
                time += math.ceil(b/m)
            return time <= h 

        # Do a binary search through possible speeds range
        # speed can be at least 1 because he can eat 1 banana each hour and still can complete eating all piles if the hour is large enough
        #  and at most max(piles)
        l, r = 1, max(piles)
        res =  r

        while l <= r:
            m = l + (r - l) // 2
            if condition(m):
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1

        return res


'''
[3,6,7,11]
=> speeds = [1, 11]
m = 6, condition = true
m = 3, condition = false 
if koko can eat 6 bananas within 8 hours, then she can eat less than 6 bananas within 8 hours. Because we try to find minimum value, so we move to the left by decrementing the r pointer. The condition for moving r pointer is time <= h
''' 