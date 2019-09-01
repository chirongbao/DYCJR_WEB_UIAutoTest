from DYCJR_WEB_UIAutoTest.DYCJR_WEB_UIAutoTest.test1.CaseKuangjia.addSub import AddSubTest
from DYCJR_WEB_UIAutoTest.DYCJR_WEB_UIAutoTest.test1.CaseKuangjia.StartEnd import setupTearDown
class test_sub(setupTearDown):
    def testOne(self):
        j = AddSubTest(2,1)
        self.assertEqual(j.sub(),1)

    def testTwo(self):
        j = AddSubTest(7,2)
        self.assertEqual(j.sub(),5)

