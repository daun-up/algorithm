def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):  # completion 길이에 맞춰 탐색
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]  # 끝까지 같으면 마지막 참가자가 미완주자