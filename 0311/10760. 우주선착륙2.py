# import sys
# sys.stdin = open('input.txt', 'r')

# 유효성 검사
def is_valid():
    return 0 <= ni < N and 0 <= nj < M  # ni가 0이상이고, N보다 작고, nj가 0이상이고, M보다 작아야 Aij의 범위를 벗어나지 않는다.


T = int(input())
for tc in range(1, T + 1):
    # N: 행길이, M: 열 길이
    N, M = map(int, input().split())
    # 착륙지 지형 정보
    Aij = [list(map(int, input().split())) for _ in range(N)]
    # 후보지를 카운트할 변수
    candidate = 0
    # 델타배열 방향(상,하,좌,우, 좌상,우상, 좌하, 우하)
    di = [-1, 1, 0, 0, -1, -1, 1, 1]
    dj = [0, 0, -1, 1, -1, 1, -1, 1]

    for i in range(N):      # 행길이 N만큼 반복
        for j in range(M):  # 열길이 M만큼 반복
            cnt = 0         # 사진찍을 수 있는 장소 카운트 할 변수
            landing_point = Aij[i][j] # 현재 착륙지점을 기준으로 비교해야하기 때문에 변수 설정해준다.
            for k in range(8): # 델타 방향만큼 반복
                ni = i + di[k] # 다음 지점은 현재 지점 기준 + 델타방향 <- 현재지점과 비교하여 사진 촬영이 가능한지 확인할 지점
                nj = j + dj[k] # 다음 지점은 현재 지점 기준 + 델타방향 <- 현재지점과 비교하여 사진 촬영이 가능한지 확인할 지점
                if is_valid() and landing_point > Aij[ni][nj]: # 유효성 검사 이후 착륙지보다 고도가 낮으면 사진촬영가능
                    cnt += 1    # 카운트 + 1
            if cnt >= 4:    # 카운트가 4이상일때 후보지 1개 증가
                candidate += 1
    # 정답 출력
    print(f'#{tc} {candidate}')
