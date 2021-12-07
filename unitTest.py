import unittest


def miMetodo(x):
    return (x + 1) / x


class TestMyModule(unittest.TestCase):
    def test1(self):
        self.assertLessEqual(miMetodo(7), 5)

    def test2(self):
        self.assertNotEqual(miMetodo(2), 3)

    def test3(self):
        self.assertLess(miMetodo(2), 2)


if __name__ == "__main__":
    unittest.main()
