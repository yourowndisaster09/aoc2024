import sys
import time

class Part2:
    VECTOR = {
        0: (-1, 0),
        1: (0, 1),
        2: (1, 0),
        3: (0, -1)
    }

    def __init__(self, grid):
        self.grid = grid
        self.m = len(grid)
        self.n = len(grid[0])
    
    def findStart(self):
        for r in range(self.m):
            for c in range(self.n):
                if grid[r][c] == '^':
                    return (r, c), 0
                elif grid[r][c] == '>':
                    return (r, c), 1
                elif grid[r][c] == 'v':
                    return (r, c), 2
                elif grid[r][c] == '<':
                    return (r, c), 3
    
    def _setObstacle(self, coor):
        r, c = coor
        gridCopy = [row.copy() for row in self.grid]
        gridCopy[r][c] = '#'
        return gridCopy
    
    def _valid(self, coor):
        r, c = coor
        return r > -1 and r < self.m and c > -1 and c < self.n
    
    def _rotate(self, direction):
        return (direction + 1) % 4
    
    def _forward(self, coor, direction):
        r, c = coor
        dr, dc = self.VECTOR[direction]
        return (r + dr, c + dc)
    
    def countObstacles(self):
        # [print(row) for row in self.grid]
        # print()
        start = self.findStart()
        coor, direction = start
        possibleObstacles = set()

        while coor:
            nextDirection = direction
            nextCoor = self._forward(coor, direction)
            if not self._valid(nextCoor):
                break
            while self.grid[nextCoor[0]][nextCoor[1]] == '#':
                nextDirection = self._rotate(nextDirection)
                if nextDirection == direction:
                    nextCoor = None
                    break
                nextCoor = self._forward(coor, nextDirection)
                if not self._valid(nextCoor):
                    nextCoor = None
                    break
            if not nextCoor:
                break
            if nextCoor != start[0]:
                possibleObstacles.add(nextCoor)
            coor, direction = nextCoor, nextDirection
        # print(f"Exiting at {(coor[1] + 1, coor[0] + 1)} with direction {direction}")


        count = 0
        for obstacle in possibleObstacles:
            # print(f"Checking obstacle at {(obstacle[1] + 1, obstacle[0] + 1)}")
            if self._subtraverse(self._setObstacle(obstacle), start[0], start[1]):
                count += 1
                # print(f"  ! obstacle at {(obstacle[1] + 1, obstacle[0] + 1)}")
        return count
    
    def _subtraverse(self, grid, coor, direction):
        visited = [[[False for _ in range(4)] for _ in range(self.n)] for _ in range(self.m)]
        # [print(row) for row in grid]

        while coor:
            if visited[coor[0]][coor[1]][direction]:
                return True
            visited[coor[0]][coor[1]][direction] = True
            nextDirection = direction
            nextCoor = self._forward(coor, direction)
            if not self._valid(nextCoor):
                break
            while grid[nextCoor[0]][nextCoor[1]] == '#':
                nextDirection = self._rotate(nextDirection)
                if nextDirection == direction:
                    nextCoor = None
                    return True
                nextCoor = self._forward(coor, nextDirection)
                if not self._valid(nextCoor):
                    nextCoor = None
                    break
            if not nextCoor:
                break
            coor, direction = nextCoor, nextDirection
        return False


if __name__ == "__main__":
    grid = []
    with open(sys.argv[1], 'r') as f:
        for line in f:
            l = line.strip()
            if not l:
                break
            row = []
            for letter in l:
                row.append(letter)
            grid.append(row)

        if sys.argv[2] == "part1":
            pass
            # print(f'Part 1 Answer = {part1(grid)}')
        if sys.argv[2] == "part2":
            print(f'Part 2 Answer = {Part2(grid).countObstacles()}')