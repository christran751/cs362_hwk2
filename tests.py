import unittest
from contrived_func import contrived_func


class TestContrivedFunc(unittest.TestCase):
    """
    This test attempt to achieve 100% Branch and Condition Coverage
    for the contrived_func.

    Author: Christopher Tran
    Date: 04/24/2025
    """

    def test1(self):
        """
        True True False False
        """
        contrived_func(13)

    def test2(self):
        """
        True False False False
        """
        contrived_func(3)

    def test3(self):
        """
        False False False False
        """
        contrived_func(15)

    def test4(self):
        """
        True True False True
        """
        contrived_func(1)

    def test5(self):
        """
        True False False True
        """
        contrived_func(0)

    def test6(self):
        """
        False True False False
        """
        contrived_func(31)

    def test7(self):
        """
        False True True False
        """
        contrived_func(998)

    def test8(self):
        """
        False False True False
        """
        contrived_func(990)


if __name__ == '__main__':
    unittest.main()
