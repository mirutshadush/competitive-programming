class UnionFind:
    def __init__(self, size: int = 26):
        self.size = self.numComponents = size
        self.id = [i for i in range(size)]
        self.sz = [1 for i in range(size)]
    def connected(self, a: int, b: int):
        return self.find(a) == self.find(b)
    def find(self, a: int)-> int:
        root = a
        while self.id[root] != root:
            root = self.id[root]
        return root
    def unify(self, a: int, b: int):
        root1 = self.find(a)
        root2 = self.find(b)
        if root1 == root2: return
        if self.sz[root1] < self.sz[root2]:
            self.sz[root2] += self.sz[root1]
            self.id[root1] = root2
        else:
            self.sz[root1] += self.sz[root2]
            self.id[root2] = root1
            
        
    
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        un = UnionFind()
        for e in equations:
            l1, cmp, l2 = e[0], e[1], e[3]
            if cmp == "!":
                continue
            un.unify(ord(l1)-ord('a'), ord(l2)-ord('a'))
        for e in equations:
            l1, cmp, l2 = e[0], e[1], e[3]
            if cmp == "=":
                continue
            if un.connected(ord(l1)-ord('a'), ord(l2)-ord('a')):
                return False
        return True
