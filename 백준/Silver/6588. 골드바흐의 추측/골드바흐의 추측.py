# 소수 먼저 판별
import sys
input = sys.stdin.readline

r = 1000000

check = [True] * r

def main() :
    # 에라토스테네스의 체
    for i in range(2, int(r**0.6)) : # i 번째 인덱스가 소수일 때
        if check[i] :
            for j in range(i*2, r, i) : # i 의 배수가 있을 때
                check[j] = False # 그 수는 false 

    while True : # 입력 받은 수가 에라토스테네스의 체에 속하는지?
        n = int(input().strip())
        
        if n == 0 :
            break
        else :
            for i in range(3,r) :
                if check[i] :
                    if check[n-i] :
                        print("%d = %d + %d"%(n, i, n-i))
                        break

if __name__ == "__main__":
    main()