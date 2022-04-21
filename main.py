from selenium import webdriver
import time
browser = webdriver.Chrome('chromedriver.exe')
browser.get("https://www.albamon.com/login/logout_trans.asp")

id = 'tjcldgkwk2'
pw = 'xmrxla1!'

# 로그인
browser.find_element_by_id('DB_Name_GI').click()
input_id = browser.find_element_by_id('M_ID').send_keys(id)
input_pw = browser.find_element_by_id('M_PWD_default').send_keys(pw)
browser.find_element_by_class_name('btnLogin').click()

# 로그인 후 팝업창 닫고 인재검색
browser.find_element_by_class_name('guideCloseBtn').click()
browser.find_element_by_class_name('nav4').click()

# 최근 본 인재 클릭 후 페이지 이동
# browser.find_element_by_class_name('n2').click()
# browser.switch_to.window(browser.window_handles[1])


time.sleep(1000)



# browser.find_element_by_xpath('//*[@id="power_link_body"]/ul/li[1]/div/a').get_attribute('href')