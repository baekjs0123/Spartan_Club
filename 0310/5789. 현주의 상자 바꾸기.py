# import sys
# sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    # N: 상자 갯수, Q: Q번동안 상자 변경
    N, Q = map(int, input().split())
    boxes = [0] * N # 처음 박스들의 상태를 상자의 갯수 N만큼 만들어준다.
    for i in range(Q): # Q번 실행하므로 Q번 반복
        L, R = map(int, input().split()) # 각 반복을 돌때 마다 시작값 L과 끝값 R을 받는다.
        for j in range(L - 1, R): # j는 시작값 인덱스인  L - 1부터 끝 값 인덱스인 R -1까지 돌아야한다.
            boxes[j] = i + 1 # 박스의 j번째는 i이다. 근데 i는 0부터 시작했으므로 문제는 1부터 시작하기에 + 1로 한다.
    # 정답 출력
    print(f'#{tc}', *boxes)