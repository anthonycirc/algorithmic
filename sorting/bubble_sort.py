def bubble_sort_not_optimized(array: list[int]) -> list:
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


def bubble_sort_optimized(array: list[int]) -> list:
    """
    Bubble sort algorithm (optimized) not count the last item
    :param array: list of integers
    :return: list: sorted list
    """
    array_size: int = len(array)

    for i in range(array_size):
        # array_size - i - 1 for not count the last element
        for j in range(array_size - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


def bubble_sort_more_optimized(array: list[int]) -> list:
    """
    Bubble sort algorithm (optimized) add swapped variable
    :param array: list of integers
    :return:list: sorted list
    """
    array_size: int = len(array)
    swapped: bool = True

    while swapped:
        swapped = False
        for i in range(array_size - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True

        if not swapped:
            break
    return array


def bubble_sort_full_optimized(array: list[int]) -> list:
    """
    Bubble sort algorithm (Full optimized) add swapped var and num_iterations
    :param array: list of integers
    :return:list: sorted list
    """
    array_size: int = len(array)
    swapped: bool = True
    num_iterations: int = 0

    while swapped:
        swapped = False
        for i in range(array_size - num_iterations - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True

        num_iterations += 1
    return array


def bubble_sort_full_optimized_without_duplicates_values(array: list[int]) -> list:
    """
    Bubble sort algorithm (optimized) add swapped var and num_iterations and remove duplicates value
    :param array: list of integers
    :return:list: sorted list
    """
    array_size: int = len(array)
    swapped: bool = True
    num_iterations: int = 0

    while swapped:
        swapped = False
        for i in range(array_size - num_iterations - 1):
            # if value is duplicate in array remove
            if array[i] == array[i + 1]:
                array.pop(i + 1)
                array_size -= 1

            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True

        num_iterations += 1
    return array


def bubble_sort_full_optimized_without_duplicates_values_with_set(array: list[int]) -> list:
    """
    Bubble sort algorithm (optimized) add swapped var and num_iterations and remove duplicates value
    :param array: list of integers
    :return:list: sorted list
    """
    array_size: int = len(array)
    swapped: bool = True
    num_iterations: int = 0

    while swapped:
        swapped = False
        for i in range(array_size - num_iterations - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True

        num_iterations += 1
    return list(set(array))


if __name__ == '__main__':
    bubble_sort_not_optimized([1, 7, 2, 8, 6, 9, 3, 5, 4])
    bubble_sort_not_optimized([1, 7, 2, 3, 2, 4, 8, 6, 9, 3, 4, 5, 4])
    bubble_sort_optimized([1, 7, 2, 8, 6, 9, 3, 5, 4])
    bubble_sort_more_optimized([1, 7, 2, 8, 6, 9, 3, 5, 4])
    bubble_sort_full_optimized([1, 7, 2, 8, 6, 9, 3, 5, 4])

    # Test with duplicates values
    bubble_sort_full_optimized_without_duplicates_values([1, 7, 2, 3, 2, 4, 8, 6, 9, 3, 4, 5, 4])
    bubble_sort_full_optimized_without_duplicates_values_with_set([1, 7, 2, 3, 2, 4, 8, 6, 9, 3, 4, 5, 4])
