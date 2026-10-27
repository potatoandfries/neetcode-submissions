class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix[:] = [list(reversed(x)) for x in zip(*matrix)]