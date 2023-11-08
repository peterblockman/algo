class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # find the first node they intersect at. Leave slow pointer there
        fast, slow = 0, 0
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if slow == fast:
                break

        # make another slow pointer and shift the two slow pointers by one. Where they interect is the result
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                break

        return slow