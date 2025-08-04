string = input()

# for i in range(data) :
exp = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# z= 가 dz= 보다 앞에 있으면 z= 를 우선으로 바꿔 버리게 되므로 순서 유의

for i in exp :
    # 크로아티아 알파벳이 입력 값에 있다면, 한글자 알파벳으로 치환
    string = string.replace(i, 'a')
    # i 를 'a' 로 바꾼다.
    
print(len(string))