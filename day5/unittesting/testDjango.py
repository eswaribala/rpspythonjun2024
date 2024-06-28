import unittest
from djangoVersion import getDjangoVersion


class TestDjango(unittest.TestCase):

    def setUp(self):
        pass

    def test_version(self):
        self.assertTrue('1.6.7', getDjangoVersion())

if __name__ == '__main__':
    unittest.main()