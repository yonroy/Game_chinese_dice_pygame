from lib import *


class Player():
	def __init__(self,name,money):
		self.name = name
		self.money = money
	def place_a_bet(self,money):
		if money > self.money:
			print("Please bet smaller")
		else:
			self.money -=money
	def win_a_bet(self,money):
		self.money += (money+money)*0.8



if __name__ == "__main__":
	a = Player("a",100)
	b = Player("b",1000)
	c = Player("c",200)
