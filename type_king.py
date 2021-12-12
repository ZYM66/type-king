from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
txtlist = []
print("欢迎使用金山打字王！".center(50,"*"))
n = int(input("每行间隔多少秒（一共五行）:"))
browser = webdriver.Chrome()
browser.get("https://dz.wubidz.cn/index.php")
key = 1
pagename = browser.find_element_by_id('contents')
txtnamelist = pagename.text.split()
for i in txtnamelist:
    print(str(key) + i)
    key = key + 1
chose = int(input("请输入要打篇目的序号:"))

s1 = Select(browser.find_element_by_id('contents'))  #选择options
s1.select_by_visible_text(txtnamelist[chose-1])


su = browser.find_element_by_name('submitss')
su.click()


count = 0


submit0 = browser.find_element_by_id('gdwz0')	#定位元素，以txt形式存入列表
txtlist.append(submit0.text)

submit1 = browser.find_element_by_id('gdwz1')
txtlist.append(submit1.text)

submit2 = browser.find_element_by_id('gdwz2')
txtlist.append(submit2.text)

submit3 = browser.find_element_by_id('gdwz3')
txtlist.append(submit3.text)

submit4 = browser.find_element_by_id('gdwz4')
txtlist.append(submit4.text)

for count in range(0,5):
    time.sleep(n)
    count_s = str(count)
    node = browser.find_element_by_id("srwz" + count_s)
    node.send_keys(txtlist[count])



