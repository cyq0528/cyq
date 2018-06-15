import unittest,time
from  hemework.HTMLTestRunner_PY3 import HTMLTestRunner
from hemework.homework0609 import zhengZhouUniversity
testcase=unittest.TestSuite()
testcase.addTest(unittest.TestLoader().loadTestsFromName('homework0609.zhengZhouUniversity'))
time=time.strftime('%Y-%m-%d-%H-%M',time.localtime())
dir='C:/Users/Administrator/Desktop/'+time+'repot.html'
file=open(dir,'wb')
runner=HTMLTestRunner(stream=file,title='陈以权自动化测试报告',description='selenium')
runner.run(testcase)
