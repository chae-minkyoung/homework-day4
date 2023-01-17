e2f={'dog':'chien',
     'cat':'chat',
     'walrus':'morse'
     }
while True:
    english = input('영어로 : (종료는 1)')
    if english in e2f:
        print(f'영어로{english}는 프랑스어로 {e2f[english]}입니다.')
    elif english=='1':
        break
    else:
        print('다시 입력하세요')


