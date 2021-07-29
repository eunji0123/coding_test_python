# My solution
n, k = map(int,input().split())
ans = 0

while n != 1:
    if n % k == 0:
        n //= k
    else:
        n -= 1
    ans += 1

print(ans)

#############################
# Good 1
# 위의 방법은 n이 k로 나누어떨어지는 수가 될 때까지 반복해서 1씩만 뺌
# 하지만 n이 k의 배수가 되도록 한 번에 빼면 계산 시간을 훨씬 줄일 수 있음.

n, k = map(int,input().split())
ans = 0

while True:
    # n을 k의 배수 중 최대로 일단 만듦
    target = (n // k) * k
    if target != 0:
        ans += (n - target) + 1 # target이 될 때까지 빼고 k의 배수가 됐으니까 1번 나눠주는 것까지 연산
        n = target // k
    else: # target이 0이라는 건, 결국 n을 k로 나눌 수 없다는 얘기
        break

ans += n - 1 # 1이 될때까지 계속 빼주는 연산
print(ans)
