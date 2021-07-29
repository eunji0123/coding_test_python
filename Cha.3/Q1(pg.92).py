# My solution
n, m, k = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort(reverse = True)
answer = 0
p = k # k는 줄어들면 안되니까 p 변수를 따로 만들어서 k처럼 사용

for i in range(m): # 전체 m번 더함
    if p == 0: # p, 즉 k의 값이 0이면 두번째로 큰 수 더해줌
        answer += nums[1]
        p = k # p 값을 다시 k로 세팅
    else:
        answer += nums[0] # p, 즉 k의 값이 0이 아니면 제일 큰 수 더해줌
        p -= 1 # p 값을 하나 줄임

print(answer)

##################################
# Good 1
n, m, k = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort(reverse = True)

first = nums[0]
second = nums[1]

# 가장 큰 수를 몇 번 더해야 하는지 계산
first_count = (m // (k+1)) * k + (m % (k+1))

answer = first * first_count + second * (m - first_count)

print(answer)
