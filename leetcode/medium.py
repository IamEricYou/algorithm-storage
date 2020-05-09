from typing import List

# add two numbers

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        # print("This class is called")
        pass

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        print(l1.__str__)
        
    def findDuplicate(self, nums: List[int]) -> int:
        temp_list = list(set(nums))
        return [x for x in nums if x not in temp_list or temp_list.remove(x)][0]

    def myAtoi(self, str: str) -> int:
        import re
        string_value = str.lstrip().split(" ")[0]
        parsed_value = re.findall('\d+|\D+', string_value)
        
        if not parsed_value:
            return 0

        if parsed_value[0] == '-' and len(parsed_value) > 1:
            try :
                num = int('-' + parsed_value[1])
                if num < -2147483648:
                    return -2147483648

                if num > 2147483647:
                    return 2147483647
                
                return num
            except ValueError:
                return 0
        elif parsed_value[0] == '+' and len(parsed_value) > 1:
            try :
                num = int(parsed_value[1])
                if num < -2147483648:
                    return -2147483648

                if num > 2147483647:
                    return 2147483647
                
                return num
            except ValueError:
                return 0
        else:
            try :
                num = int(parsed_value[0])
                if num < -2147483648:
                    return -2147483648

                if num > 2147483647:
                    return 2147483647

                return num
            except ValueError:
                return 0

        return 0
    

    def generateParenthesis(self, n: int) -> List[str]:
        complete_paran = ['(', ')']
        temp = []
        for i in range(n):
            temp.append(complete_paran*i)
        return temp



if __name__ == "__main__":
    temp = Solution()
    # list_one = ListNode(val=2, next=ListNode(val=4, next= ListNode(val=3, next=None)))
    # list_two = ListNode(val=5, next=ListNode(val=6, next= ListNode(val=4, next=None)))

    # temp.addTwoNumbers(ListNode, list_two)

    # print(temp.findDuplicate([1,3,4,2,2]))

    # print(temp.myAtoi("+1"))

    print(temp.generateParenthesis(3))
