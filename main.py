from selenium import webdriver
import time
browser = webdriver.Chrome('chromedriver.exe')
browser.get("https://www.albamon.com/login/logout_trans.asp")

id = 'tjcldgkwk2'
pw = 'xmrxla1!'

browser.find_element_by_id('DB_Name_GI').click()
input_id = browser.find_element_by_id('M_ID').send_keys(id)
input_pw = browser.find_element_by_id('M_PWD_default').send_keys(pw)
browser.find_element_by_class_name('btnLogin').click()

time.sleep(10)

# browser.find_element_by_xpath('//*[@id="power_link_body"]/ul/li[1]/div/a').get_attribute('href')