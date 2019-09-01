from DYCJR_WEB_UIAutoTest.DYCJR_WEB_UIAutoTest.test1.CaseKuangjia.addSub import AddSubTest
from DYCJR_WEB_UIAutoTest.DYCJR_WEB_UIAutoTest.test1.CaseKuangjia.StartEnd import setupTearDown
class test_add(setupTearDown):
    def testOne(self):
        j = AddSubTest(1,2)
        self.assertEqual(j.add(),3)

    def testTwo(self):
        j = AddSubTest(3,4)
        self.assertEqual(j.add(),8)
