# import sys
# sys.stdin = open('input.txt', 'r')

# 테스트 케이스 갯수
T = int(input())
# T만큼 반복
for tc in range(1, T + 1):
    # N: 농장의 크기
    N = int(input())
    # farm_value: 농장의 가치를 2차원 배열로 입력
    farm_value = [list(map(int, input())) for _ in range(N)]
    '''
    농장의 크기는 항상 홀수, 수확은 항상 농장의 크기에 딱맞는 정사각형 마름모 형태.
    이때 농작물의 가치는?
    
    일단 행기준으로보면 0번행의 농장의 중심 인덱스만 더해준다.
    그리고 한 줄씩 내려갈 때 마다 좌우로 +-1 씩 범위가 넓어지고 행번호가 중심이되면
    다시 좌우로 1칸씩 줄어든다.
    '''
    # 중심 인덱스 번호, 농장의 크기는 항상 홀수 이므로
    # 2로 나눈 몫을 구하면 그게 중심인덱스 번호이다
    center_index = N // 2
    # 농장의 모든 가치를 더해줄 변수
    value_sum = 0
    # 이중 반복을 돌릴건데 행은 N만큼 돌리고 열은 i가 중심 인덱스보다 작거나 같을때와
    # 그리고 중심인덱스 보가 클때로 나눠서 열을 계산한다.
    for i in range(N):
        # 매 행의 중심 인덱스 값을 먼저 더해준다.
        value_sum += farm_value[i][center_index]
        # 만약 행번호가 중심인덱스보다 작거나 같다면
        if i <= center_index:
            # 열은 중심 인덱스를 기준으로 행번호가 증가 할때마다
            # 양옆으로 1칸씩 더해준다.
            # 그러기 위해서 i를 이용하여 j의 범위를 1, i + 1로 정한다.
            for j in range(1, i + 1):
                # 인덱스 범위 유효성 검사
                if 0 <= center_index - j and center_index + j < N:
                    # 중심인덱스 기준 양옆으로 +-j만큼 더해준다.
                    value_sum += farm_value[i][center_index - j] + farm_value[i][center_index + j]
        # 행 번호가 중심인덱스 값보다 클 때
        else:
            # 이때는 1칸씩 줄어야 하므로 증가하는 행번호 i를 이용하여
            # j의 범위를 N - i까지로 정한다.
            for j in range(1, N - i):
                # 유효성 검사
                if 0 <= center_index - j and center_index + j < N:
                    # 중심인덱스 기준 양옆으로 +-j만큼 더해준다.
                    value_sum += farm_value[i][center_index - j] + farm_value[i][center_index + j]
    # 정답 출력
    print(f'#{tc} {value_sum}')





