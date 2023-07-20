from lib import *

def roll_the_dice():
	a = random.randint(1,6)
	b = random.randint(1,6)
	c = random.randint(1,6)

	result  = a + b + c
	if result>= 11 and result <=17:
		final = 1
	elif result >=4 and result<=10:
		final = 0
	return [a,b,c,final]