# My solution
n = int(input())
plans = list(input().split())
x, y = 1, 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for plan in plans:
    if plan == 'L':
        nx = x + dx[0]
        ny = y + dy[0]
    elif plan == 'R':
        nx = x + dx[1]
        ny = y + dy[1]
    elif plan == 'U':
        nx = x + dx[2]
        ny = y + dy[2]
    else:
        nx = x + dx[3]
        ny = y + dy[3]

    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue
    else:
        x = nx
        y = ny

print(x, y)

###################################################
# Good 1
# 위의 풀이에서 반복되는 부분을 간단하게 묶는다

n = int(input())
plans = input().split() # 이 경우에 split은 list()로 감싸주지 않아도 리스트 형태로 저장
x, y = 1, 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
moves = ['L', 'R', 'U', 'D'] # 이동 유형도 똑같이 리스트로 저장

for plan in plans:
    for i in range(len(moves)): # 중첩반복문을 이용하여 이렇게 짧게 줄일 수 있음
        if plan == moves[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue
    
    x, y = nx, ny

print(x, y)
