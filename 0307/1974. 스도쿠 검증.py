# import sys
# sys.stdin = open('input.txt', 'r')
# 테스트 케이스 갯수
T = int(input())
# T만큼 반복
for tc in range(1, T + 1):
    # 스도쿠 행렬로 입력받기
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    '''
    접근법
    이중반복문을 돌면서 매행과 열을 검사하고 set을 써서 중복 숫자 제거한 후
    행의 길이, 열의 길이, 3 X 3의 크기가 9가 아니면 0, 9면 1 출력
    '''
    # 초기값을 1로 정하고 만약 스도쿠 검사 결과가 올바르면 그대로 1 출력 아니면 0으로 바꿔서 출력한다.
    result = 1
    # 행 검사
    for i in range(9):
        # 행길이는 set()을써서 중복되는 숫자가 있으면 길이가 9보다 작아지게 된다.
        row_len = len(set(sudoku[i]))
        # 열의 요소를 담을 변수
        col = []
        # 열 길이 초기화
        col_len = 0
        # 행 요소 길이가 9보다 작다는 것은 스도쿠에 중복되는 숫자가 있다는 뜻
        if row_len < 9:
            # result를 0으로 바꿔준다.
            result = 0
        # 열 검사
        for j in range(9):
            # col에 스도쿠 열의 요소를 넣어준다.
            col.append(sudoku[j][i])
            # 열의 길이 역시 set을 써서 중복요소를 지워준다.
            col_len = len(set(col))
        # 열의 길이가 9보다 작다면 result = 0
        if col_len < 9:
            result = 0
    # 3 X 3 검사
    # i를 0부터 8까지 3씩 증가해줘서 3 X 3 박스의 기준이 될 숫자를 정해준다.
    for i in range(0, 9, 3):
        # 3 X 3 요소를 담아줄 변수 sq
        sq = []
        # sq길이 초기화
        sq_len = 0
        # sq의 행번호 = j
        for j in range(i, i + 3):
            # sq의 열번호 = k
            for k in range(i, i + 3):
                # sq에 3 X 3 박스의 요소 추가
                sq.append(sudoku[j][k])
                # sq 의 길이 역시 set을 써서 중복요소를 제거해준다.
                sq_len = len(set(sq))
        # sq의 길이가 9보다 작으면 중된 숫자가 있다는 뜻
        if sq_len < 9:
            # result를 0으로 변경
            result = 0
    # 정답 출력
    print(f'#{tc} {result}')
