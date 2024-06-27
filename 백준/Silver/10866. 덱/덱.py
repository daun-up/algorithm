from collections import deque
import sys
 
N = int(sys.stdin.readline().strip())
deque = deque()

for i in range(N) :
    cmd = sys.stdin.readline().strip().split()
    if (cmd[0] == 'push_back') :
        deque.append(cmd[1])
    elif (cmd[0] == 'push_front') :
        deque.appendleft(cmd[1])
    elif (cmd[0] == 'pop_front') :
        if len(deque) == 0:
            print(-1)
        else : print(deque.popleft())
    elif (cmd[0] == 'pop_back') :
        if len(deque) == 0:
            print(-1)
        else : print(deque.pop())
    elif (cmd[0] == 'size') :
        print(len(deque))
    elif (cmd[0] == 'empty') :
        if len(deque) == 0:
            print(1)
        else : print(0)
    elif (cmd[0] == 'front'):
        if len(deque) != 0:
            print(deque[0])
        else : print(-1)
    elif (cmd[0] == 'back'):
        if len(deque) != 0:
            print(deque[-1])
        else : print(-1)
        
