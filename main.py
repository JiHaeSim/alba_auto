from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

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

# 인재정보 50개씩 보기
browser.find_element_by_class_name('selPerPage').click()
select = Select(browser.find_element_by_class_name('selPerPage'))
select.select_by_value('50')

# 맞춤 인재정보 스크랩
table = browser.find_element_by_class_name('tbl')
rows = table.find_elements_by_tag_name("tr")
# table 스크랩 테스트
# for tr in table.find_elements_by_tag_name("tr"):
#         td = tr.find_elements_by_tag_name("td")
#         s = "{} , {}\n".format(td[1].text , td[2].text)
#         #print (s)
#         fp.write(s)

# for index, value in enumerate(rows):
    # body=value.find_elements_by_tag_name("td")[0]
    # body = value.find_element_by_class_name('cTit')
    # print(body.text)
    # print(index.text,value.text)

time.sleep(1000)

