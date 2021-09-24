# Selection sort (선택 정렬)

array = [4, 0, 8, 2, 6, 1, 3, 9, 7, 5]

for i in range(len(array)):
    min_index = i
    # 첫 번째 원소는 뒤의 9개 원소와 크기 비교
    # 두 번째 원소는 뒤의 8개 원소와 크기 비교
    # ...
    # 아홉 번째 원소는 뒤의 1개 원소와 크기 비교
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] # swap

print(array)
