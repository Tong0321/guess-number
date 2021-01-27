import random
start = input('請決定最小值：') 
end= input('請決定最大值：')
number = random.randint(int(start), int(end))
count = 0
while True:
	count += 1
	guess = input('請在決定的區間內猜一個數字')
	guess =int(guess)
	if guess == number:
		print('猜對了！！')
		print('這是你猜的第', count, '次')
		break
	elif guess < number and guess > int(start):
		print('比數字小')
	elif guess > number and guess <= int(end):
		print('比數字大')
	else:
		print('只能猜區間內的數字')
	print('這是你猜的第', count, '次')