
import unittest
import time
from HTMLTestRunner import HTMLTestRunner

test_dir = './'
discovery = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')
#
# runner = unittest.TextTestRunner()
# runner.run(discovery)

if __name__ == '__main__':
    report_dir = './test_report'                    #存放报告的文件夹
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    report_name = report_dir+'/'+now+'result.html'  #报告文件的完整路径

    with open(report_name,'wb') as file:
        runner = HTMLTestRunner(stream=file,title='Test Report',description='Test Case Result ')
        runner.run(discovery)
    file.close()