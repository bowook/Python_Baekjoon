exam_score = int(input())

if(90 <= exam_score <= 100):
    print('A')
elif(80 <= exam_score <90):
    print('B')
elif(70 <= exam_score < 80):
    print('C')
elif(60 <= exam_score < 70):
    print('D')
else:
    print('F')