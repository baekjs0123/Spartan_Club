# import sys
#
# sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    # N: 선택받은 사람 수, M: 붕어빵 만드는 시간, K: M초동안 만드는 붕어빵 갯수
    N, M, K = map(int, input().split())
    # 손님 도착시간 리스트
    people_department = list(map(int, input().split()))
    '''
    붕어빵을 만들고 N만큼 반복문을 돈다.
    time변수를 만들고 붕어빵이 처음 만들어지는데 필요한시간 M을 저장한다.
    그리고 time 보다 people_deratment[i]가 커지면 time + M을 해준다.
    그리고 붕어빵 갯수도 K만큼 증가시킨다.
    '''
    # 도착시간 순서대로 반복문을 돌리기 위해서 리스트를 정렬한다.
    people_department.sort()
    # 붕어빵 갯수
    fish_cake = 0
    # 정답 여부 담을 변수
    answer = ''
    # 붕어빵 만드는데 걸리는 시간
    time = M
    # 만약 도착시간이 가장 빠른 사람이 첫 붕어빵 만드는데 걸리는 시간
    # 보다 빨리 도착한다면 붕어빵이 없으므로 바로 불가능 출력
    if people_department[0] < M:
        answer = 'Impossible'
    # 아니라면
    else:
        # 사람 수 만큼 반복
        for i in range(N):
            # 만약 i 번째로 도착한 사람이 붕어빵 만드는데 걸린 시간보다
            # 늦다면 붕어빵 한번 더 구워야 하므로 time 을 M 추가하고
            # 붕어빵 갯수도 K개 추가한다.
            if people_department[i] >= time:
                time += M
                fish_cake += K
            # 여기는 time보다 도착시간이 작은 사람만 온다.
            # 여기 있는 사람들은 그냥 붕어빵을 1개씩 받아간다.
            fish_cake -= 1
            # 만약 붕어빵 갯수가 0보다 작아지면 바로 불가능 출력
            if fish_cake < 0:
                answer = 'Impossible'
                break
            # 아니라면
            else:
                # 가능
                answer = 'Possible'
    # 정답 출력
    print(f'#{tc} {answer}')