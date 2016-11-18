import unittest

from testing.script import MyClass, MySecondClass


class MyClassCase(unittest.TestCase):
    def test_goodness(self):
        self.assertTrue(MyClass.good)

    def test_badness(self):
        self.assertFalse(MyClass.bad)


class MySecondClassCase(unittest.TestCase):
    def test_goodness(self):
        self.assertFalse(MySecondClass.good)

    def test_badness(self):
        self.assertTrue(MySecondClass.bad)


if __name__ == '__main__':
    unittest.main()
