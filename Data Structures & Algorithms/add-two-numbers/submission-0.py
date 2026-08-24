# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        carry = 0
        one = l1
        two = l2

        dummyHead = ListNode(0)

        curr = dummyHead

        while one is not None or two is not None or carry:
            val = carry
            if one is not None:
                val += one.val
                one = one.next
            if two is not None:
                val += two.val
                two = two.next
            carry = 0

            if val >= 10:
                carry = 1
                val -= 10

            curr.next = ListNode(val)
            curr = curr.next

        
        return dummyHead.next

        

        