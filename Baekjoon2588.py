number_01 = int(input())
number_02 = int(input())

print(number_01 * (number_02%10))
print(number_01 * ((number_02%100)//10))
print(number_01 * (number_02//100))
print(number_01 * number_02)