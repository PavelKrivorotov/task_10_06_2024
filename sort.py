
def merge_sort(array: list) -> None:
    def _merge_sort(array: list, start: int, end: int) -> None:
        if end - start > 0:
            middle = (start + end) // 2
            _merge_sort(array, start, middle)
            _merge_sort(array, middle + 1, end)
            _merge(array, start, middle, end)

    _merge_sort(array, 0, len(array) - 1)

def _merge(array: list, start: int, middle: int, end: int) -> None:
    tmp_arr = []
    ind_1 = start
    ind_2 = middle + 1

    while (ind_1 <= middle and ind_2 <= end):
        if array[ind_1] > array[ind_2]:
            tmp_arr.append(array[ind_2])
            ind_2 += 1
        else:
            tmp_arr.append(array[ind_1])
            ind_1 += 1

    while ind_1 <= middle:
        tmp_arr.append(array[ind_1])
        ind_1 += 1

    while ind_2 <= end:
        tmp_arr.append(array[ind_2])
        ind_2 += 1

    array[start:end + 1] = tmp_arr

