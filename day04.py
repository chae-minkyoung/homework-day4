e2f={'dog':'chien',
     'cat':'chat',
     'walrus':'morse'
     }
f2e={french:english for english,french in e2f.items()}
while True:
    french1 = input('영어로 : (종료는 1)')
    if french1 in f2e:
        print(f'영어로{french1}는 프랑스어로 {f2e[french1]}입니다.')
    elif french1=='1':
        break
    else:
        print('다시 입력하세요')

# while True:
#     english = input('영어로 : (종료는 1)')
#     if english in e2f:
#         print(f'영어로{english}는 프랑스어로 {e2f[english]}입니다.')
#     elif english=='1':
#         break
#     else:
#         print('다시 입력하세요')


