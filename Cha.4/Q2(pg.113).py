# My solution
n = int(input())
count = 0

end = n * 60 * 60 + 59 * 60 + 59 # 가능한 마지막 시간 계산

for i in range(end+1): # 0 ~ 마지막 시간
    hour = i // 3600
    if '3' in str(hour):
        count += 1
        continue

    minute = (i % 3600) // 60
    if '3' in str(minute):
        count += 1
        continue

    second = (i % 3600) % 60
    if '3' in str(second):
        count += 1

print(count)

########################################
# Good 1
# 중첩반복문 활용

n = int(input())
count = 0

for hour in range(n + 1):
    for minute in range(60):
        for sec in range(60):
            if '3' in str(hour) + str(minute) + str(sec):
                count += 1

print(count)
