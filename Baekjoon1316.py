word_count = int(input())
count = word_count

for i in range(word_count):
    word = input()
    for j in range(0, len(word)-1):
        #-1을 해줘야 인덱스 오류 안남
        if word[j] == word[j+1]:
            continue
        elif word[j] in word[j+1:]:
            #연달아 없다란 소리는 어딘가에 있는거니까
            #그룹단어가 아님
            count -= 1
            break


print(count)
