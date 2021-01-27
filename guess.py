import random
number = random.randint(1, 100)
count = 0
while True:
	count += 1
	guess = input('請在1～100間猜一個數字')
	guess =int(guess)
	if guess == number:
		print('猜對了！！')
		print('這是你猜的第', count, '次')
		break
	elif guess < number and guess > 0:
		print('比數字小')
	elif guess > number and guess <= 100:
		print('比數字大')
	else:
		print('只能猜1～100的數字')
	print('這是你猜的第', count, '次')