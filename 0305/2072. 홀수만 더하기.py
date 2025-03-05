# 테스트 케이스 갯수
T = int(input())
# 테스트 케이스 횟수 만큼 반복문 1부터 돌기 때문에
# T + 1까지 범위 설정
for tc in range(1, T + 1):
    # 숫자 리스트 담는 변수
    arr = list(map(int, input().split()))
    # 홀수만 더해서 담아줄 변수
    num_sum = 0
    # arr의 갯수 만큼 반복문
    for i in range(len(arr)):
        # arr의 i번째 요소를 2로 나눈 나머지가 1이면 홀수
        if arr[i] % 2:
            # 홀수 일때마가 더해준다.
            num_sum += arr[i]
    # 결과를 출력한다.
    print(f'#{tc} {num_sum}')