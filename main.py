from lib import *

from player import Player
from enviroment import enviroment


if __name__ == "__main__":
	a = Player("MinhToan",10000000)
	print(a.name)
	list_player = [a]
	enviroment(list_player)