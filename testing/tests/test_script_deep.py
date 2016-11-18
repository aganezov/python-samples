import unittest

import time

from testing.script import MyClass


class MyClassDeepTestCase(unittest.TestCase):
    def test_deep(self):
        # some deep testing stuff
        time.sleep(1)
        self.assertNotEqual(MyClass.bad, MyClass.good)


if __name__ == '__main__':
    unittest.main()
