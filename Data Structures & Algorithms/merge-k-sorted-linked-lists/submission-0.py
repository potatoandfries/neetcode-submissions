# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        e_list = [];
        for list in lists:
            while list:
                e_list.append(list.val)
                list = list.next
        e_list = sorted(e_list)
        if not e_list:
            return None
        dummy = ListNode(0)
        current = dummy
        for val in e_list:
            current.next = ListNode(val)
            current = current.next
        return dummy.next