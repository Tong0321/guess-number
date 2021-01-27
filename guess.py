import random
number = random.randint(1, 100)
while True:
	guess = input('請在1～100間猜一個數字')
	guess =int(guess)
	if guess == number:
		print('猜對了！！')
		break
	elif guess < number and guess > 0:
		print('比數字小')
	elif guess > number and guess <= 100:
		print('比數字大')
	else:
		print('只能猜1～100的數字')