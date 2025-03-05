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
    # Ai의 길이
    len_A = len(Ai)
    # Bi의 길이
    len_B = len(Bj)
    # 만약 Ai가 Bj보다 작다면 short_arr = Ai, long_arr = Bj
    if len_A < len_B:
        # 짧은 배열은 Ai
        short_arr = Ai
        # 긴 배열은 Bj
        long_arr = Bj
    #  Ai가 Bj보다 크다면 short_arr = Bj, long_arr = Ai
    else:
        # 짧은 배열은 Bj
        short_arr = Bj
        # 긴 배열은 Ai
        long_arr = Ai
    # 곱의 최대값을 담을 변수
    max_total = 0
    # 큰 수와 작은수를 구하긴 했지만 간결하게 쓰고 싶어서
    # N - M에 abs()를 씌워 절대값에서 + 1로 범위를 설정해주었다.
    # for i in range(len(long_arr) - len(short_arr) + 1): 로 적어주어도 똑같다.
    # 슬라이딩 윈도우 기법으로 반복을 돈다.
    for i in range(abs(N - M) + 1):
        # total을 초기화
        total = 0
        # 짧은 배열의 수만큼 반복을 돌며 곱한뒤 더해줄것이다.
        for j in range(len(short_arr)):
            # 토탈에 짧은 배열의 요소와 긴 배열의 요소를 곱하고 더해준다.
            total += short_arr[j] * long_arr[i + j]
        # 맥스 토탈 보다 토탈이 더 크면
        if max_total < total:
            # 맥스토탈을 토탈로 바꿔준다.
            max_total = total
    # 결과를 출력한다.
    print(f'#{tc} {max_total}')