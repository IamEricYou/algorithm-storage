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
    
    def reverseBits(self, n: int) -> int:
        temp_val = str(bin(n)[2:].zfill(32))
        swap_val = temp_val[::-1]
        # '{:032}'.format(int(swap_val))
        return int(swap_val, 2)
        
    # Number of 1 Bits
    def hammingWeight(self, n: int) -> int:
        return str(bin(n)[2:].zfill(32)).count('1')

    # Power of Two
    def isPowerOfTwo(self, n: int) -> bool:
        answer = n
        while True:
            if answer == 0:
                return False
            
            if answer == 1:
                return True

            answer = answer / 2

        return True
    
    def singleNumber(self, nums: List[int]) -> int:
        temp_list = list(set(nums))
        list_has_duplicates =  [x for x in nums if x not in temp_list or temp_list.remove(x)]
        return list(set(nums) - set(list_has_duplicates))
    
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', "[.]")

    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        answer = []
        for i in candies:
            answer.append(i + extraCandies >= max(candies) )
        return answer
    
    def isMonotonic(self, A: List[int]) -> bool:
        checker = 0 # increasing 0, if not 1
        temp = A[0]
        for i in range(1,len(A)):
            if(temp >= A[i]):
                pass
        return 4

    def isPalindrome(self, x: int) -> bool:
        if (x < 0):
            return False
        
        str_number = str(x)
        comp_number = str_number[::-1]
        
        if comp_number != str_number:
            return False

        return True

    def isValid(self, s: str) -> bool:
        open_bracket = ["(", "{", "<", "["]
        closed_bracket = [")", "}", ">", "]"]
        temp = [x for x in s]
        checker = []

        # while True:
        #     if not temp:
        #         return True
            
        #     x = temp.pop(0)

        #     if x in open_bracket:
        #         where = open_bracket.index(x)
        #         if closed_bracket[where] not in temp:
        #             return False
        #         else:
        #             temp.remove(closed_bracket[where])
        #     else:
        #         return False

        for item in temp:
            if item in open_bracket:
                checker.append(item)
            else:
                if not checker:
                    return False
                    
                where = closed_bracket.index(item)
                print(checker)
                if checker[-1] == open_bracket[where]:
                    del checker[-1]
                else:
                    return False
        
        if checker:
            return False

        return True

if __name__ == "__main__":
    two = Solution()
    
    # print(two.twoSum([1,2,2,7,3,3], 6))
    # print(two.twoSumByListMethod([1,2,2,7,3,3], 6))
    
    # print(two.reverse(342))
    # print(two.reverse(-120))
    # print(two.reverse(0))

    # print(two.reverseBits(43261596))

    # print(two.hammingWeight(11))
    
    # print(two.isPowerOfTwo(10))

    # print(two.singleNumber([4,4,2,2,1]))