from sorting.bubble_sort import bubble_sort_not_optimized, bubble_sort_more_optimized, bubble_sort_full_optimized, \
    bubble_sort_full_optimized_without_duplicates_values, bubble_sort_full_optimized_without_duplicates_values_with_set

if __name__ == '__main__':
    print(bubble_sort_not_optimized([1, 7, 2, 8, 6, 9, 3, 5, 4]))
    print(bubble_sort_not_optimized([1, 7, 2, 3, 2, 4, 8, 6, 9, 3, 4, 5, 4]))
    print(bubble_sort_more_optimized([1, 7, 2, 8, 6, 9, 3, 5, 4]))
    print(bubble_sort_full_optimized([1, 7, 2, 8, 6, 9, 3, 5, 4]))
    print(bubble_sort_full_optimized_without_duplicates_values([1, 7, 2, 3, 2, 4, 8, 6, 9, 3, 4, 5, 4]))
    print(bubble_sort_full_optimized_without_duplicates_values_with_set([1, 7, 2, 3, 2, 4, 8, 6, 9, 3, 4, 5, 4]))
