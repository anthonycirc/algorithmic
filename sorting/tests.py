import unittest

from sorting.bubble_sort import bubble_sort, bubble_sort_optimized, bubble_sort_more_optimized, \
    bubble_sort_full_optimized


class TestBubbleSort(unittest.TestCase):
    def setUp(self) -> None:
        self.array = [1, 7, 2, 8, 6, 9, 3, 5, 4]
        self.array_repeat_values = [1, 7, 2, 3, 2, 4, 8, 6, 9, 3, 4, 5, 4]

    def test_array_is_sorted(self) -> None:
        self.assertEqual(bubble_sort([1, 7, 2, 8, 6, 9, 3, 5, 4]), [1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(bubble_sort_optimized([1, 7, 2, 8, 6, 9, 3, 5, 4]), [1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(bubble_sort_more_optimized([1, 7, 2, 8, 6, 9, 3, 5, 4]), [1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(bubble_sort_full_optimized([1, 7, 2, 8, 6, 9, 3, 5, 4]), [1, 2, 3, 4, 5, 6, 7, 8, 9])


if __name__ == '__main__':
    unittest.main()
