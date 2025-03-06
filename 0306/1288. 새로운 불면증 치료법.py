# import sys
# sys.stdin = open('input.txt', 'r')
# 테스크 케이스 갯수
T = int(input())
# T만큼 반복
for tc in range(1, T + 1):
    # 처음 시작할 양의 숫자
    N = int(input())
    '''
    취향이 독특한 호석이는 양을 셀 때 N의 배수 번호인 양을 센다.
    첫번째는 N번양, 두번째는 2N번 양,..., k번째는 kN번 양을 센다.
    이전에 셌던 번호들의 각 자리수에서 0 ~ 9 까지 모든 숫자를 보는 것은
    최소 몇 번째 양을 센 시점인가?
    
    접근법
    양을 N의 배수만큼 셀때마다 각 자리수 번호를 새로운 리스트에 넣어준다. 이미 센 번호는
    넣지 않는다.
    번호를 담은 리스트의 길이가 10이 되면 그때의 k값을 출력한다.
    '''
    # 이미 센 숫자를 담아줄 리스트
    counted_num = []
    # 정답을 담아줄 변수
    answer = 0
    # 1번째가 시작이므로 i = 1
    i = 1
    # counted_num이 10보다 작을때만 반복문
    while len(counted_num) < 10:
        # Ni: N의 i배
        Ni = i * N
        # Ni를 문자열로 바꿔준다
        str_Ni = str(Ni)
        # 문자열이 된 Ni만큼 반복문
        for j in range(len(str_Ni)):
            # str_Ni의 j가 counted_num에 있다면 건너뛴다.
            if str_Ni[j] in counted_num:
                continue
            # 없다면 counted_num에 추가해준다.
            else:
                counted_num.append(str_Ni[j])
        # counted_num이 10이 될때가 정답을 출력할 수 있다.
        if len(counted_num) == 10:
            # 정답은 현재 세고 있는 양의 번호이므로 Ni이다.
            answer = Ni
        # 위 조건을 모두 수행하고 마지막에 i가 증가한다.
        i += 1
    # 정답 출력
    print(f'#{tc} {answer}')
