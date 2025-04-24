import unittest
from contrived_func import contrived_func


class TestContrivedFunc(unittest.TestCase):

    def test1(self):
        contrived_func(0)

    def test2(self):
        contrived_func(100)

    def test3(self):
        contrived_func(1)

    def test4(self):
        contrived_func(15)


if __name__ == '__main__':
    unittest.main()
