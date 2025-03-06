# import sys
# sys.stdin = open('input.txt', 'r')
# 테스트 케이스 갯수
T = int(input())
# T만큼 반복
for tc in range(1, T + 1):
    # 메모리값 받기
    memory = list(map(int, input()))
    # 메모리 길이
    N = len(memory)
    # 초기상태
    default_status = [0] * N
    # 몇번 돌리는 지 카운트
    cnt = 0
    # N만큼 반복
    for i in range(N):
        # 디폴트랑 메모리랑 다르면
        if default_status[i] != memory[i]:
            # 디폴트값 1일때
            if default_status[i]:
                # 횟수 + 1
                cnt += 1
                # i부터 N까지 모두 0
                for j in range(i, N):
                    default_status[j] = 0
            # 디폴트 0이면
            else:
                # 횟수 + 1
                cnt += 1
                # i부터 N까지 모두 1
                for j in range(i, N):
                    default_status[j] = 1
    # 정답 출력
    print(f'#{tc} {cnt}')