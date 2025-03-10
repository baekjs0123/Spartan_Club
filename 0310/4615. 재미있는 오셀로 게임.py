# import sys
#
# sys.stdin = open('input.txt', 'r')

# 보드의 범위를 벗어나지 않도록 유효성 검사
def is_valid():
    return 0 <= ni < N and 0 <= nj < N

T = int(input())
for tc in range(1, T + 1):
    # N: 한 변의 길이, M: 돌을 놓는 횟수
    N, M = map(int, input().split())
    # 보드판 만들기
    board = [[0] * N for _ in range(N)]
    # 초기에 셋팅된 돌이 있기 때문에 그 돌을 미리 적어주고 시작한다.
    # 초기에 셋팅된 돌은 항상 보드의 중앙에 있다.
    # 그러면 N // 2 - 1을 하면 중앙 인덱스를 찾을 수 있다.
    default_stone_idx = N // 2 - 1
    board[default_stone_idx][default_stone_idx] = 2  # 보드의 초기 백돌 위치
    board[default_stone_idx][default_stone_idx + 1] = 1  # 보드의 초기 흑돌 위치
    board[default_stone_idx + 1][default_stone_idx] = 1  # 보드의 초기 흑돌 위치
    board[default_stone_idx + 1][default_stone_idx + 1] = 2  # 보드의 초기 백돌 위치
    '''
    접근법
    흑돌차례일 경우 2를 찾고 2의 양옆 중 한곳에 1이 있을 경우
    반대편에 흑돌을 둘 수 있다. 이때 사이에 끼인 백돌은 흑돌로 바뀐다.
    
    백돌차례일 경우 1을 찾고 1의 양옆 중 한곳에 2가 있을 경우
    반대편에 흰돌을 둘 수 있다. 이 때 사이에 끼인 흑돌은 백돌로 바뀐다.
    
    돌을 놓을 곳이 없다면 상대편이 돌을 놓게 된다.
    보드에 빈 곳이 없거나 양 플레이어 모두 돌을 놓을 곳이 없으면 게임이 끝나고
    그 때 보드에 있는 돌의 개수가 많은 플레이어가 승리하게 된다.
    
    이 문제에서는 돌놓을 좌표가 주어지기 때문에 돌을 놓고 델타탐색하며 상대돌이 있다면
    해당 델타의 방향으로 계속 탐색할때 값이 0이 아니면 내 돌이 나올때 까지 쭉 색깔을 바꿔준다.
    0이 나오면 델타 방향을 바꿔준다. 그리고 해당 델타 방향으로 끝까지 탐색을 했을 때 내돌이 안나오면
    델타 방향을 바꿔준다.
    그리고 게임이 끝나면 반복문을 돌면서 돌의 색깔을 카운팅하고 흑돌, 백돌 갯수를 출력한다.
    '''
    di = [-1,1,0,0,-1,-1,1,1] # 상,하, 좌, 우, 상좌, 상우, 하좌, 하우
    dj = [0,0,-1,1,-1,1,-1,1] # 상,하, 좌, 우, 상좌, 상우, 하좌, 하우

    # M번 반복
    for i in range(M):
        # x는 x좌표, y는 y좌표, color는 돌 색깔
        x, y, color = map(int, input().split())
        # 인덱스 번호는 0부터 시작이므로 1씩 빼준다
        x, y = x - 1, y - 1
        board[x][y] = color # 보드의 x,y 좌표를 color로 바꿔준다.
        # 델타 반복
        for j in range(8):
            ni = x + di[j]  # ni = x + di[j]로 정해주어 델타 배열 탐색을 한다.
            nj = y + dj[j]  # nj = x + dj[j]로 정해주어 델타 배열 탐색을 한다.
            stones_to_flip = []     # 뒤집어야 할 돌의 좌표를 담을 리스트
            # 유효성 검사 결과 True이면서 board[ni][nj]이 0과 color가 아니면 반복
            while is_valid() and board[ni][nj] not in [0, color]:
                # stones_to_flip에 (ni, nj)를 추가해준다.
                stones_to_flip.append((ni, nj))
                # ni, nj를 해당 델타 방향으로 쭉 더해준다.
                ni += di[j]
                nj += dj[j]
            # 유효성 검사 and 보드의 ni,nj가 color일 때 그 사이에 있는 돌들을 모두 color로 바꿔준다.
            if is_valid() and board[ni][nj] == color:
                # stones_to_flip을 순회하며 매번 flip_x, flip_y를 뽑아낸다.
                for flip_x, flip_y in stones_to_flip:
                    # board의 flip_x,flip_y를 color로 바꿔준다.
                    board[flip_x][flip_y] = color
    # 여기까지 오면 모든 돌을 바꾼 후이다.
    black_cnt = 0   # 검은돌 카운팅 할 변수
    white_cnt = 0   # 흰돌 카운팅 할 변수
    # 이중 for문 돌면서 각 요소를 검사한다.
    for i in range(N):
        for j in range(N):
            # 만약 요소가 1이면 흑돌
            if board[i][j] == 1:
                black_cnt += 1      # 흑돌 카운트 + 1
            # 만약 요소가 2이면 흰돌
            if board[i][j] == 2:
                white_cnt += 1      # 흰돌 카운트 + 1
    # 정답 출력
    print(f'#{tc} {black_cnt} {white_cnt}')







