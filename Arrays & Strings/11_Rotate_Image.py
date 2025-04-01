def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        """
        Step 1 -> Transpose the matrix, means make each Row a column
        Step 2 -> swap the elements
        """
        for r in range(n):
            for c in range(r+1,n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        # Horizontal Reflection
        for i in range(0,n):
            matrix[i].reverse()


        