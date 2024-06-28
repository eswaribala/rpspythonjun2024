import unittest

class TestA(unittest.TestCase):
    def runTest(self):
        self.assertEqual(1, 1)

class TestB(unittest.TestCase) :
    def runTest(self):
        self.assertEqual(2, 2)

class TestC(unittest.TestCase) :
    def runTest(self):
        self.assertEqual(3, 3)

suite = unittest.TestSuite()
suite.addTest(TestA())
suite.addTests([TestB(), TestC()])

unittest.TextTestRunner().run(suite)