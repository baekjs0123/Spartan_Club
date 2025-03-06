# import sys
# sys.stdin = open('input.txt', 'r')

# T = 테스크 케이스 갯수
T = int(input())
# T만큼 반복
for tc in range(1, T + 1):
    # N: 소인수분해 할 숫자
    N = int(input())
    # pow_cnt: 몇제곱인지 카운트할 변수
    pow_cnt = 0
    # 문제의 조건이 N=2^a x 3^b x 5^c x 7^d x 11^e 로 정해져 있으므로
    # numbers에 2,3,5,7,11을 담고 반복을 돌린다.
    numbers = [2,3,5,7,11]
    # 정답을 출력할때 사용할 변수
    answer = []
    # numbers의 길이만큼 반복
    for i in range(len(numbers)):
        # number가 바뀔때마다 pow_cnt는 초괴화 되어야한다.
        pow_cnt = 0
        # numbers[i]가 N보다 작거나 같을때만 반복한다.
        while numbers[i] <= N:
            # N을 numbers[i]로 나눈 나머지가 0이면 나눈다.
            if N % numbers[i] == 0:
                # N을 numbers[i]로 나눈 몫을 N으로 재할당한다.
                N //= numbers[i]
                # 이때 제곱수가 1증가한다.
                pow_cnt += 1
            # 아니라면 break로 탈출
            else:
                break
        # answer에 pow_cnt를 추가해준다.
        answer.append(pow_cnt)
    # 결과를 출력한다.
    print(f'#{tc}', *answer)