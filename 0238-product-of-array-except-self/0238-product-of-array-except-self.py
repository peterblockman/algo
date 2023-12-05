class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        '''
            nums [1, 2, 3, 4]
            pre  [1, 1, 2, 6] (prefix products of every num, nums[i] 
                not included)
            post [24, 12, 4, 1] (postfix products of every num, 
                    nums[i]  not included) 
            output [24, 12, 8, 6] [1 * 24, 1* 12, 2*4, 6*1]
        '''

        output = [1] * len(nums)
        prefix = 1
        postfix = 1
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]

        for i in range(len(nums)  - 1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]
        
        return output