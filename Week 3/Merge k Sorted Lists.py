# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ans = ListNode(-1e5)
        ans_node = ans
        
        memo = deque()

        for node in lists:
            temp = deque()
            while node:
                temp.append(node.val)
                node = node.next
            memo.extend(temp)

        memo = sorted(memo)
        for i in range(len(memo)):
            ans_node.next = ListNode(memo[i])
            ans_node = ans_node.next
        return ans.next
            
        
