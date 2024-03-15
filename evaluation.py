from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random
from selenium.webdriver.common.action_chains import ActionChains

usrname = '2023224020193'
password = 'cf11012011980@LTF'

# 初始化浏览器为chrome
service = Service('D:/Workspace/EvaluationofTeaching/chromedriver.exe')
driver = webdriver.Chrome(service=service)
actions = ActionChains(driver)

driver.maximize_window()   
driver.get(r'https://ehall.scu.edu.cn/gsapp/sys/wspjapp/*default/index.do?THEME=cherry&amp;EMAP_LANG=zh#/wspj')
time.sleep(2)

# 登录页
usrname_input = driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div/div[2]/div/div[1]/div[2]/div[2]/div/form/div[1]/div/div/div[2]/div/input')
usrname_input.send_keys(usrname)

if password:
    password_input = driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div/div[2]/div/div[1]/div[2]/div[2]/div/form/div[2]/div/div/div[2]/div/input')
    password_input.send_keys(password)

# 等待输入验证码
time.sleep(7)

login = driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div/div[2]/div/div[1]/div[2]/div[2]/div/form/div[4]/div/button')
login.click()

# 等待跳转
time.sleep(3)
guide_close = driver.find_element(by=By.XPATH, value='//*[@id="guideShut"]')
guide_close.click()
time.sleep(3)

node_num = 0

while True:
    # 找到表单父节点
    form_parentnode = driver.find_element(by=By.XPATH, value='//*[@id="wspjConstainer"]/div/div[2]/div/div/div')
    formnodes = form_parentnode.find_elements(by=By.XPATH, value='.//*[contains(@class, "bh-card bh-card-lv1 bh-pull-left bh-m-8")]')
    # print(len(formnodes))
    node=formnodes[0]

    # 如果未评教
    condition = node.find_element(by=By.XPATH, value='./div/div[1]')
    if condition.text=='未评教':
        node.click()
        time.sleep(3)
        if node_num == 0:
            guide_shut = driver.find_element(by=By.XPATH, value='//*[@id="guideShut"]')
            guide_shut.click()

        # ============================== 表单内容 ================================
        choice_1 = driver.find_element(by=By.XPATH, value='//*[@id="nr_f9914f972dcf4bd4b847fb49f38a8757"]/div/label[{}]/span'.format(random.choice([1,2])))
        choice_1.click()
        choice_2 = driver.find_element(by=By.XPATH, value='//*[@id="nr_7ee76034a06a479a99f06bc44b6fff4d"]/div/label[{}]/span'.format(random.choice([1,2])))
        choice_2.click()
        choice_3 = driver.find_element(by=By.XPATH, value='//*[@id="nr_17eb2686bd1f493c8f955945d991569d"]/div/label[{}]/span'.format(random.choice([1,2])))
        choice_3.click()
        choice_4 = driver.find_element(by=By.XPATH, value='//*[@id="nr_7a708b11005342a682763992793cc551"]/div/label[{}]/span'.format(random.choice([1,2])))
        choice_4.click()
        choice_5 = driver.find_element(by=By.XPATH, value='//*[@id="nr_9e625f4708674c3e81b74570a87f5877"]/div/label[{}]/span'.format(random.choice([1,2])))
        choice_5.click()
        choice_6 = driver.find_element(by=By.XPATH, value='//*[@id="nr_b9eb8d256e794def85b1690bc62cec6d"]/div/label[{}]/span'.format(random.choice([1,2])))
        choice_6.click()
        choice_7 = driver.find_element(by=By.XPATH, value='//*[@id="nr_221a4484e8ad474d9f98f25bbeef5201"]/div/label[{}]/span'.format(random.choice([1,2])))
        textarea = driver.find_element(by=By.XPATH, value='//*[@id="wb_3125e98a6fb14eda9a0f32fd9bdfa383"]')
        actions.move_to_element(textarea).perform()
        time.sleep(1)
        choice_7.click()
    

        textarea.send_keys('老师讲的很好！')
        textarea.send_keys(Keys.ENTER)
        time.sleep(1)

        submit = driver.find_element(by=By.XPATH, value='//*[@id="pjfooter"]/a[2]')
        actions.move_to_element(submit).click().perform()
        time.sleep(1)
        tan = driver.find_element(by=By.CLASS_NAME, value="bh-bhdialog-container")

        confirm = driver.find_element(by=By.XPATH, value='//*[@id="{}"]/div[1]/div[1]/div[2]/div[2]/a[1]'.format(tan.get_attribute("id")))
        confirm.click()
        time.sleep(3)
        node_num += 1
    else:
        break
            

# 关闭浏览器
driver.close()