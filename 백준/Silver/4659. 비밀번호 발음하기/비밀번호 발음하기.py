vowels = ['a', 'e', 'i', 'o', 'u'] 

while True :
    password = input().strip()

    if password == "end" :
        break

    cnt1 = 0 # 모음이 있는가
    cnt2, cnt3 = 0, 0 # 모음, 자음이 세 번 이상 반복되는가
    flag = True
    last = ''

    for i in password :
        if i in vowels :
            if cnt2 == 2 or ((i != 'e' and i != 'o') and last == i) :
                flag = False
                break
            else :
                cnt2 += 1
                cnt3 = 0
                cnt1 += 1
                last = i
        else :
            if cnt3 == 2 or last == i :
                flag = False
                break
            else :
                cnt3 += 1
                cnt2 = 0
                last = i

    if cnt1 == 0 :
        flag = False
        

    # if flag :
    #     print ("<%s> is acceptable." %(password))
    # else :
    #     print ("<%s> is not acceptable." %(password))
    if flag:
        print("<{}> is acceptable.".format(password))  # Modified output format
    else:
        print("<{}> is not acceptable.".format(password))  # Modified output format