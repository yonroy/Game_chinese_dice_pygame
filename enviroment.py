from lib import *
from random_a_bet import roll_the_dice

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

def draw_env(display):
	x = 200
	pygame.draw.rect(display, (27, 125, 225,1), (x +20, 20, 160, 160))
	pygame.draw.rect(display, (132, 62, 0,1), (x+200, 20, 160, 160))
	font = pygame.font.SysFont(None, 24)
	img = font.render('Tai', True, BLUE)
	display.blit(img, (x+70, 100))
	img = font.render('Xiu', True, BLUE)
	display.blit(img, (x+250, 100))

def find_codinate_of_mouse(event_list):
	x, y = pygame.mouse.get_pos()
	for event in event_list:
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				print('LEFT MOUSE BUTTON CLICKED')
				if x >=220 and x <=380 and y>=20 and y<=180:
					print('Tai')
					return 1
				elif x >=400 and x <=560 and y>=20 and y<=180:
					print('Xiu')
					return 0
				else:
					print("O")
def count_down(count):
	if count <= 0:
		count = 5
	else:
		count -= 1
	return count

def draw_count_down(count,display):
	font = pygame.font.SysFont(None, 50)
	img = font.render(str(count), True, BLUE)
	display.blit(img, (350, 200))
	pygame.display.flip()
def draw_list_player(list_player,display):
	for player in list_player:
		font = pygame.font.SysFont(None, 50)
		img = font.render(str(player.name), True, BLUE)
		display.blit(img, (270, 300))
		img = font.render(str(player.money), True, BLUE)
		display.blit(img, (450, 300))

def enviroment(list_player):
	# Xòng bạc
	# initialize it
	pygame.init()

	# configurations
	frames_per_second = 30
	window_height = 600
	window_width = 800
	# creating window
	display = pygame.display.set_mode((window_width, window_height))

	# creating our frame regulator
	clock = pygame.time.Clock()

	run = True
	# forever loop
	current_time = 0

	count = 5
	select_of_player  = -1
	while run:
	  # frame clock ticking
		clock.tick(60)
		# time
		time = int(pygame.time.get_ticks()/1000)
		if time - current_time >= 1:
			current_time =  int(pygame.time.get_ticks()/1000)
			count = count_down(count)

			if count == 0:
				results = roll_the_dice()
				print(results)
				# check result
				if select_of_player == -1:
					print("None")
				else:
					if results[-1] == select_of_player:
						print("Win")
						select_of_player  = -1
						list_player[0].win_a_bet(money=100000)
					else:
						print("Lose")
						select_of_player  = -1
				


		
		# event listener
		event_list =  pygame.event.get()
		for event in event_list:
			if event.type == pygame.QUIT:
				run = False

		# draw object
		display.fill((255, 255, 255))
		draw_env(display)
		draw_list_player(list_player,display)
		draw_count_down(count,display)


		select = find_codinate_of_mouse(event_list)
		if select == 1:
			select_of_player = 1
			list_player[0].place_a_bet(money=10000000)
		elif select == 0:
			select_of_player = 0
			list_player[0].place_a_bet(money=1000000)
		


if __name__ == "__main__":
	enviroment("a")