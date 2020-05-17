from typing import List

# add two numbers

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        print("This class is called")

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        print(l1.__str__)
        
    def findDuplicate(self, nums: List[int]) -> int:
        temp_list = list(set(nums))
        return [x for x in nums if x not in temp_list or temp_list.remove(x)][0]
        
    def lengthOfLongestSubstring(self, s: str) -> int:
        str_to_set = set([x for x in s])
        return len(str_to_set)

    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        for char in J:
            count += S.count(char)
        return count

if __name__ == "__main__":

    temp = Solution()
    # list_one = ListNode(val=2, next=ListNode(val=4, next= ListNode(val=3, next=None)))
    # list_two = ListNode(val=5, next=ListNode(val=6, next= ListNode(val=4, next=None)))

    # temp.addTwoNumbers(ListNode, list_two)

    # print(temp.findDuplicate([1,3,4,2,2]))

    # print(temp.lengthOfLongestSubstring("pwwkew"))

    print(temp.numJewelsInStones("z", "ZZ"))