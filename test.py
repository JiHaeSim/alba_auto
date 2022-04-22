str = '대학(4년제) 휴학'

if '재학' in str:
    print("우리와 함께 하실 수 없습니다.")
    if '휴학' in str:
        print("우리와 함께 하실 수 없습니다.")
else:
    print("반가워...!!")
    
    
if '휴학' in str:
    print('휴학중')
elif '재학' in str:
    print('재학중')
else:
    print("반가워")