input_num = int(input("Input digits to sum: "))

digits_sum = 0
current_num = input_num
while current_num != 0:
    digits_sum += current_num % 10
    current_num = current_num // 10

print("The sum of digits:", digits_sum)