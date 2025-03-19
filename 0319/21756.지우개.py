# 정수 N은 총 숫자 갯수
N = int(input())
# 숫자 리스트
arr = [i for i in range(1, N + 1)]
# arr의 길이가 1이 아니면 무한 반복
while len(arr) != 1:
    # arr의 홀수번을 삭제하니까 arr의 짝수번만 1개남을때까지 담아준다
    # 여기서는 인덱스 번호가 0부터이므로 인덱스 번호가 1부터 N까지 2씩 증가하면 짝수번 인덱스만 계속해서 담는다.
    arr = arr[1:N:2]
print(arr[0])