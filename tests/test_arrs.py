import unittest
from utils import arrs


class TestArrs(unittest.TestCase):

    # Тесты для get
    def test_get_with_negative_index(self):
        self.assertIsNone(arrs.get([1, 2, 3], -1))

    def test_get_with_index_equal_to_array_length(self):
        self.assertEqual(arrs.get([1, 2, 3], 3, "test"), "test")

    def test_get_with_valid_index(self):
        self.assertEqual(arrs.get([1, 2, 3], 0), 1)

    # Тесты для my_slice
    def test_my_slice_with_negative_indices(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4, 5], -4, -2), [2, 3])

    def test_my_slice_start_greater_than_end(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 3, 2), [])

    def test_my_slice_indices_out_of_bounds(self):
        self.assertEqual(arrs.my_slice([1, 2, 3], 1, 10), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], -10, 10), [1, 2, 3])

    def test_my_slice_with_none_indices(self):
        self.assertEqual(arrs.my_slice([1, 2, 3]), [1, 2, 3])

    def test_my_slice_with_empty_array(self):
        self.assertEqual(arrs.my_slice([]), [])
