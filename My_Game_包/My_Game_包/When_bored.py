import sys

name = 'User'
print('你是否启动 逍遥散人复读机 ?\n \t[Yes] \t[No]\n>>> ', end = '')
a = input()
if 'y' in a or 'Y' in a or 'e' in a or 'E' in a or 's' in a or 'S' in a:
    print('''====================================逍遥散人复读机===================================''')
    print('Your name> ', end = '')
    name = input()
    while 1:
        print('[' + name + ']> ', end = '')
        User_input = input()
        if 'quit' in User_input or '退出' in User_input:
            print('''================================End-逍遥散人复读机-End===============================''')
            sys.exit(0)
        else:
            p = ''.join(User_input.split('吗'))
            p = ''.join(p.split('？'))
            p = ''.join(p.split('么'))
            p = ''.join(p.split('?'))
            p = ''.join(p.split('你'))
            print('[逍遥散人复读机]> ' + p + '!')
else:
    print('================================End-逍遥散人复读机-End===============================')
    sys.exit(0)