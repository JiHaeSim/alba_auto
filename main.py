from lib2to3.pgen2 import driver
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import UnexpectedAlertPresentException


browser = webdriver.Chrome('chromedriver.exe')
browser.get("https://www.albamon.com/login/logout_trans.asp")

id = 'tjcldgkwk2'
pw = 'xmrxla1!'

# 로그인
browser.find_element_by_id('DB_Name_GI').click()
input_id = browser.find_element_by_id('M_ID').send_keys(id)
input_pw = browser.find_element_by_id('M_PWD_default').send_keys(pw)
browser.find_element_by_class_name('btnLogin').click()
time.sleep(2)

# 로그인 후 팝업창 닫고 인재검색
browser.find_element_by_class_name('guideCloseBtn').click()
browser.find_element_by_class_name('nav4').click()

# 최근 본 인재 클릭 후 페이지 이동
# browser.find_element_by_class_name('n2').click()
# browser.switch_to.window(browser.window_handles[1])

# 인재정보 50개씩 보기
'''
browser.find_element_by_class_name('selPerPage').click()
select = Select(browser.find_element_by_class_name('selPerPage'))
select.select_by_value('50')
'''

# 맞춤 인재정보 스크랩
tbody = browser.find_element_by_tag_name('tbody')
tr = tbody.find_elements_by_tag_name('tr')
cTit = tbody.find_element_by_class_name('cInfo').find_element_by_class_name('cTit')


# 열람 전 인재 크롤링
name = tbody.find_element_by_class_name('cName_1')
print(name.get_attribute('innerText'))

hrefList = []
for r in tr:
    cTit = r.find_element_by_class_name('cTit')
    if "O" in r.find_element_by_class_name('cName_1').get_attribute('innerText'):
        print(r.find_element_by_class_name('cName_1').get_attribute('innerText'))
        hrefList.append(cTit.find_elements_by_tag_name('a')[0].get_attribute('href'))
    else:
        print("열람 됨")
        
print(hrefList)

# 열람 전 조건 체크(아직 미완)
for href in hrefList:
    browser.get(href)
    if browser.current_url=="https://www.albamon.com/ResumeSearch":
        continue
    point = browser.find_element_by_class_name('point')
    print(point)
    if '재학' in point.get_attribute('innerText'):
        if '휴학' in point.get_attribute('innerText'):
            print("우리와 함께 하실 수 없습니다.")
    else:
        print("반가워...!!")
        
time.sleep(1000)

