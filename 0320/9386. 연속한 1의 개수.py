# import sys
#
# sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    bin_num = input()
    max_cnt = 0

    cnt = 0
    for i in range(N):
        if bin_num[i] == '1':
            cnt += 1
        if bin_num[i] == '0' or i == N - 1:
            if max_cnt < cnt:
                max_cnt = cnt
                cnt = 0
    print(f'#{tc} {max_cnt}')
