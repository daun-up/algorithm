import sys
input = sys.stdin.readline

s = 0  # 비트마스크로 모든 값을 0으로 초기화

for _ in range(int(input())):
    command = input().split()
    
    if command[0] == "add":
        index = int(command[1]) - 1
        s |= (1 << index)  # index 위치의 비트를 1로 설정
        
    elif command[0] == "remove":
        index = int(command[1]) - 1
        s &= ~(1 << index)  # index 위치의 비트를 0으로 설정
        
    elif command[0] == "check":
        index = int(command[1]) - 1
        print(1 if s & (1 << index) else 0)  # index 위치의 비트가 1인지 확인
        
    elif command[0] == "toggle":
        index = int(command[1]) - 1
        s ^= (1 << index)  # index 위치의 비트를 반전
        
    elif command[0] == "all":
        s = (1 << 20) - 1  # 20개의 비트를 모두 1로 설정
        
    elif command[0] == "empty":
        s = 0  # 모든 비트를 0으로 초기화