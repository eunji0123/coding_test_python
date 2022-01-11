# 계수 정렬

array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1
    # 여기까지가 O(N)

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end = ' ')
    # 확인하는 작업이 O(K)
    # K = 데이터 중 최댓값의 크기
    
######################################
'''
- 시간 복잡도: O(N+K)
- 공간 복잡도: O(N+K)
- 최솟값과 최댓값의 차이가 1,000,000 보다 작을 때 쓸 수 있음
- 중복된 데이터가 많을수록 유리
- 데이터가 0과 999,999 이렇게 2개만 있는 경우 등에는 매우 비효율적
- 따라서 데이터의 특성을 파악하기 어렵다면 일반적인 경우에 평균적으로 빠르게 동작하는 퀵 정렬을 이용하는 것이 유리
'''