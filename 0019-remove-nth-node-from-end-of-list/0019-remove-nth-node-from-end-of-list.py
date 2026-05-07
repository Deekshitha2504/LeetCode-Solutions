# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        # dummy=ListNode(0,head)
        # cur=head
        # count=0
        # while cur:
        #     count+=1
        #     cur=cur.next
        # diff=count-n
        # cur=dummy
        # for i in range(diff):
        #     cur=cur.next
        # cur.next=cur.next.next
        # return dummy.next      
        dum=ListNode(0,head)
        slo,fast=dum,dum
        for i in range(n):
            fast=fast.next
        while fast.next!=None:
            fast=fast.next
            slo=slo.next
        slo.next=slo.next.next
        return dum.next