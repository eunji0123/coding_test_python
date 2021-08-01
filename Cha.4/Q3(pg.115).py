# My solution
s = input()

x = ord(s[0]) - 96 # chr <-> ord
y = int(s[1])

dx = [-1, 1, 2, 2, -1, 1, -2, -2]
dy = [-2, -2, -1, 1, 2, 2, -1, 1]
count = 0

for i in range(len(dx)):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0 < nx < 9 and 0 < ny < 9:
        count += 1

print(count)

###########################################
# Good 1
# dx, dy 리스트를 따로 두지 않고 이렇게 steps로 한꺼번에 저장할 수도 있음
s = input()

x = ord(s[0]) - ord('a') + 1 # To be more general
y = int(s[1])

steps = [(-1, -2), (1, -2), (2, -1), (2, 1), (-1, 2), (1, 2), (-2, -1), (-2, 1)]
count = 0

for step in steps:
    nx = x + step[0]
    ny = y + step[1]

    if 0 < nx < 9 and 0 < ny < 9:
        count += 1

print(count)

# 만약, '1a'와 같이 잘못 들어온 입력을 예외처리 해야 한다면
# ord()를 활용해 범위를 확인해볼 수 있음
