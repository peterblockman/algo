class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # neetcode solution
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2

        if len(A) > len(B):
            A, B = B, A
        
        l, r = 0, len(A) - 1

        while True:
            i = l + (r - l) // 2
            # i + 1 because A is a 0-index
            # - 1 at the end because we want to get the index of B
            j = half - (i + 1) - 1

            # looking at 2 numbers on the shorter partition 
            A_Left = A[i] if i >= 0 else float("-infinity")
            A_Right = A[i+ 1] if (i + 1) < len(A) else float("infinity")
            # looking at 2 numbers on the longer partition
            B_Left = B[j] if j >= 0 else float("-infinity")
            B_Right = B[j + 1] if (j + 1) < len(B) else float("infinity")

            # all items at the middle of sorted merged array must satisfy:
            if A_Left <= B_Right and B_Left <= A_Right:
              if total % 2:
                return min(A_Right, B_Right)
              else:
                return (max(A_Left, B_Left) + min(A_Right, B_Right)) / 2
            elif A_Left > B_Right:
                # item on A Left gt B Right => move r because A_Left <= B_Right
                r = i - 1
            else:
                l = i + 1
            