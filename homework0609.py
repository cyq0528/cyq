from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest,time
class zhengZhouUniversity(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        # 打开郑州大学官网
        print('开始')
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(6)
        self.driver.get('http://www.zzu.edu.cn/')
        self.driver.maximize_window()
    @classmethod
    def tearDownClass(self):
        pass
    #关闭郑州大学官网
        # self.driver.close()
    def testcase1(self):
        # moveToMouse，院系专业的xpath
        self.moveMose()
        #点击临床医学系
        self.driver.find_element_by_xpath('//*[@id="header_big_nav"]/li[3]/div/div/div[3]/dl/dt[3]/span').click()
        handles=self.driver.window_handles
        self.driver.switch_to.window(handles[1])
        self.assertEqual(self.driver.title,'临床医学系')
    def testcase2(self):
        #切换窗口
        handles=self.driver.window_handles
        self.driver.switch_to.window(handles[0])
        self.moveMose()
        #点击 院系专业-更多
        self.driver.find_element_by_xpath('//*[@id="header_big_nav"]/li[3]/div/div/div[3]/dl[2]/dt[7]/span[2]').click()
        newHandles=self.driver.window_handles
        self.driver.switch_to.window(newHandles[2])
        self.assertEqual(self.driver.title,'郑州大学.医学类院系')
    def moveMose(self):
        #移动鼠标到院系专业
        #切换到frame
        self.driver.switch_to.frame('zzu_top_6')
        #moveToMouse，院系专业的xpath
        moveToMouse=self.driver.find_element_by_xpath('//*[@id="header_big_nav"]/li[3]/a')
        webdriver.ActionChains(self.driver).move_to_element(moveToMouse).perform()
if __name__=="__main__":
    unittest.main()



