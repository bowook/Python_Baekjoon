exam_count = int(input())
exam_socre = list(map(int, input().split()))
exam_max_score = max(exam_socre)

for i in range(0, exam_count):
    exam_socre[i] = (exam_socre[i]/exam_max_score) * 100

print(sum(exam_socre) / exam_count)