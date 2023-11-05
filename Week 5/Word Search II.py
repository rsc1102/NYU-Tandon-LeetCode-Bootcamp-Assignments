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
