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


if __name__ == "__main__":
    temp = Solution()
    list_one = ListNode(val=2, next=ListNode(val=4, next= ListNode(val=3, next=None)))
    list_two = ListNode(val=5, next=ListNode(val=6, next= ListNode(val=4, next=None)))

    temp.addTwoNumbers(ListNode, list_two)
