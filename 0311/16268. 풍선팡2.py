# import sys
# sys.stdin = open('input.txt', 'r')

# ni, nj가 범위를 벗어나지 않도록 유효성 검사
def is_valid():
    return 0 <= ni < N and 0 <= nj < M

T = int(input())
for tc in range(1, T + 1):
    # N은 행 갯수, N은 열 갯수
    N, M = map(int, input().split())
    # 풍선 정보 담는 행렬
    balloons = [list(map(int, input().split())) for _ in range(N)]

    # 최대값 담아줄 변수
    max_cnt = 0

    # 상하좌우
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    for i in range(N):  # 행 갯수만큼 반복
        for j in range(M):  # 열 갯수만큼 반복
            cnt = 0  # 매번 반복 돌때마다 cnt 0으로 초기화
            distance = balloons[i][j]  # 거리는 현재 터트린 풍선에 담겨있는 꽃가루 수
            cnt += balloons[i][j]  # 카운트에 현재 터트린 풍선의 꽃가루 수를 먼저 담아준다.
            for k in range(4):  # 델타배열탐색을 위해 방향 4번 돌린다.
                    ni = i + di[k]  # 다음 위치는 현재 위치 + 델타배열 방향
                    nj = j + dj[k]  # 다음 위치는 현재 위치 + 델타배열 방향
                    if is_valid():
                        cnt += balloons[ni][nj]
            # 만약 max_cnt < cnt가 크면
            if max_cnt < cnt:
                max_cnt = cnt  # max_cnt를 cnt로 바꿔준다.
    # 정답 출력
    print(f'#{tc} {max_cnt}')