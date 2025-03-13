# import sys
#
# sys.stdin = open('input.txt', 'r')

# 경사로를 설치할 수 있는지 판단하는 함수 정의
def can_runway(arr, N, X):
    # 경사로가 이미 설치된 위치를 표시하는 리스트 (0: 미설치, 1: 설치됨)
    used = [False] * N
    # 0번 인덱스부터 N-2번 인덱스까지 검사 (현재 칸과 다음 칸을 비교)
    for i in range(N - 1):
        # 만약 현재 칸과 다음 칸의 높이가 동일하면 별도 처리 없이 다음 칸으로 이동
        if arr[i] == arr[i + 1]:
            continue
        # 다음 칸이 현재 칸보다 1 높아진 경우 (오르막 경사)
        elif arr[i + 1] - arr[i] == 1:
            # 경사로를 뒤쪽(현재 위치부터 과거 X칸)으로 설치할 수 있는지 확인
            # i부터 i - X + 1 까지 총 X칸이 모두 현재 칸의 높이여야 함
            for j in range(i, i - X, -1):  # i, i-1, ..., i-X+1 까지 역순으로 확인
                # 만약 배열 범위를 벗어나거나 높이가 일치하지 않거나 이미 경사로가 설치되었다면 설치 불가
                if j < 0 or arr[j] != arr[i] or used[j]:
                    return False
                # 경사로가 설치되었다고 표시
                used[j] = True
        # 다음 칸이 현재 칸보다 1 낮은 경우 (내리막 경사)
        elif arr[i] - arr[i + 1] == 1:
            # 경사로를 앞으로(다음 칸부터 X칸) 설치할 수 있는지 확인
            # i+1부터 i+X 까지 총 X칸이 모두 동일한 높이여야 함
            for j in range(i + 1, i + 1 + X):
                # 만약 배열 범위를 벗어나거나 높이가 일치하지 않거나 이미 경사로가 설치되었다면 설치 불가
                if j >= N or arr[j] != arr[i + 1] or used[j]:
                    return False
                # 경사로가 설치되었다고 표시
                used[j] = True
        # 높이 차이가 1보다 크면 경사로 설치 자체가 불가능하므로 바로 False 반환
        else:
            return False
    # 모든 검사를 통과하면 활주로를 건설할 수 있는 경로임을 의미하므로 True 반환
    return True


# 테스트 케이스 수 입력 (SWEA 문제는 여러 테스트 케이스로 구성됨)
T = int(input())

# 각 테스트 케이스에 대해 처리
for tc in range(1, T + 1):
    # N: 격자 크기, X: 경사로 길이 입력
    N, X = map(int, input().split())
    # N x N 크기의 지형 정보를 2차원 리스트로 입력받음
    grid = [list(map(int, input().split())) for _ in range(N)]

    # 활주로를 건설할 수 있는 경우의 수를 저장할 변수 초기화
    cnt = 0

    # 1. 각 행(row)에 대해 활주로 건설 가능 여부 판단
    for i in range(N):
        # 현재 행의 정보를 그대로 전달하여 경사로 설치가 가능한지 검사
        if can_runway(grid[i], N, X):
            cnt += 1  # 가능하다면 경우의 수 증가

    # 2. 각 열(column)에 대해 활주로 건설 가능 여부 판단
    for j in range(N):
        # j번째 열의 정보를 리스트로 추출 (각 행의 j번째 원소)
        col = [grid[i][j] for i in range(N)]
        # 추출한 열 정보를 인자로 전달하여 활주로 설치 가능 여부 검사
        if can_runway(col, N, X):
            cnt += 1  # 가능하면 경우의 수 증가

    # 정답 출력
    print(f"#{tc} {cnt}")
