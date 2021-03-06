# 삽입 정렬

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)): # 맨 첫 번째 원소는 이미 정렬되었다 생각하므로 두 번째 원소부터 시작
    for j in range(i, 0, -1):
        if array[j] < array[j-1]: # 더 전에 있는 원소가 크면 자리 바꿈
            array[j], array[j-1] = array[j-1], array[j]
        else: # 더 전에 있는 원소가 작으면 그대로 종료
            break
            
print(array)

#########################################################
'''
- 시간 복잡도: O(N^2)
- 어느 정도 정렬된 데이터가 들어오면 더욱 빠르게 동작하여 최선의 경우 O(N)의 시간 복잡도
'''
