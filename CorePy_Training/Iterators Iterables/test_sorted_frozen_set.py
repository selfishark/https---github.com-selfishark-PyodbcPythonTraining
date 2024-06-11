import unittest

from sorted_frozen_set import SortedFrozenSet

# a test for grouping construction related test
# this will help test our SortedFrozenSet
# class TestConstruction(unittest.TestCase):

#     def test_construct_empty(self):
#         s = SortedFrozenSet([])   # initialized a new SortedFrozenSet with empty list

#     def test_construct_from_non_empty_list(self):
#         s = SortedFrozenSet([7, 5, 6, 9, 1])    # initialized a new SortedFrozenSet with some items

#     def test_constructor_from_an_iterator(self):
#         items = [7, 5, 6, 9, 1]
#         iterator = iter(items)  # iter will allow us to check our iterator doesn't throw exceptions
#         s = SortedFrozenSet(iterator)

#     def test_no_constructor_no_args(self):
#         s = SortedFrozenSet()   # test an empty constructor with no argument in the use of the class


# class TestContainerProtocol(unittest.TestCase):

#     # setUp is an optional method for test fixtures to a test case instance
#     # it help to create example test data, avoiding repetition for each test method
#     # the unittest runner will call setUp before every test method to isolate individual tests from each other
#     def setUp(self):
#         self.s = SortedFrozenSet([7, 5, 6, 9, 1])

#     ## Test positive and negative assertions from the list of items in the SortedFrozenSet
#     def test_positive_contained(self):
#         self.assertTrue(5 in self.s)

#     def test_negative_contained(self):
#         self.assertFalse(3 in self.s)

#     def test_positive_not_contained(self):
#         self.assertTrue(2 not in self.s)

#     def test_negative_not_contained(self):
#         self.assertFalse(9 not in self.s)


# class TestSizedProtocol(unittest.TestCase):

#     def test_empty_with_default(self):
#         s = SortedFrozenSet()
#         self.assertEqual(len(s), 0)     # Test a default empty SortedFrozenSet

#     def test_empty(self):
#         s = SortedFrozenSet([])
#         self.assertEqual(len(s), 0)     # Test an empty SortedFrozenSet

#     def test_one(self):
#         s = SortedFrozenSet([25])
#         self.assertEqual(len(s), 1)     # Test SortedFrozenSet has at least one item

#     def test_ten(self):
#         s = SortedFrozenSet(range(10))
#         self.assertEqual(len(s), 10)    # Test SortedFrozenSet has at least 10 items

#     def test_with_duplicates(self):
#         s = SortedFrozenSet([1, 1, 1])
#         self.assertEqual(len(s), 1)     # Test SortedFrozenSet has no duplicates


# # test the iterable protocol to see if the class SortedFrozenSet meets the iter property
# class TestIterableProtocol(unittest.TestCase):

#     def setUp(self):
#         self.s = SortedFrozenSet([9, 1, 1, 6, 2])   # the list is intentionally unsorted

#     def test_iter(self):
#         iterator = iter(self.s)                 # This test obtains the built-in iterator,
#         self.assertEqual(next(iterator), 1)     # to assert the property to see if each value is as expected,
#         self.assertEqual(next(iterator), 2)     # in sorted order with no duplicates.
#         self.assertEqual(next(iterator), 6)
#         self.assertEqual(next(iterator), 9)
#         self.assertRaises(
#             StopIteration,                      # this exception fashionably terminates the iteration
#             lambda: next(iterator)              # the next iterator is called with 'lambda' rather than the code calling it in the next assertion (best practice)
#         )

#     # test if the SortedFrozenSet can be used in a for-loop
#     # although if the test_iter (testing the iteration property) the for-loop will also work
#     def test_for_loop(self):
#         expected = [1, 2, 6, 9]
#         index = 0
#         for item in self.s:
#             self.assertEqual(item, expected[index])
#             index += 1

class TestSequenceProtocol(unittest.TestCase):

    def setUp(self):
        self.s = SortedFrozenSet([1, 3, 5, 6, 8, 9])

#     ## test the indexing of a sequence protocol
#     def test_index_zero(self):
#         self.assertEqual(self.s[0], 1)

