from selenium import webdriver
import time,unittest,random
from selenium.webdriver.common.action_chains import ActionChains
class chating(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://test.zhonghuajinfu.com/match/auth/index.html')
        '''登录'''
        self.driver.find_element_by_xpath('//*[@id="username"]').send_keys('test01')
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys('111111')
        time.sleep(12)
        '''点击登录按钮'''
        self.driver.find_element_by_xpath('//*[@id="signup"]').click()
    def testChatting(self):
        time.sleep(3)
        '''点击私信聊天icon'''
        self.driver.find_element_by_xpath('//*[@id="vu_chitchat"]').click()
        '''点击分组名称'''
        self.driver.find_element_by_xpath('//*[@id="vu_accordion"]/li/div/span[1]').click()
        '''img:头像位置'''
        img=self.driver.find_element_by_xpath('//*[@id="vu_accordion"]/li/ul/li')
        time.sleep(1)
        '''双击头像'''
        ActionChains(self.driver).double_click(img).perform()
        '''点击对话框'''
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="vu_chat"]/div[3]/div[2]/textarea').click()
        '''输入文字'''
        for i in range(0, 100):
            Price=random.randint(6000,9000)
            '''textBox:文本框的位置'''
            textBox=self.driver.find_element_by_xpath('//*[@id="vu_chat"]/div[3]/div[2]/textarea')
            textBox.send_keys('出：meg 明天上午交割 国际 500吨 %d'%(Price)+' --新天\n')
            textBox.send_keys('接：meg 下周或下下周 国际 %d'%(Price)+'---博纳')
            '''点击发送按钮'''
            self.driver.find_element_by_xpath('//span[@class="vu_send"]').click()
        '''关闭对话框'''
        self.driver.find_element_by_xpath('//*[@id="tuo"]/div/p/span').click()
        self.groupOffer()
    '''进行报价和群发'''
    def groupOffer(self):
        '''在首页点击新增报价按钮'''
        self.driver.find_element_by_xpath('//*[@id="ajax_content"]/div[4]/div[6]/div[1]/div/div[3]/a').click()
        time.sleep(3)
        '''打开群发，关闭群发按钮'''
        button=self.driver.find_element_by_xpath('//*[@id="addQuickForm"]/div/div[1]/span')
        if button.text == "打开群发":
            button.click()
            time.sleep(1)
            self.groupContains()
        elif button.text=="关闭群发":
            time.sleep(1)
            self.groupContains()
    '''判断有无群发人员'''
    def groupContains(self):
        '''people：群发人数'''
        people=int(self.driver.find_element_by_xpath('//*[@id="addQuickForm"]/div/div[1]/div[2]/div/div/div[2]/p/span').text)
        if people >1:
            self.offer()
        else:
            openPeople=self.driver.find_element_by_xpath('//*[@id="addQuickForm"]/div/div[1]/div[2]/div/div/div[1]/ul/li')
            hasattr(openPeople,'class')
            openPeople.click()
            '''点击全选'''
            self.driver.find_element_by_xpath('//*[@id="addQuickForm"]/div/div[1]/div[2]/div/div/div[1]/ul/li/p').click()
            time.sleep(1)
            self.driver.find_element_by_xpath(
                '//*[@id="addQuickForm"]/div/div[1]/div[2]/div/div/div[1]/ul/li/p').click()
            time.sleep(1)
            self.offer()
    '''offer:进行报价方法'''
    def offer(self):
        '''offerTxtBox：报价文本框'''
        offerTxtBox=self.driver.find_element_by_xpath('//*[@id="quick_parse_txt"]')
        '''进入报价框'''
        offerTxtBox.click()
        '''输入报价的文本'''
        offerTxtBox.send_keys('出：meg 明天上午交割 国际 500吨 7030 --新天')
        '''点击报价识别按钮'''
        self.driver.find_element_by_xpath('//*[@id="quick_parse_create"]').click()
        time.sleep(0.5)
        '''点击提交报价按钮'''
        self.driver.find_element_by_xpath('//button[@id="quick_parse_submit_price"]').click()
if __name__=='__main__':
    unittest.main()



