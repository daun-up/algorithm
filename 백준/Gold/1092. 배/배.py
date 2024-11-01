n = int(input())
cranes = list(map(int, input().split()))
m = int(input())
boxes = list(map(int, input().split()))

cranes.sort(reverse=True)
boxes.sort(reverse=True)

count = 0

if boxes[0] > cranes[0]:
    count = -1
else:
    while boxes:
        for crane in cranes:
            if boxes and crane < boxes[-1] :
                continue
            for i in range(len(boxes)):
                if crane >= boxes[i]:
                    boxes.pop(i)  
                    break
        count += 1
print(count)