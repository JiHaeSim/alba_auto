from lib2to3.pgen2 import driver
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import NoSuchElementException
import random

# (이력서 열람 오류를 위해 추가한 부분)
'''
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options)
'''

browser = webdriver.Chrome('chromedriver.exe')
browser.get("https://www.albamon.com/login/logout_trans.asp")
# browser.set_window_size(1920,1280)

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
browser.find_element_by_class_name('selPerPage').click()
select = Select(browser.find_element_by_class_name('selPerPage'))
select.select_by_value('50')

# 맞춤 인재정보 스크랩
tbody = browser.find_element_by_tag_name('tbody')
tr = tbody.find_elements_by_tag_name('tr')
cTit = tbody.find_element_by_class_name('cInfo').find_element_by_class_name('cTit')


# 열람 전 인재 링크 크롤링
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
index = 1
for href in hrefList:
    time.sleep(random.randrange(5))
    script = f"window.open('{href}')"
    browser.execute_script(script)
    browser.switch_to.window(browser.window_handles[index]) # 현재 페이지로 활성화 해줘야했음 ㅠㅠ
    
    try:
        if browser.current_url=="https://www.albamon.com/ResumeSearch":
            browser.quit()
            continue
    except UnexpectedAlertPresentException as e:
        print(e.__dict__['msg'])
    
    time.sleep(3)
    
    point = browser.find_element_by_class_name('point')

    print(browser.find_element_by_class_name('name').get_attribute('innerText'))
    print(point.get_attribute('innerText'))
    if '재학' in point.get_attribute('innerText'):
        print("우리와 함께 하실 수 없습니다.")
    elif '휴학' in point.get_attribute('innerText'):
        print("우리와 함께 하실 수 없습니다.")
    else:
        try:
            suggestBtn = browser.find_element_by_class_name('devBtnSuggestAlba')
            if suggestBtn:
                print('알바제의 따위는 하지 않는다.')
                index+=1
                continue
        except NoSuchElementException as e:
            print(e.__dict__['msg'])
        if "O" not in browser.find_element_by_class_name('name').get_attribute('innerText'):
            print("이미 열람된 이력서입니다.")
            index+=1
            continue
        print("반가워...!!")
        time.sleep(2)
        openBtn = browser.find_element_by_class_name('rsBtNewBnr').find_element_by_tag_name('button')
        openBtn.click()
        time.sleep(3)
        try:
            if browser.find_element_by_id('dev_show_open_msg'): # 알바생 메세지 있는 경우
                print('알바생 메세지가 있습니다.')
                index+=1
                continue
        except NoSuchElementException as e:
            print(e.__dict__['msg'])
        cancleBtn = browser.find_element_by_xpath('//*[@id="dev_resume_open_layer"]/div[3]/p/button[2]')
        cancleBtn.click()
        # okBtn = browser.find_element_by_class_name('lyBottom').find_element_by_css_selector('#dev_resume_open_layer > div.lyBottom > p > button.on.confirmBtn.dev_btn_2')
    # browser.close()
    
    # quit 맞는지 확인해야함
    index+=1

print("for문 빠져나왔음")
# 1번째 창 빼고 다 닫기
# browser.quit()
time.sleep(1000)

