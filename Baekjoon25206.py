#전공평점은 전공과목별 학점 * 과목평점의 합
sum : float = 0.0
sum_avg : float = 0.0
point_sum : float = 0.0
for i in range(0, 20):
    name, point, score = input().split()
    name = str(name)
    point = float(point)
    score = str(score)
    if(score == 'P'):
        point_sum += 0
    else:
        point_sum += point

    if (score == 'A+'):
        major = 4.5
    elif score == 'A0':
        major = 4.0
    elif score == 'B+':
        major = 3.5
    elif score == 'B0':
        major = 3.0
    elif score == 'C+':
        major = 2.5
    elif score == 'C0':
        major = 2.0
    elif score == 'D+':
        major = 1.5
    elif score == 'D0':
        major = 1.0
    elif score == 'F':
        major = 0.0
    else:
        major = 0.0
    
    sum_avg = point * major

    sum += sum_avg

print(round(sum / point_sum, 6))