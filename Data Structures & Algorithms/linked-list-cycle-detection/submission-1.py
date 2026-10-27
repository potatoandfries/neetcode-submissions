# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# this is for previous attempt. I understand what you're trying to do, but unfortunately, your code has several issues. Here's a breakdown of what's wrong and how to fix it:

# for i in head for range of (len(head)-1): is not a valid Python syntax. You can't use for loops like this to iterate over a linked list.
# len(head) is not a valid operation because head is a node, not a list.
# head[i] is not a valid operation because head is a node, not a list.
# head[i+2].find() is not a valid operation because head[i+2] is not a valid expression, and even if it were, find() is not a method that can be called on a node.

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False;

