class Solution:
    def minDominoRotations(self, a: List[int], b: List[int]) -> int:
        size = len(a)
        x,y = None,None
        if all([a[0] in (a[i], b[i]) for i in range(size)]):
            x = min(size-a.count(a[0]), size - b.count(a[0]))
        if all([b[0] in (a[i], b[i]) for i in range(len(b))]):
            y = min(size-a.count(b[0]), size - b.count(b[0]))
        # print(x,y)
        if x is None:
            if y is None:
                return -1
            else:
                return y
        else:
            if y is None:
                return x
            else:
                return min(x,y)
