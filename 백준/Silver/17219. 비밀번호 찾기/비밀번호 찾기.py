import sys
input = sys.stdin.readline 

n,m = map(int,input().split()) 
dic = {} # 사이트와 비밀번호를 딕셔너리로 입력 받는다.

for _ in range(n):
    site,ps = input().split()
    dic[site] = ps

for _ in range(m):
    print(dic[input().rstrip()])
