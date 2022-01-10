# 퀵 정렬 - 방법 1

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end: # 원소가 1개만 있으면 정렬됐다고 보고 종료
        return

    pivot = start # 여기서 피벗은 첫 번째 원소
    left = start + 1
    right = end

    while left <= right:
        # 왼쪽에서부터는 피벗보다 큰 원소를 찾음
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 오른쪽에서부터는 피벗보다 작은 원소를 찾음
        while right > start and array[right] >= array[pivot]:
            right -= 1
        # 큰 원소와 작은 원소가 엇갈릴 경우, 작은 원소와 피벗을 교환
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        # 그게 아닐 경우, 큰 원소와 작은 원소 교환
        else:
            array[right], array[left] = array[left], array[right]

    # 정렬 완료 후에는 왼쪽과 오른쪽 리스트로 분할하여 다시 정렬 진행
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)
            

quick_sort(array, 0, len(array)-1)
print(array)

#########################################################
# 방법 2 - 심플 but 조금 비효율적

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    tail = array[1:]

    left_array = [x for x in tail if x <= pivot]
    right_array = [x for x in tail if x > pivot]

    return quick_sort(left_array) + [pivot] + quick_sort(right_array)
    
print(quick_sort(array))

#########################################################
'''
- 시간 복잡도: O(NlogN)
- 이 경우처럼 피벗을 가장 왼쪽 원소로 했는데 어느 정도 정렬된 데이터가 들어올 경우,
오히려 느리게 동작해서 최악의 경우 시간 복잡도 O(N^2)
- 이러한 점에서 삽입 정렬과 반대임
'''

