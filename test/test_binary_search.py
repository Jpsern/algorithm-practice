import unittest
from src.tutorial import Tutorial


class TestBinarySearch(unittest.TestCase):
    def test_binary_search_found_middle(self):
        self.assertEqual(
            Tutorial.binary_search([1, 3, 5, 7, 9], 5),
            2,
            '中央の要素が見つかる'
        )

    def test_binary_search_found_first(self):
        self.assertEqual(
            Tutorial.binary_search([1, 3, 5, 7, 9], 1),
            0,
            '先頭の要素が見つかる'
        )

    def test_binary_search_found_last(self):
        self.assertEqual(
            Tutorial.binary_search([1, 3, 5, 7, 9], 9),
            4,
            '末尾の要素が見つかる'
        )

    def test_binary_search_not_found(self):
        self.assertEqual(
            Tutorial.binary_search([1, 3, 5, 7, 9], 4),
            -1,
            '存在しない要素は-1を返す'
        )

    def test_binary_search_duplicate_values(self):
        self.assertEqual(
            Tutorial.binary_search([1, 2, 2, 2, 3], 2),
            1,
            '重複要素は左端のindexを返す'
        )

    def test_binary_search_empty_array(self):
        self.assertEqual(
            Tutorial.binary_search([], 1),
            -1,
            '空配列では-1を返す'
        )
