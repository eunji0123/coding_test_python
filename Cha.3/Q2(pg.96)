# My solution
n, m = map(int,input().split())
ans = 0 # 최댓값을 찾아야 하니까 처음 시작은 0으로
        # 만약, 최솟값을 찾는 것이라면 처음 시작은 가능한 최댓값보다 1 큰 수 정도로 설정하면 됨.

for i in range(n): # 각 행마다 반복
    nums = list(map(int,input().split()))
    num = min(nums)
    ans = max(ans, num)

print(ans)
