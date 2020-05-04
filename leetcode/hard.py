from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        import statistics
        combined = nums1 + nums2
        return float(statistics.median(combined))

if __name__ == "__main__":
    two = Solution()
    print(two.findMedianSortedArrays([1,3], [2]))