import unittest
from contrived_func import contrived_func


class TestContrivedFunc(unittest.TestCase):
    """
    The purpose of this program is to write a series of unit tests that
    attempt to meet 100% Branch and Condition Coverage for the contrived_func.

    Author: Christopher Tran
    Date: 04/25/2025
    """

    def test1(self):
        """
        a   b   c   d
        True True False False
        """
        contrived_func(13)

    def test2(self):
        """
        a   b   c   d
        True False False False
        """
        contrived_func(3)

    def test3(self):
        """
        a   b   c   d
        False False False False
        """
        contrived_func(15)

    def test4(self):
        """
        a   b   c   d
        True True False True
        """
        contrived_func(1)

    def test5(self):
        """
        a   b   c   d
        True False False True
        """
        contrived_func(0)

    def test6(self):
        """
        a   b   c   d
        False True False False
        """
        contrived_func(31)

    def test7(self):
        """
        a   b   c   d
        False True True False
        """
        contrived_func(998)

    def test8(self):
        """
        a   b   c   d
        False False True False
        """
        contrived_func(990)


if __name__ == '__main__':
    unittest.main()
