class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        # motonomically decreasing queue: a way to get the maximum value which is always the first
        q = collections.deque()
        left = 0

        for right in range(len(nums)):
            # if current num greater than the last number of the queue 
            # it will break the order of the queue 
            # remove the last item from the queue 
            # and then add the current num to the queue
            # to start a new order
            while q and  nums[right] > nums[q[-1]]:
                q.pop()

            q.append(right)

            # when moving left, q[0] will be no longer in bound, we need to pop it
            if left > q[0]:
                q.popleft()

            # why does it need to be at least size k not exactly size k?
            # => if k = 3, means that right must be at least 2 in order to make
            # the window len 3
            if (right + 1) >= k:
                res.append(nums[q[0]])
                left += 1

        return res
