from selenium import webdriver
from time import sleep

path = r'D:\10-Software\python\SeleniumDriver\chromedriver.exe'

w = webdriver.Chrome(executable_path=path)

# 打开百度浏览器
url = 'http://www.baidu.com/'
w.get(url)
sleep(3)

# 通过id找到百度的输入框
my_imput = w.find_element_by_id('kw')

# 在输入框里输入美女
my_imput.send_keys('美女')
sleep(3)

# 查找百度一下按钮
button = w.find_element_by_id('su')
# 点击搜索按钮
button.click()
sleep(3)

# 查找到单张图片
poto = w.find_elements_by_xpath('//*[@id="1"]/div[2]/a/img')
# 点击图片
poto.click()
sleep(3)

# 关闭浏览器
w.quit()

