hour, minute = map(int, input().split())

if(minute<45):
    minute = 60+minute-45
    hour -=1
    if(hour == -1):
        hour = 23
elif(minute>=45):
    minute = minute - 45

print(hour, minute)

