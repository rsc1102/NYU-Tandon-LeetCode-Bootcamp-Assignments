# [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/description/)
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue = deque()
        queue.append(root)
        ans = []
        while len(queue):
            size = len(queue)
            temp = []
            while size:
                curr = queue.popleft()
                temp.append(curr.val)
                if curr.left is not None:
                    queue.append(curr.left)
                if curr.right is not None:
                    queue.append(curr.right)
                size-=1
            ans.append(temp)
        return ans
```

# [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/description/)
```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)

        for x in nums:
            counter[x]+=1

        heap = []
        for key in counter:
            heapq.heappush(heap,(-1*counter[key],key))
        
        ans = []
        while k:
            _ , key = heapq.heappop(heap)
            ans.append(key)
            k-=1
        return ans
```

# [Word Search II](https://leetcode.com/problems/word-search-ii/description/)
```python
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = defaultdict(dict)

        for word in words:
            node = trie
            for letter in word:
                if letter not in node:
                    node[letter] = {}
                node = node[letter]
            node["$"] = word

        n,m = len(board),len(board[0])
        ans = []

        def backtracking(i,j,parent):
            letter = board[i][j]
            curr = parent[letter]

            word_matched = curr.pop("$",False)
            if word_matched:
                ans.append(word_matched)
            
            board[i][j] = "#"

            for (x,y) in [(-1,0),(1,0),(0,-1),(0,1)]:
                if (i+x <0 or i+x == n or j+y<0 or j+y==m or board[i+x][j+y] not in curr):
                    continue
                backtracking(i+x,j+y,curr)

            board[i][j] = letter
            if not curr:
                parent.pop(letter)

        for i in range(n):
            for j in range(m):
                if board[i][j] in trie:
                    backtracking(i,j,trie)

        return ans
```
