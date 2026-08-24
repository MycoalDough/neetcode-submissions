class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        copyHead = Node(head.val)
        copy_curr = copyHead
        curr = head.next

        saved = {head: copyHead}

        while curr is not None:
            newNode = Node(curr.val)

            copy_curr.next = newNode
            saved[curr] = newNode

            curr = curr.next
            copy_curr = copy_curr.next

        curr = head
        copy_curr = copyHead

        while curr is not None:
            copy_curr.random = saved.get(curr.random)

            curr = curr.next
            copy_curr = copy_curr.next

        return copyHead