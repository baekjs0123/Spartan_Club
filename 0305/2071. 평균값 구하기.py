# 테스트 케이스 갯수
T = int(input())
# T 만큼 반복
for tc in range(1, T + 1):
    # 입력되는 숫자 값 받아줄 변수
    arr = list(map(int, input().split()))
    # N = arr의 길이
    N = len(arr)
    # 모든 수를 더해줄 변수
    total = 0
    # N만큼 반복
    for i in range(N):
        # 순회하며 모든 수를 더해준다.
        total += arr[i]
    # 평균값을 담는다. round()를 사용,소숫점 첫째 자리에서 반올림한다
    avg = round(total / N)
    # 결과 출력
    print(f'#{tc} {avg}')
