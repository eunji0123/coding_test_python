# My solution

n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))


for i in range(k):
    a_min = min(a)
    b_max = max(b)

    if a_min < b_max:
        a.remove(a_min)
        b.remove(b_max)
        a.append(b_max)
        b.append(a_min)

    else:
        break

print(sum(a))

# remove()는 O(N)의 시간이 소요되므로 남발하면 시간 초과될 수 있음. 지양하기. (insert도 마찬가지)

######################################################

# 답지

'''
# 한 번 정렬을 먼저 해주면 전체 연산 횟수는 down
a.sort()
b.sort(reverse = True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i] # 서로 다른 리스트의 원소도 swap 가능
    else:
        break

print(sum(a))
'''    
