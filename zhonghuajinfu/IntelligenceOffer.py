from selenium import webdriver
import time,random,unittest
class intelligenceOffer(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://test.zhonghuajinfu.com/match/auth/index.html')
        '''登录'''
        self.driver.find_element_by_xpath('//*[@id="username"]').send_keys('test01')
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys('111111')
        time.sleep(12)
        #         '''点击登录按钮'''
        self.driver.find_element_by_xpath('//*[@id="signup"]').click()
    @classmethod
    def tearDownClass(self):
        self.driver.close()
    def testIntelligenceOfferDef(self):
        '''在首页点击新增报价按钮'''
        time.sleep(3)
        self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        self.driver.find_element_by_xpath('//*[@id="ajax_content"]/div[4]/div[6]/div[1]/div/div[3]/a').click()
        '''offerTxtBox：报价文本框'''
        offerTxtBox = self.driver.find_element_by_xpath('//*[@id="quick_parse_txt"]')
        '''进入报价框'''
        offerTxtBox.click()
        for i in range(1,10):
            Price=random.randint(6000,9000)
            '''输入报价的文本'''
            offerTxtBox.send_keys('出：meg 明天上午交割 国际 500吨 %d'%(Price)+' --新天\n')
            offerTxtBox.send_keys('接：meg 下周或下下周 国际 %d'%(Price)+'---博纳')
            '''点击报价识别按钮'''
            time.sleep(0.5)
            self.driver.find_element_by_xpath('//*[@id="quick_parse_create"]').click()
            time.sleep(0.5)
            '''点击提交报价按钮'''
            self.driver.find_element_by_xpath('//button[@id="quick_parse_submit_price"]').click()
            # pngTime = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())
            # self.driver.get_screenshot_as_file('D:/自动化截图/' + pngTime +'.png')
if __name__=='__main__':
    unittest.main()






