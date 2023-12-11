import json
from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
import time
import pyotp

# 加载启动项，这里设置headless，表示不启动浏览器，只开一个监听接口获取返回值
option = webdriver.ChromeOptions()
option.add_argument('headless')
# 通过url访问浏览器
driver = webdriver.Chrome(options=option)
url = 'https://home.sandbox.cobo.com/#/login'
try:
    driver.get(url=url)
    driver.implicitly_wait(60)
    driver.find_element(By.XPATH, '''//*[@id="root"]/div/div[2]/div[2]/div/div''').click()
    print("点击登录。。。")
finally:
    driver.quit()


# 退出并关闭浏览器
