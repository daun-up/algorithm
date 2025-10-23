def solution(phone_number):
    # return phone_number.replace(phone_number[:-4], '*'*(len(phone_number)-4), 1)
    return '*'*(len(phone_number)-4) + phone_number[-4:]
