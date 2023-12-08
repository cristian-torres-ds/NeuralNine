import unittest
import my_functions

# For running in the terminal:
# python -m unittest my_tests.py

class TestMultiplyImperfect(unittest.TestCase):
    # tests allways have to start with the key word test
    def test_with_two_positives(self):
        self.assertEqual(my_functions.multiply_with_loop_imperfect(10, 5), 10 * 5)
        self.assertEqual(my_functions.multiply_with_loop_imperfect(5165431, 5168743), 5165431 * 5168743)
        self.assertEqual(my_functions.multiply_with_loop_imperfect(1, 2), 2)

    def test_with_one_zero(self):
        self.assertEqual(my_functions.multiply_with_loop_imperfect(137, 0), 0)
        self.assertEqual(my_functions.multiply_with_loop_imperfect(0, 137), 0)

    def test_with_two_zeroes(self):
        self.assertEqual(my_functions.multiply_with_loop_imperfect(0, 0), 0)

    def test_with_one_negative(self):
        self.assertEqual(my_functions.multiply_with_loop_imperfect(-10, 5), (-10) * 5)
        self.assertEqual(my_functions.multiply_with_loop_imperfect(10, -5), 10 * (-5))

    def test_with_two_negatives(self):
        self.assertEqual(my_functions.multiply_with_loop_imperfect(-10, -5), 50)



class TestMultiplyImproved(unittest.TestCase):
    # tests allways have to start with the key word test
    def test_with_two_positives(self):
        self.assertEqual(my_functions.multiply_with_loop_improved(10, 5), 10 * 5)
        self.assertEqual(my_functions.multiply_with_loop_improved(5165431, 5168743), 5165431 * 5168743)
        self.assertEqual(my_functions.multiply_with_loop_improved(1, 2), 2)

    def test_with_one_zero(self):
        self.assertEqual(my_functions.multiply_with_loop_improved(137, 0), 0)
        self.assertEqual(my_functions.multiply_with_loop_improved(0, 137), 0)

    def test_with_two_zeroes(self):
        self.assertEqual(my_functions.multiply_with_loop_improved(0, 0), 0)

    def test_with_one_negative(self):
        self.assertEqual(my_functions.multiply_with_loop_improved(-10, 5), (-10) * 5)
        self.assertEqual(my_functions.multiply_with_loop_improved(10, -5), 10 * (-5))

    def test_with_two_negatives(self):
        self.assertEqual(my_functions.multiply_with_loop_improved(-10, -5), 50)


class TestIntegerLength(unittest.TestCase):
    # tests allways have to start with the key word test
    def test_with_positive_integer(self):
        self.assertEqual(my_functions.length_of_integer(123456), 6)
        self.assertEqual(my_functions.length_of_integer(1), 1)
        self.assertEqual(my_functions.length_of_integer(10), 2)

    # the length must include the negative symbol
    def test_with_negative_integer(self):
        self.assertEqual(my_functions.length_of_integer(-123), 4)
        self.assertEqual(my_functions.length_of_integer(-1), 2)
        self.assertEqual(my_functions.length_of_integer(-123456), 7)

    def test_with_zero(self):
        self.assertEqual(my_functions.length_of_integer(0), 1)

    def test_with_invalid_type(self):
        self.assertRaises(TypeError, my_functions.length_of_integer, "12345")
        self.assertRaises(TypeError, my_functions.length_of_integer, "Hello")
        self.assertRaises(TypeError, my_functions.length_of_integer, True)
        self.assertRaises(TypeError, my_functions.length_of_integer, 123.123)
        self.assertRaises(TypeError, my_functions.length_of_integer, [1, 2, 3])


class TestIntegerLengthImproved(unittest.TestCase):
    # tests allways have to start with the key word test
    def test_with_positive_integer(self):
        self.assertEqual(my_functions.length_of_integer_improved(123456), 6)
        self.assertEqual(my_functions.length_of_integer_improved(1), 1)
        self.assertEqual(my_functions.length_of_integer_improved(10), 2)

    # the length must include the negative symbol
    def test_with_negative_integer(self):
        self.assertEqual(my_functions.length_of_integer_improved(-123), 4)
        self.assertEqual(my_functions.length_of_integer_improved(-1), 2)
        self.assertEqual(my_functions.length_of_integer_improved(-123456), 7)

    def test_with_zero(self):
        self.assertEqual(my_functions.length_of_integer_improved(0), 1)

    def test_with_invalid_type(self):
        self.assertRaises(TypeError, my_functions.length_of_integer_improved, "12345")
        self.assertRaises(TypeError, my_functions.length_of_integer_improved, "Hello")
        self.assertRaises(TypeError, my_functions.length_of_integer_improved, True)
        self.assertRaises(TypeError, my_functions.length_of_integer_improved, 123.123)
        self.assertRaises(TypeError, my_functions.length_of_integer_improved, [1, 2, 3])