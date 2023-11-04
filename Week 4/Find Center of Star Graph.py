class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        connections = defaultdict(int)
        for item in edges:
            connections[item[0]] += 1
            connections[item[1]] += 1
        
        for key in connections:
            if connections[key] == len(connections) -1:
                return key
        return 0
