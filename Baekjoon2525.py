hour, minute = map(int, input().split())
cook_minute = int(input())

if(minute + cook_minute >= 60):
    temp_share = (minute + cook_minute) // 60
    temp_remain = (minute + cook_minute) % 60
    hour = hour + temp_share
    if(hour >= 24):
        hour = hour - 24
    if(temp_remain == 0):
        # 60으로 나누어 떨어진다는 소리니까 minute = 0
        minute = 0
    else:
        minute = temp_remain
else :
    minute = minute + cook_minute
print(hour, minute)