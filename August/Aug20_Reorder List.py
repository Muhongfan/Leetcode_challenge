"""
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
"""


def reorderList(self, head):
    """
    :type head: ListNode
    :rtype: void Do not return anything, modify head in-place instead.
    """
    if head and head.next and head.next.next:
        # find mid
        fast, slow = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        head1 = head
        head2 = slow.next
        slow.next = None

        # reverse linked list head2
        dummy = ListNode(0)
        dummy.next = head2
        p = head2.next
        head2.next = None
        while p:
            temp = p
            p = p.next
            temp.next = dummy.next
            dummy.next = temp
        head2 = dummy.next

        # merge two linked list head1 and head2
        p1 = head1
        p2 = head2
        while p2:
            temp1 = p1.next
            temp2 = p2.next
            p1.next = p2
            p2.next = temp1
            p1 = temp1
            p2 = temp2
#demo
def reorderList2(self, head):
    """
    :type head: ListNode
    :rtype: None Do not return anything, modify head in-place instead.
    """
    if not head:
        return
    slow = head
    fast = head
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
    secondHead = slow.next
    slow.next = None
    if secondHead:
        prev = None
        curr = secondHead
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        curr1 = head
        curr2 = prev
        while curr1 and curr2:
            newNext = curr1.next
            curr1.next = curr2
            curr1 = curr2
            curr2 = newNext