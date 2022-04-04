def bubble_sort(array: list[int]) -> list:
    """
    Bubble sort algorithm (not optimized)
    :param array: list of integers
    :return:list: sorted list
    """
    array_size: int = len(array) - 1

    for i in range(array_size):
        for j in range(array_size - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


if __name__ == '__main__':
    bubble_sort([1, 7, 2, 8, 6, 9, 3, 5, 4])
