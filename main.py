from audioop import add
from lib2to3.pgen2 import driver
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import NoSuchElementException
import random
import pandas as pd
from openpyxl import load_workbook
import os
import shutil

# (이력서 열람 오류를 위해 추가한 부분)
'''
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options)
'''

id = input("아이디: ")
pw = input("비밀번호: ")

browser = webdriver.Chrome('chromedriver.exe')
browser.get("https://www.albamon.com/login/logout_trans.asp")
# browser.set_window_size(1920,1280)

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
employee = []
# for href in hrefList:
while index < 10:
    time.sleep(random.randrange(5))
    # script = f"window.open('{href}')"
    script = f"window.open('{hrefList[index]}')"
    browser.execute_script(script)
    browser.switch_to.window(browser.window_handles[index]) # 현재 페이지로 활성화 해줘야했음 ㅠㅠ
    
    # 이력서 삭제된 경우 수정해야함 (팝업 확인 안됨)
    try:
        if browser.current_url=="https://www.albamon.com/ResumeSearch":
            browser.quit()
            continue
    except UnexpectedAlertPresentException as e:
        print(e.__dict__['msg'])
    
    time.sleep(3)
    
    point = browser.find_element_by_class_name('point') # 최종학력

    print(browser.find_element_by_class_name('name').get_attribute('innerText'))
    print(point.get_attribute('innerText'))
    if '재학' in point.get_attribute('innerText'):
        print("우리와 함께 하실 수 없습니다.")
    elif '휴학' in point.get_attribute('innerText'):
        print("우리와 함께 하실 수 없습니다.")
    else:
        try:
            suggestBtn = browser.find_element_by_class_name('devBtnSuggestAlba') # 알바제의
            if suggestBtn:
                print('알바제의 따위는 하지 않는다.')
                index+=1
                continue
        except NoSuchElementException as e:
            print(e.__dict__['msg'])
        if "O" not in browser.find_element_by_class_name('name').get_attribute('innerText'): # 열람된 이력서
            print("이미 열람된 이력서입니다.")
            index+=1
            continue
        print("반가워...!!")
        time.sleep(2)
        openBtn = browser.find_element_by_class_name('rsBtNewBnr').find_element_by_tag_name('button')
        openBtn.click() # 이력서 열람
        time.sleep(3)
        try:
            if browser.find_element_by_id('dev_show_open_msg'): # 알바생 메세지 있는 경우
                print('알바생 메세지가 있습니다.')
                index+=1
                continue
        except NoSuchElementException as e:
            print(e.__dict__['msg'])
        cancleBtn = browser.find_element_by_xpath('//*[@id="dev_resume_open_layer"]/div[3]/p/button[2]')
        okBtn = browser.find_element_by_class_name('lyBottom').find_element_by_css_selector('#dev_resume_open_layer > div.lyBottom > p > button.on.confirmBtn.dev_btn_2')
        # okBtn = browser.find_element_by_class_name('on confirmBtn dev_btn_2')
        # cancleBtn.click()
        okBtn.click()
        name = browser.find_element_by_class_name('name').get_attribute('innerText')
        gender = browser.find_element_by_class_name('gender').get_attribute('innerText')
        age = browser.find_element_by_class_name('age').get_attribute('innerText')
        address = browser.find_element_by_xpath('//*[@id="layer_ggViewWrap"]/section/article[1]/div[2]/div[2]/ul/li[1]/span[2]').get_attribute('innerText')
        phone = browser.find_element_by_xpath('//*[@id="layer_ggViewWrap"]/section/article[1]/div[2]/div[2]/ul/li[2]/span[2]').get_attribute('innerText').split()[0]
        email = browser.find_element_by_xpath('//*[@id="layer_ggViewWrap"]/section/article[1]/div[2]/div[2]/ul/li[3]/span[2]').get_attribute('innerText').split()[0]
        person = [name, gender, age, address, phone, email]
        print(person)
        employee.append(person)
    index+=1

print("for문 빠져나왔음")
print(employee)
employeeExcel = pd.DataFrame(employee)
dir_path = './excel'
dir = './excel'+time.strftime('%Y-%m-%d', time.localtime(time.time()))+'.xlsx'
if os.path.exists(dir_path):
    shutil.rmtree(dir_path)
os.makedirs(dir_path)

with pd.ExcelWriter(dir) as writer:
    employeeExcel.to_excel(writer, sheet_name=time.strftime('%Y-%m-%d', time.localtime(time.time())))
        
time.sleep(1000)

