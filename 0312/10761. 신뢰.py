# import sys
#
# sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    # 눌러야 하는 버튼의 갯수 N과 로봇이 눌러야하는 버튼 정보가 담긴 리스트
    arr = input().split()
    # 눌러야 하는 버튼의 갯수
    N = int(arr[0])

    # 로봇들의 시작 위치와 idle time 초기화
    b_start, o_start = 1, 1
    b_idle, o_idle = 0, 0
    # 총 시간
    total_time = 0

    # 명령을 순서대로 처리 (arr[1]부터, 두 칸씩)
    for i in range(1, len(arr), 2):
        # 로봇의 정보는 i번째에 담겨있고 눌러야할 버튼 = target은 i + 1번 째에 문자열로 담겨있다
        robot = arr[i]
        target = int(arr[i + 1])    # 문자열이므로 int로 변환해준다.
        # 만약 로봇이 블루 로봇이면
        if robot == 'B':
            # 블루 로봇이 목표 버튼까지 이동해야 할 거리
            distance = abs(target - b_start) # 음수가 나올 수도 있기때문에 절대값으로 씌워준다.
            # 이미 기다린 시간(b_idle)만큼 거리를 커버했으므로 추가 필요한 시간
            wait_time = max(distance - b_idle, 0)
            time_needed = wait_time + 1  # 이동 + 버튼 누르기 (1초)

            total_time += time_needed  # 총 시간 갱신
            b_start = target  # 블루 위치 갱신
            b_idle = 0  # 블루 idle time 초기화
            o_idle += time_needed  # 오렌지는 이 시간 동안 이동 가능
        else:  # robot == 'O'
            # 오렌지 로봇이 목표 버튼까지 이동해야 할 거리
            distance = abs(target - o_start) # 음수가 나올 수도 있기때문에 절대값으로 씌워준다.
            # 이미 기다린 시간(o_idle)만큼 거리를 커버했으므로 추가 필요한 시간
            wait_time = max(distance - o_idle, 0)
            time_needed = wait_time + 1  # 이동 + 버튼 누르기 (1초)

            total_time += time_needed # 총 시간 갱신
            o_start = target # 오렌지 위치 갱신
            o_idle = 0 # 오렌지 idle time 초기화
            b_idle += time_needed  # 블루는 이 시간 동안 이동 가능
    # 정답 출력
    print(f'#{tc} {total_time}')
