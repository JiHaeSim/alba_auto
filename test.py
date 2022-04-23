import pandas as pd
from openpyxl import load_workbook
import time
import os
import shutil

# str = '0507-1897-8094 \n안심번호 사용 중\n 통화가능시간 : 09:00~22:00'
str = '상품명: 보몽드 순면스퀘어 솔리드 누빔매트커버, 다크블루 05 Jun 2020'.split()
str2 = '상품명: 슈에뜨룸 선인장 리플 침구 세트, 베이지 05 Jun 2020'.split()
test = []
test.append(str)
test.append(str2)
print(test)

testExcel = pd.DataFrame(test)
dir_path = './excel'
dir = './excel/'+time.strftime('%Y-%m-%d', time.localtime(time.time()))+'.xlsx'
if os.path.exists(dir_path):
    shutil.rmtree(dir_path)
os.makedirs(dir_path)

with pd.ExcelWriter(dir) as writer:
    testExcel.to_excel(writer, sheet_name=time.strftime('%Y-%m-%d', time.localtime(time.time())))