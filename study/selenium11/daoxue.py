# coding=utf-8
from selenium import webdriver
import time
#API文档  https://www.cnblogs.com/hanxiaobei/p/6108677.html
import json

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

req_url = "http://lftbjb.52fdw.com:9058/LFT-EditingSystem/login.htm?returlUrl=%2FLFT-EditingSystem%2Fpage%2Ftranslate%2FtranslateQuestionList.jsp"


browser = webdriver.Firefox(executable_path = 'D:\\Python27\\Scripts\\geckodriver.exe')
#browser = webdriver.Chrome()

#打开网页
browser.get(req_url)
browser.maximize_window()

time.sleep(2)

#登录
#browser.find_element_by_xpath('//*[@id="userid"]').send_keys(unicode("BCLR西安王伟").encode("utf-8"))
browser.find_element_by_xpath('//*[@id="userid"]').send_keys(json.loads(json.dumps("BCLR西安王伟")))

browser.find_element_by_xpath('//*[@id="userpass"]').click()
browser.find_element_by_xpath('//*[@id="userpass"]').send_keys("000000")

browser.find_element_by_xpath('//*[@id="login"]').click()
time.sleep(2)

#抽题
browser.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[1]/div[2]/ul/li/div').click()

time.sleep(1)
browser.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div/div[2]/div[1]/a/span').click()

browser.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[7]/div').click()

