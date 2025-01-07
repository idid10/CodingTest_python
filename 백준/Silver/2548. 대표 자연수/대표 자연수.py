# 입력 받기
import sys
input = sys.stdin.read

data = input().split()
N = int(data[0])  # 숫자의 개수
numbers = list(map(int, data[1:]))

# 수열 정렬
numbers.sort()

# 중앙값 찾기
# N이 짝수일 경우, 두 중앙값 중 작은 값 사용 (정렬 기준으로 자동으로 작은 값 선택)
median = numbers[(N - 1) // 2]

# 결과 출력
print(median)
