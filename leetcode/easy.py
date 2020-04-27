# two-sum

from typing import List
class Solution:
    #Basic Version
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer_list = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    answer_list.append(i)
                    answer_list.append(j)
                    return answer_list

    def twoSumByDictionary(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for cnt, num in enumerate(nums):
            print(cnt, num)
            if target - num in lookup:
                return lookup[target-num], cnt
            lookup[num] = cnt

if __name__ == "__main__":
    two = Solution()
    print(two.twoSum([1,2,2,7,3,3], 6))
    print(two.twoSumByListMethod([1,2,2,7,3,3], 6))