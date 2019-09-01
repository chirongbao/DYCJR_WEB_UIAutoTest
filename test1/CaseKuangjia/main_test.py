import unittest
test_dir = './'
discovery = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')

runner = unittest.TextTestRunner()
runner.run(discovery)