#     def test_index_four(self):
#         self.assertEqual(self.s[4], 8)

#     def test_index_one_beyond_the_end(self):
#         with self.assertRaises(IndexError):     # with allows to hold the index
#             self.s[6]

#     def test_index_minus_one(self):
#         self.assertEqual(self.s[-1], 9)

#     def test_index_minus_five(self):
#         self.assertEqual(self.s[-6], 1)

#     def test_index_one_before_the_beginning(self):
#         with self.assertRaises(IndexError):
#             self.s[-6]

    ## test the slicing of a sequence protocol
    def test_slice_from_start(self):
        self.assertEqual(self.s[:3], SortedFrozenSet([1, 3, 5, 6]))

    def test_slice_to_end(self):
        self.assertEqual(self.s[3:], SortedFrozenSet([8, 9]))

    def test_slice_empty(self):
        self.assertEqual(self.s[10:], SortedFrozenSet())

    def test_slice_arbitrary(self):
        self.assertEqual(self.s[2:4], SortedFrozenSet([5, 6, 8]))

    def test_slice_step(self):
        self.assertEqual(self.s[0:5:2], SortedFrozenSet([[1, 5, 8]]))

    def test_slice_full(self):
        self.assertEqual(self.s[:], self.s)


    def test_reversed(self):
        s = SortedFrozenSet([1, 3, 5, 7])
        r = reversed(s)
        self.assertEqual(next(r), 7)
        self.assertEqual(next(r), 5)
        self.assertEqual(next(r), 3)
        self.assertEqual(next(r), 1)
        self.assertRaises(StopIteration, lambda: next(r))

    def test_index_positive(self):
        s = SortedFrozenSet([1, 5, 8, 9])
        self.assertEqual(s.index(8), 2)

    def test_index_negative(self):
        s = SortedFrozenSet([1, 5, 8, 9])
        with self.assertRaises(ValueError):
            s.index(15)

    def test_count_zero(self):
        s = SortedFrozenSet([1, 5, 7, 9])
        self.assertEqual(s.count(11), 0)

    def test_count_one(self):
        s = SortedFrozenSet([1, 5, 7, 9])
        self.assertEqual(s.count(7), 1)


class TestReprProtocol(unittest.TestCase):

    def test_repr_empty(self):
        s = SortedFrozenSet()
        self.assertEqual(repr(s), "SortedFrozenSet()")

    def test_repr_one(self):
        s = SortedFrozenSet([42, 40, 19])
        self.assertEqual(repr(s), "SortedFrozenSet([19, 40, 42])")


class TestEqualityProtocol(unittest.TestCase):

    def test_positive_equal(self):
        self.assertTrue(
            SortedFrozenSet([4, 5, 6]) == SortedFrozenSet([6, 5, 4])
        )

    def test_negative_equal(self):
        self.assertFalse(
            SortedFrozenSet([4, 5, 6]) == SortedFrozenSet([1, 2, 3])
        )

    def test_type_mismatch(self):
        self.assertFalse(
            SortedFrozenSet([4, 5, 6]) == [4, 5, 6]
        )

    def test_identical(self):
        s = SortedFrozenSet([10, 11, 12])
        self.assertTrue(s == s)


class TestInequalityProtocol(unittest.TestCase):

    def test_positive_unequal(self):
        self.assertTrue(SortedFrozenSet([4, 5, 6]) != SortedFrozenSet([1, 2, 3]))

    def test_negative_unequal(self):
        self.assertFalse(SortedFrozenSet([4, 5, 6]) != SortedFrozenSet([6, 5, 4]))

    def test_type_mismatch(self):
        self.assertTrue(SortedFrozenSet([1, 2, 3]) != [1, 2, 3])

    def test_identical(self):
        s = SortedFrozenSet([10, 11, 12])
        self.assertFalse(s != s)


class TestHashableProtocol(unittest.TestCase):

    def test_equal_sets_have_the_same_hash_code(self):
        self.assertEqual(
            hash(SortedFrozenSet([5, 2, 1, 4])),
            hash(SortedFrozenSet([5, 2, 1, 4])),
        )

if __name__ == "__main__":
    unittest.main()
