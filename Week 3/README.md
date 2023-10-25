# [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/description/)
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False

        slow = head
        fast = head.next

        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
```

# [Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/description/)
```python
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = [[0]*len(grid[0]) for _ in range(len(grid))]

        for i in reversed(range(len(grid))):
            for j in reversed(range(len(grid[0]))):
                if i+1<len(grid) and j+1<len(grid[0]):
                    memo[i][j] = min(memo[i+1][j],memo[i][j+1]) + grid[i][j]
                elif i + 1 < len(grid) and j + 1 == len(grid[0]):
                    memo[i][j] = memo[i+1][j] + grid[i][j]
                elif i + 1 == len(grid) and j + 1 < len(grid[0]):
                    memo[i][j]  = memo[i][j+1] + grid[i][j]
                elif i + 1 == len(grid) and j + 1 == len(grid[0]):
                    memo[i][j] = grid[i][j]

        return memo[0][0]
```
# [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/description/)
```python
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
```
