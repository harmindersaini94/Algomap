def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix) #6
        n = len(matrix[0]) #4

        # For Directions
        UP, RIGHT, LEFT, DOWN = 0,1,2,3
        UP_WALL = 0
        RIGHT_WALL = n
        DOWN_WALL = m
        LEFT_WALL = -1

        r, c = 0, 0        
        ans = []
        direction = RIGHT

        while len(ans) != m*n:
            if direction == RIGHT:
                while c < RIGHT_WALL:
                    ans.append(matrix[r][c])
                    c += 1
                c -= 1
                RIGHT_WALL -= 1
                r += 1
                direction = DOWN
            elif direction == DOWN:
                while r < DOWN_WALL:
                    ans.append(matrix[r][c])
                    r += 1
                r -= 1
                c -= 1
                DOWN_WALL -= 1
                direction = LEFT
            elif direction == LEFT:
                while c > LEFT_WALL:
                    ans.append(matrix[r][c])
                    c -= 1
                c += 1
                r -= 1
                LEFT_WALL += 1
                direction = UP
            elif direction == UP:
                while r > UP_WALL:
                    ans.append(matrix[r][c])
                    r -= 1
                r += 1
                c += 1
                UP_WALL += 1
                direction = RIGHT
        return ans
                
