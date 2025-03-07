# import sys
# sys.stdin = open('input.txt', 'r')
# 테스트 케이스 갯수
T = int(input())
# T번 반복
for tc in range(1, T + 1):
    # N: 돌 갯수 M: M번 뒤집기
    N, M = map(int, input().split())
    # 초기상태
    default_status = list(map(int, input().split()))
    # i,j 리스트에 담기
    ij = [list(map(int, input().split())) for _ in range(M)]
    # M번 반복
    for i in range(M):
        # s는 비교를 시작할 중심 인덱스
        s = ij[i][0] - 1
        # e는 양옆으로 뒤집을 돌 갯수
        e = ij[i][1]
        # 1개부 뒤집어야 하므로 1 ~ e까지 반복돌려야함. e도 포함해야해서 e + 1
        for j in range(1, e + 1):
            # 인덱스 유효성 검사 먼저 하고 s로 부터 양옆의 돌이 같으면
            if 0 <= s - j and s + j < N and default_status[s - j] == default_status[s + j]:
                # 1일때
                if default_status[s - j]:
                    # 0으로 뒤집는다.
                    default_status[s - j] = 0
                    default_status[s + j] = 0
                # 0일 때
                else:
                    # 1로 뒤집는다.
                    default_status[s - j] = 1
                    default_status[s + j] = 1
    # 결과 출력
    print(f'#{tc}', *default_status)

