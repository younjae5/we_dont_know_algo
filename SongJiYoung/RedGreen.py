from collections import deque
import sys
pic = []
temp = []
check = []

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def bfs(r, c):
    queue = deque()
    queue.append((r,c))
    first = pic[r][c]
    while len(queue) != 0:
        #queue에서 첫번째 항목 pop
        r = queue[0][0]
        c = queue[0][1]
        queue.popleft()
        check[r][c] = 1
        #상하좌우 확인
        for m in range(4):
            nx = r + dx[m]
            ny = c + dy[m]
            if (nx < 0 or nx >= n or ny < 0 or ny >= n):
                continue
            if check[nx][ny]:
                continue
            if (pic[nx][ny] == first):
                check[nx][ny] = 1
                queue.append((nx, ny))


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    for i in range(n):
        line = list(input().strip())
        pic.append(line)
    check = [[0] * n for i in range(n)]
    ans = 0
    rans = 0
    for i in range(n):
        for j in range(n):
            if check[i][j] == 0:
                bfs(i, j)
                ans = ans + 1
    for i in range(n):
        for j in range(n):
            if pic[i][j] == "G":
                pic[i][j] = "R"
    check = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if check[i][j] == 0:
                bfs(i, j)
                rans = rans + 1
    print(ans, rans)