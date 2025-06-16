# 테스트 케이스는 여러 개로 이루어져 있다

while True :
    try :
        data = int(input())
        str = '1'
        flag = 0
        while flag == 0 :
            if(int(str) % data == 0) :
                print(len(str))
                flag = 1
            else :
                str += '1'
    except EOFError :
        break