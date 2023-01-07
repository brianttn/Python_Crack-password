pwd = input("請輸入1~3位數密碼(大小寫英文字母或數字)：")
pwdlen = len(pwd)

if pwdlen < 1:
    raise Exception('密碼長度不足!!')
if pwdlen > 3:
    raise Exception('密碼長度太長!!')

acceptNums = [x for x in range(48,123) if (x<=57 or (x>=65 and x<=90) or x>=97)]

for i in range(len(pwd)):
    if ord(pwd[i]) not in acceptNums:
        raise Exception('輸入資料類型錯誤!!')

pwdNotFound = True

for num in range(1,4):
    match (num):
        case (1):
            for char1 in acceptNums:
                if pwdNotFound:
                    code = chr(char1)
                    if code == pwd:
                        print('\nThe cracked password is：', code)
                        pwdNotFound = False
                        break
                        break
                    else:
                        print(code,end=' ')
        case (2):
            for char1 in acceptNums:
                for char2 in acceptNums:
                    if pwdNotFound:
                        code = chr(char1) + chr(char2)
                        if code == pwd:
                            print('\nThe cracked password is：', code)
                            pwdNotFound = False
                            break
                            break
                        else:
                            print(code,end=' ')
        case (3):
            for char1 in acceptNums:
                for char2 in acceptNums:
                    for char3 in acceptNums:
                        if pwdNotFound:
                            code = chr(char1) + chr(char2) + chr(char3)
                            if code == pwd:
                                print('\nThe cracked password is：', code)
                                pwdNotFound = False
                                break
                            else:
                                print(code,end=' ')
