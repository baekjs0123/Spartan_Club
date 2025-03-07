# import sys
# sys.stdin = open('input.txt', 'r')
# 테스트 케이스 갯수
T = int(input())
# T만큼 반복
for tc in range(1, T + 1):
    # N: 돌갯수, M: 돌 바꿀 횟수
    N, M = map(int, input().split())
    # 초기상태
    default_status = list(map(int, input().split()))
    # ij : i와 j값을 리스트형태로 저장
    ij = [list(map(int, input().split())) for _ in range(M)]
    # M개의 줄이므로 M번 반복
    for i in range(M):
        # 바꿔야할 숫자
        change_color = default_status[ij[i][0] - 1]
        # 스타트 지점 인덱스 번호는 0부터니까 -1
        s = ij[i][0] - 1
        # 엔드 지점 = 스타트 지점 + j개의 돌
        e = s + ij[i][1]
        # 스타트부터 엔드까지 반복
        for j in range(s, e):
            # 유효성 검사 N보다 작을때만 돌 뒤집기
            if j < N:
                default_status[j] = change_color
    # 출력
    print(f'#{tc}', *default_status)
