# 테스트 케이스 갯수
T = int(input())
# T만큼 반복
for tc in range(1, T + 1):
    # N: 학생의 수, K: 확인하고 싶은 학생의 순서
    N, K = map(int, input().split())
    # score : 학생들의 점수를 입력받을 변수
    score = [list(map(int, input().split())) for _ in range(N)]
    # 토탈 점수담을 변수
    total = []
    # 점수 비율 곱해줄 변수
    score_ratio = [0.35, 0.45, 0.2]
    # 점수 등급
    score_level = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    # 점수를 계산하고 total에 담는다.
    for i in range(N):
        # 각 학생의 점수를 임시로 담을 변수
        temp = 0
        for j in range(3):
            # 점수가 3개이므로 3번 반복 돌며 temp에 비율을 곱해준 만큼 더해준다.
            temp += score[i][j] * score_ratio[j]
        # 계산하여 나온 점수를 토탈에 추가해준다.
        total.append(temp)
    # K의 토탈
    K_total = total[K - 1]
    # K의 등급 담을 변수
    K_score_level = ''
    # K의 등수
    K_rank = 0
    # 중복 가능한 등급 인원 수
    same_score_level_range = N / 10
    # 점수 높은순으로 정렬
    total.sort(reverse=True)
    # N만큼 반복
    for i in range(N):
        # K토탈 점수랑 정렬한 토탈의 i번 째 가 같을 때 K의 등수를 지정
        if K_total == total[i]:
            K_rank = i
        # 아니면 continue로 건너 뛴다.
        else:
            continue
        # 등급의 갯수 만큼 10번 반복
        for j in range(10):
            # j * same_score_level_range 보다 랭크가 크고 (j + 1) * same_score_level_range 보다 작다면
            # K의 등급은 score_level[j]이다.
            if j * same_score_level_range <= K_rank < (j + 1) * same_score_level_range:
                K_score_level = score_level[j]
    # 결과 출력
    print(f'#{tc} {K_score_level}')