# import sys
# sys.stdin = open('input.txt', 'r')

def is_valid():
    return 0 <= ni < N and 0 <= nj < M

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    balloons = [list(map(int, input().split())) for _ in range(N)]
    # print(balloons)
    max_cnt = 0
    di = [-1,1,0,0]
    dj = [0,0,-1,1]
    for i in range(N):
        for j in range(M):
            cnt = 0
            distance = balloons[i][j]
            cnt += balloons[i][j]
            for k in range(4):
                for l in range(1, distance + 1):
                    ni = i + di[k] * l
                    nj = j + dj[k] * l
                    if is_valid():
                        cnt += balloons[ni][nj]
            if max_cnt < cnt:
                max_cnt = cnt
    print(f'#{tc} {max_cnt}')