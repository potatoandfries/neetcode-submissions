class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix[:] = list(zip(*matrix[::-1]))
        #matrix[::-1]  reverses the order of the rows:
        #zip(*matrix[::-1]) transposes the matrix, swapping rows and columns:


