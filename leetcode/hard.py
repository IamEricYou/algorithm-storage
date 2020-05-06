from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        import statistics
        combined = nums1 + nums2
        return float(statistics.median(combined))

    def isNumber(self, s: str) -> bool:
        a = 4
        print(s.isdigit())
        return 0
if __name__ == "__main__":
    two = Solution()
    # print(two.findMedianSortedArrays([1,3], [2]))
    print(two.isNumber("23.3"))