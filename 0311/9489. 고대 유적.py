import sys
sys.stdin = open('input.txt', 'r')

# # 유효성 검사
# def is_valid():
#     return 0 <= ni < N and 0 <= nj < M
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     # N: 행길이, M: 열길이
#     N, M = map(int, input().split())
#     # data = 땅속 구조물 위치 정보
#     data = [list(map(int, input().split())) for _ in range(N)]
#
#     # 델타 상하좌우
#     di = [-1,1,0,0]
#     dj = [0,0,-1,1]
#
#     # 최대 길이 담아줄 변수
#     max_len = 0
#     for i in range(N): # 행길이 만큼 반복
#         for j in range(M): # 열길이 만큼 반복
#             flag = False # while문을 돌릴 때 쓸 조건
#             if data[i][j] == 1: # 데이터의 i,j가 1이면,
#                 for k in range(4): # 델타 방향으로 탐색한다.
#                     remains_len = 1 # 이때 remain_len을 1로 초기화한다.
#                     ni = i + di[k] # 델타로 탐색할 지점은 현재위치 + 델타방향
#                     nj = j + dj[k] # 델타로 탐색할 지점은 현재위치 + 델타방향
#                     # 유효성 검사 하고 data의 (ni,nj)가 1이라면
#                     if is_valid() and data[ni][nj] == 1:
#                         # 플래그를 True로 바꿔서 while문을 돌릴 준비를 한다.
#                         flag = True
#                         # 이때 remain_len을 +1 해준다.
#                         remains_len += 1
#                         while flag:     # flag가 트루면 무한 루프
#                             ni += di[k] # 다음 위치 참색을 해당 디렉션 방향으로 쭉 탐색한다.
#                             nj += dj[k] # 다음 위치 참색을 해당 디렉션 방향으로 쭉 탐색한다.
#                             # 만약 유효성 검사 결과 범위를 벗어났거나 데이터의 ni,nj가 0이면 플래그를 False로 초기화한다.
#                             if not is_valid() or data[ni][nj] == 0:
#                                 flag = False
#                             else: # 아니라면
#                                 remains_len += 1 # remains_len +1 해준다.
#                         # 최대값과 비교하여 더크면 최대값으로 설정.
#                         if max_len < remains_len:
#                             max_len = remains_len
#     # 정답 출력
#     print(f'#{tc} {max_len}')

# 다른 풀이방법
T = int(input())
for tc in range(1, T + 1):
    # N: 행길이, M: 열길이
    N, M = map(int, input().split())
    # data = 땅속 구조물 위치 정보
    data = [list(map(int, input().split())) for _ in range(N)]
    # 최대 길이 담을 변수
    max_len = 0
    # 반복문 안에서 각 길이 더해줄 변수
    cnt = 0

    # 행 우선 순회
    for i in range(N): # 행길이 만큼 반복
        for j in range(M): # 열 길이 만큼 반복
            if data[i][j] == 1: # 데이터의 i,j가 1이면
                cnt += 1 # 카운트 + 1
            # 종료조건
            # j == M - 1이라는 뜻은 행의 끝에 도착했다는 말.
            # data의 i,j가 0이면 다음에 1이 나올 경우를 대비해 최대값을 비교해주고 cnt를 0으로 초기화해야함
            if j == M - 1 or data[i][j] == 0:
                # 최대값 비교 후 최대값 저장
                if max_len < cnt:
                    max_len = cnt
                # 카운트 초기화
                cnt = 0
    # 열 우선 순회
    for j in range(M): # 열 길이 만큼 반복
        for i in range(N): # 행 길이 만큼 반복
            if data[i][j] == 1: # 데이터의 i,j가 1이면
                cnt += 1 # 카운트 + 1
            # 종료조건
            # i == N - 1이라는 뜻은 열의 끝에 도착했다는 말.
            # data의 i,j가 0이면 다음에 1이 나올 경우를 대비해 최대값을 비교해주고 cnt를 0으로 초기화해야함
            if i == N - 1 or data[i][j] == 0:
                # 최대값 비교 후 최대값 저장
                if max_len < cnt:
                    max_len = cnt
                # 카운트 초기화
                cnt = 0
    # 정답 출력
    print(f'#{tc} {max_len}')
