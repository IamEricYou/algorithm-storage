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
    
    # Reverse Integer 
    def reverse(self, x: int) -> int:
        temp_val = str(x)
        # print(''.join(reversed(temp_val))) #method 1
        if temp_val[0] == '-':
            answer = int(self.delete_front_zeros('-' + temp_val[:0:-1]))
        else:
            answer = int(self.delete_front_zeros(temp_val[::-1]))
        
        if answer > 2**31 - 1 or answer < -2**31 - 1:
            return 0
        
        return answer
    
    def delete_front_zeros(self, x: str) -> str:
        temp_val = list(x)
        count = 0
        for item in x:
            if item == '0' and len(x) == 1:
                return ''.join(temp_val)

            if item != '0':
                return ''.join(temp_val)

            temp_val.pop(0)


if __name__ == "__main__":
    two = Solution()
    # print(two.twoSum([1,2,2,7,3,3], 6))
    # print(two.twoSumByListMethod([1,2,2,7,3,3], 6))
    print(two.reverse(342))
    print(two.reverse(-120))
    print(two.reverse(0))