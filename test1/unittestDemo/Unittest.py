import unittest
from DYCJR_WEB_UIAutoTest.DYCJR_WEB_UIAutoTest.test1.unittestDemo.testAdd import AddTest
from DYCJR_WEB_UIAutoTest.DYCJR_WEB_UIAutoTest.test1.unittestDemo.testJian import Sub


class TestDemo(unittest.TestCase):
    def setUp(self):
        print('starting,,,,,,')

    def test_demo1(self):
        aa = AddTest(10,11)
        self.assertEqual(aa.add(),21)

    def tearDown(self):
        print('end,,,,,,')

class TestSub(unittest.TestCase):
    def setUp(self):
        print('start,,,,')

    def TestSubTest(self):
        bb = Sub(9,8)
        self.assertEqual(bb.testsub(),1)

    def tearDown(self):
        print('stop,,,,,,')

if __name__ == '__main__':
    suit = unittest.TestSuite()           #多个测试用例集合在一起就是testSuite
    suit.addTest(TestDemo('test_demo1'))
    suit.addTest(TestSub('TestSubTest'))
    runner = unittest.TextTestRunner()    #TextTestRunner()是用来执行测试用例的
    runner.run(suit)                      #run()会执行TestSuite中的用例