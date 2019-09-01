import unittest

class testOne(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('class start ,,,,')

    @classmethod
    def tearDownClass(cls):
        print('class stop ,,,,')

    def testa(self):
        print('1')

    def testb(self):
        print('2')


class testTwo(unittest.TestCase):

    def testc(self):
        print('3')

    def testd(self):
        print('4')

if __name__ == '__main__':
    unittest.main()