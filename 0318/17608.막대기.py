# N: 직원 수
N = int(input())
# 막대기 리스트
sticks = [int(input()) for _ in range(N)]
# 오른쪽에서부터 보기 때문에 최대 막대기 높이를 sticks[-1]로 설정
max_height = sticks[-1]
# 카운트는 맨 오른쪽 1개는 이미 세고 시작하기에 1로 설정
cnt = 1
# 오른쪽에서 부터 반복문 시작
for i in range(-1, -(N + 1), -1):
    # 만약 막대기 높이가 최대 높이보다 크다면 카운트 1증가하고 현재값을 최대높이로 설정한다.
    if sticks[i] > max_height:
        cnt += 1
        max_height = sticks[i]
# 정답 출력
print(cnt)