class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hashmap = defaultdict(list)

        for item in prerequisites:
            hashmap[item[0]].append(item[1])
            if item[0] in hashmap[item[1]]:
                return False
            
        def dfs(course):
            if course in self.seen or hashmap[course] == []:
                return
            if course in self.stack:
                self.ans = False
                return
            
            self.stack.add(course)
            for preq in hashmap[course]:
                dfs(preq)
            self.stack.remove(course)
            self.seen.add(course)

        self.ans = True
        self.seen = set()
        for i in range(numCourses):
            self.stack = set()
            dfs(i)
            if self.ans == False:
                return False

        return self.ans 
