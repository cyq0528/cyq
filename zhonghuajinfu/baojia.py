# *-* coding: utf-8 *-*
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import random
import time
import datetime

def autoOffer():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://test.zhonghuajinfu.com/match/auth/index.html')
    userName=driver.find_element_by_id("username")
    userName.send_keys('huasuhui')
    password=driver.find_element_by_id("password")
    password.send_keys("huasuhui123")
    time.sleep(10)
    locator=(By.ID,"reload_data")
    WebDriverWait(driver, 5).until(EC.presence_of_element_located(locator))
    driver.get('http://www.egy.cn/match/offer/index?catalog_id=11')
    js='jQuery(".match-kanpan-1>a").trigger("click")';
    driver.execute_script(js)
    time.sleep(1)
    sell_buy=True
    while True:
        trade_price_num=random.randint(7800,7850)
        trade_price_num=trade_price_num//10*10
        trade_price = driver.find_element(By.ID,"trade_price")
        trade_price.clear()
        trade_price.send_keys(trade_price_num)
        trade_amount_num = random.randint(2, 10)
        trade_amount = driver.find_element(By.ID,"trade_amount")
        trade_amount.clear()
        trade_amount.send_keys(trade_amount_num)
        # trade_type = driver.find_element_by_id("trade_type")
        trade_type =driver.find_element(By.ID,"trade_type")
        trade_type_num = 1 if sell_buy else -1
        for i in trade_type.find_elements_by_tag_name("option"):
            if int(i.get_attribute("value"))==int(trade_type_num):
                i.click()
        dateArr=getDateinterval()
        js = 'document.getElementById("delivery_start").value="' + dateArr[0] + '";'
        driver.execute_script(js)
        js='document.getElementById("delivery_end").value="'+dateArr[1]+'";'
        driver.execute_script(js)
        addBtn=driver.find_element_by_id('addCompanyEventBtn')
        addBtn.click()
        time.sleep(random.randint(5,10))
        sell_buy=not sell_buy

def getDateinterval():
    dateArr=[]
    start = int(time.time())  # 生成开始时间戳
    end = datetime.datetime.now() + datetime.timedelta(days=30)
    end = int(end.timestamp())
    for i in range(2):
        t = random.randint(start, end)  # 在开始和结束时间戳中随机取出一个
        date_touple = time.localtime(t)  # 将时间戳生成时间元组
        date = time.strftime("%Y-%m-%d", date_touple)  # 将时间元组转成格式化字符串（1976-05-21）
        dateArr.append(date)
        start=t
    return dateArr
if __name__ == "__main__":
    autoOffer()

