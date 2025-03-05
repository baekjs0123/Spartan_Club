# 테스트 케이스 갯수
T = int(input())
# T만큼 반복
for tc in range(1, T + 1):
    # N: Ai의 길이, M: Bj의 길이
    N, M = map(int, input().split())
    # Ai 입력받기
    Ai = list(map(int, input().split()))
    # Bj 입력받기
    Bj = list(map(int, input().split()))
    len_A = len(Ai)
    len_B = len(Bj)
    short_arr = 0
    long_arr = 0
    if len_A < len_B:
        short_arr = Ai
        long_arr = Bj
    else:
        short_arr = Bj
        long_arr = Ai



