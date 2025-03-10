# import sys
# sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    # N: a,b로 나누어지는지 확인할 정수
    N = int(input())
    '''
    접근법
    정수 N이 1이상 9이하 인 두수 a,b의 곱으로 표현된다면 Yes, 아니라면 No를 출력한다.
    약수를 구해서 이 수가 1이상 9이하인지 판별하고 맞으면 Yes, 아니면 No 출력
    '''

    a = 0 # 약수 a
    b = 0 # 약수 b
    result = '' # 결과를 담아줄 변수
    for i in range(1, N + 1): # 1부터 N까지 반복
        if N % i == 0: # N을 i로 나눈 나머지가 0이라면 i는 약수이다.
            a = i # a = i로 설정
            if 1 <= a <= 9: # 만약 a가 1이상 9이하일 때
                b = N // a # N을 a로 나눈 몫은 b이다.
                if 1 <= b <= 9: # 만약 b가 1이상 9이하라면
                    result = 'Yes' # 결과는 Yes
                else: # 아니라면
                    result = 'No' # 결과는 No
    # 정답 출력
    print(f'#{tc} {result}')