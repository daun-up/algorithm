sl, sr = input().split()

keyboard = {
    'q' : (0,0),
    'w' : (0,1),
    'e' : (0,2),
    'r' : (0,3),
    't' : (0,4),
    'y' : (0,5),
    'u' : (0,6),
    'i' : (0,7),
    'o' : (0,8),
    'p' : (0,9),
    
    'a' : (1,0),
    's' : (1,1),
    'd' : (1,2),
    'f' : (1,3),
    'g' : (1,4),
    'h' : (1,5),
    'j' : (1,6),
    'k' : (1,7),
    'l' : (1,8),
    
    'z' : (2,0),
    'x' : (2,1),
    'c' : (2,2),
    'v' : (2,3),
    'b' : (2,4),
    'n' : (2,5),
    'm' : (2,6),

}


left_hand_keys = set('qwertasdfgzxcv')
right_hand_keys = set('yuiohjklbnm')
target = input()
total_time = 0

for char in target :
    
    if char in left_hand_keys : # 왼손 사용
        start_pos = keyboard[sl]
        end_pos = keyboard[char]
        
        # 시간 계산 및 누적
        distance = abs(start_pos[0] - end_pos[0]) + abs(start_pos[1] - end_pos[1])
        
        total_time += distance + 1 # 이동 시간 + 누르는 시간
        sl = char
    else : # 오른손 사용
        start_pos = keyboard[sr]
        end_pos = keyboard[char]
        
        distance = abs(start_pos[0] - end_pos[0]) + abs(start_pos[1] - end_pos[1])
        
        total_time += distance + 1
        sr = char
print(total_time)