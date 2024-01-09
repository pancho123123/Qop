import pygame, random
from random import randint
from pathlib import Path

WIDTH = 1200
HEIGHT = 700
BLACK = (0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = (0, 255, 0)
RED = (255,0,0)
BLUE = (0,0,255)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("qop")
clock = pygame.time.Clock()
current_path = Path.cwd()
file_path = current_path / 'highscore.txt'

def draw_text1(surface, text, size, x, y):
	font = pygame.font.SysFont("serif", size)
	text_surface = font.render(text, True, WHITE)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	surface.blit(text_surface, text_rect)

def draw_text2(surface, text, size, x, y):
	font = pygame.font.SysFont("serif", size)
	text_surface = font.render(text, True, BLACK)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	surface.blit(text_surface, text_rect)

def draw_hp_bar(surface, x, y, percentage):
	BAR_LENGHT = 100
	BAR_HEIGHT = 10
	fill = (percentage / 100) * BAR_LENGHT
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
	pygame.draw.rect(surface, GREEN, fill)
	pygame.draw.rect(surface, WHITE, border, 2)

def draw_mana_bar(surface, x, y, percentage):
	BAR_LENGHT = 100
	BAR_HEIGHT = 10
	fill = (percentage / 100) * BAR_LENGHT
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
	pygame.draw.rect(surface, BLUE, fill)
	pygame.draw.rect(surface, WHITE, border, 2)

class Player1(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		
		self.image = pygame.transform.scale(pygame.image.load("img/qop.png").convert(),(50,65))
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.centerx = 50
		self.rect.centery = HEIGHT * 1/3
		self.speed_x = 0
		self.hp = 100
		self.mana = 100
		

	def update(self):
		self.hp -= 1/25
		self.mana += 1/50
		if self.mana < 0:
			self.mana = 0
		if self.mana > 100:
			self.mana = 100
		if self.hp < 0:
			self.hp = 0
		if self.hp > 100:
			self.hp = 100
		self.speed_x = 0
		self.speed_y = 0
		keystate = pygame.key.get_pressed()
		if self.hp > 0:
			if keystate[pygame.K_a]:
				self.speed_x = -5
			if keystate[pygame.K_d]:
				self.speed_x = 5
			self.rect.x += self.speed_x
			if keystate[pygame.K_w]:
				self.speed_y = -5
			if keystate[pygame.K_s]:
				self.speed_y = 5
			self.rect.y += self.speed_y
		if self.hp == 0:
			self.image = pygame.transform.scale(pygame.image.load("img/fond.png").convert(),(20,20))
			if keystate[pygame.K_a]:
				self.speed_x = 0
			if keystate[pygame.K_d]:
				self.speed_x = 0
			self.rect.x += self.speed_x
			if keystate[pygame.K_w]:
				self.speed_y = 0
			if keystate[pygame.K_s]:
				self.speed_y = 0
			self.rect.y += self.speed_y
		if self.rect.right > WIDTH:
			self.rect.right = WIDTH
		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.top < 10:
			self.rect.top = 10
		if self.rect.bottom > 700:
			self.rect.bottom = 700

class Player2(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		#self.image = pygame.image.load("img/player2.png").convert()
		self.image = pygame.transform.scale(pygame.image.load("img/qop.png").convert(),(50,65))
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.centerx = 50
		self.rect.centery = HEIGHT * 2/3
		self.speed_x = 0
		self.hp = 100
		self.mana = 100
		

	def update(self):
		self.hp -= 1/25
		self.mana += 1/50
		if self.mana < 0:
			self.mana = 0
		if self.mana > 100:
			self.mana = 100
		if self.hp < 0:
			self.hp = 0
		if self.hp > 100:
			self.hp = 100
		self.speed_x = 0
		self.speed_y = 0
		keystate = pygame.key.get_pressed()
		if self.hp > 0:
			if keystate[pygame.K_LEFT]:
				self.speed_x = -5
			if keystate[pygame.K_RIGHT]:
				self.speed_x = 5
			self.rect.x += self.speed_x
			if keystate[pygame.K_UP]:
				self.speed_y = -5
			if keystate[pygame.K_DOWN]:
				self.speed_y = 5
			self.rect.y += self.speed_y
		if self.hp == 0:
			self.image = pygame.transform.scale(pygame.image.load("img/fond.png").convert(),(20,20))
			if keystate[pygame.K_LEFT]:
				self.speed_x = 0
			if keystate[pygame.K_RIGHT]:
				self.speed_x = 0
			self.rect.x += self.speed_x
			if keystate[pygame.K_UP]:
				self.speed_y = 0
			if keystate[pygame.K_DOWN]:
				self.speed_y = 0
			self.rect.y += self.speed_y
		
		if self.rect.right > WIDTH:
			self.rect.right = WIDTH
		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.top < 10:
			self.rect.top = 10
		if self.rect.bottom > 700:
			self.rect.bottom = 700

class Player3(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		
		self.image = pygame.transform.scale(pygame.image.load("img/qop.png").convert(),(50,65))
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.centerx = 1000
		self.rect.centery = HEIGHT * 1/3
		self.speed_x = 0
		self.hp = 100
		self.mana = 100
		

	def update(self):
		self.hp -= 1/25
		self.mana += 1/50
		if self.mana < 0:
			self.mana = 0
		if self.mana > 100:
			self.mana = 100
		if self.hp < 0:
			self.hp = 0
		if self.hp > 100:
			self.hp = 100
		self.speed_x = 0
		self.speed_y = 0
		keystate = pygame.key.get_pressed()
		if self.hp > 0:
			if keystate[pygame.K_j]:
				self.speed_x = -5
			if keystate[pygame.K_l]:
				self.speed_x = 5
			self.rect.x += self.speed_x
			if keystate[pygame.K_i]:
				self.speed_y = -5
			if keystate[pygame.K_k]:
				self.speed_y = 5
			self.rect.y += self.speed_y
		if self.hp == 0:
			self.image = pygame.transform.scale(pygame.image.load("img/fond.png").convert(),(20,20))
			if keystate[pygame.K_j]:
				self.speed_x = 0
			if keystate[pygame.K_l]:
				self.speed_x = 0
			self.rect.x += self.speed_x
			if keystate[pygame.K_i]:
				self.speed_y = 0
			if keystate[pygame.K_k]:
				self.speed_y = 0
			self.rect.y += self.speed_y
		if self.rect.right > WIDTH:
			self.rect.right = WIDTH
		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.top < 10:
			self.rect.top = 10
		if self.rect.bottom > 700:
			self.rect.bottom = 700

class Runa(pygame.sprite.Sprite):
	
	def __init__(self):
		super().__init__()
		
		self.image = runas_images[0]
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(10, WIDTH - 30)
		self.ngo_list = [110, 240, 370, 500]
		self.rect.y = random.randrange(17, HEIGHT - 30)
		self.rangupdate = 3
    
	def update(self):
		if randint(0,10000) < self.rangupdate:
			self.rect.x = random.randrange(10, WIDTH - 30)
			self.rect.y = random.randrange(17, HEIGHT - 30)


def show_go_screen():
	
	screen.fill(BLACK)#(background, [0,0])
	draw_text1(screen, "Qop", 65, WIDTH // 2, HEIGHT // 4)
	draw_text1(screen, "Colecta los cristales para sobrevivir", 20, WIDTH // 2, HEIGHT // 2)
	draw_text1(screen, "Press Q", 20, WIDTH // 2, HEIGHT * 3/4)
	#draw_text(screen, "Created by: Francisco Carvajal", 10,  60, 625)
	
	
	pygame.display.flip()
	waiting = True
	while waiting:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					waiting = False

runas_images = []
runa_list = ["img/runarege.png"]

for img in runa_list:
	runas_images.append(pygame.transform.scale((pygame.image.load(img).convert()),(30,30)))



def get_high_score():
	with open(file_path,'r') as file:
		return file.read()

def show_game_over_screenp1():
	screen.fill(BLACK)
	#draw_text1(screen, "Qop", 65, WIDTH // 2, HEIGHT // 4)
	draw_text1(screen, "Player 1 WINS", 20, WIDTH // 2, HEIGHT // 2)
	draw_text1(screen, "Press Q", 20, WIDTH // 2, HEIGHT * 3/4)

	pygame.display.flip()
	waiting = True
	while waiting:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					waiting = False

def show_game_over_screenp2():
	screen.fill(BLACK)
	#draw_text1(screen, "Qop", 65, WIDTH // 2, HEIGHT // 4)
	draw_text1(screen, "Player 2 WINS", 20, WIDTH // 2, HEIGHT // 2)
	draw_text1(screen, "Press Q", 20, WIDTH // 2, HEIGHT * 3/4)

	pygame.display.flip()
	waiting = True
	while waiting:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					waiting = False

def show_game_over_screenp3():
	screen.fill(BLACK)
	#draw_text1(screen, "Qop", 65, WIDTH // 2, HEIGHT // 4)
	draw_text1(screen, "Player 3 WINS", 20, WIDTH // 2, HEIGHT // 2)
	draw_text1(screen, "Press Q", 20, WIDTH // 2, HEIGHT * 3/4)

	pygame.display.flip()
	waiting = True
	while waiting:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					waiting = False

background = pygame.image.load("img/fond.png")

### high score

try:
	highest_score = int(get_high_score())
except:
	highest_score = 0


game_over1 = False
game_over2 = False
game_over3 = False
running = True
start = True
while running:
	if game_over1:

		show_game_over_screenp1()
		screen.blit(background,(0,0))
		game_over1 = False
		
		all_sprites = pygame.sprite.Group()
		runa_list = pygame.sprite.Group()
		player1 = Player1()
		all_sprites.add(player1)
		player2 = Player2()
		all_sprites.add(player2)
		player3 = Player3()
		all_sprites.add(player3)

		runa = Runa()
		all_sprites.add(runa)
		runa_list.add(runa)

	if game_over2:

		show_game_over_screenp2()
		screen.blit(background,(0,0))
		game_over2 = False
		
		all_sprites = pygame.sprite.Group()
		runa_list = pygame.sprite.Group()
		player1 = Player1()
		all_sprites.add(player1)
		player2 = Player2()
		all_sprites.add(player2)
		player3 = Player3()
		all_sprites.add(player3)

		runa = Runa()
		all_sprites.add(runa)
		runa_list.add(runa)
	
	if game_over3:

		show_game_over_screenp3()
		screen.blit(background,(0,0))
		game_over3 = False
		
		all_sprites = pygame.sprite.Group()
		runa_list = pygame.sprite.Group()
		player1 = Player1()
		all_sprites.add(player1)
		player2 = Player2()
		all_sprites.add(player2)
		player3 = Player3()
		all_sprites.add(player3)

		runa = Runa()
		all_sprites.add(runa)
		runa_list.add(runa)

	if start:
		show_go_screen()
		start = False
		all_sprites = pygame.sprite.Group()
		runa_list = pygame.sprite.Group()
		player1 = Player1()
		all_sprites.add(player1)
		player2 = Player2()
		all_sprites.add(player2)
		player3 = Player3()
		all_sprites.add(player3)

		runa = Runa()
		all_sprites.add(runa)
		runa_list.add(runa)	
		
		
		
		
		


	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False


	
		

	if player1.hp <= 0 and player2.hp <= 0:
		game_over3 = True
	if player2.hp <= 0 and player3.hp <= 0:
		game_over1 = True
	if player1.hp <= 0 and player3.hp <= 0:
		game_over2 = True
	
	all_sprites.update()
	
	
	
	# Checar colisiones - jugador1 - runa
	hits = pygame.sprite.spritecollide(player1, runa_list, True)
	for hit in hits:
		if player1.hp > 0:
			player1.hp += 3
			runa = Runa()
			all_sprites.add(runa)
			runa_list.add(runa)
		elif player1.hp == 0:
			pass
		
	# Checar colisiones - jugador2 - runa
	hits = pygame.sprite.spritecollide(player2, runa_list, True)
	for hit in hits:
		if player2.hp > 0:
			player2.hp += 3
			runa = Runa()
			all_sprites.add(runa)
			runa_list.add(runa)
		elif player2.hp == 0:
			pass

	# Checar colisiones - jugador3 - runa
	hits = pygame.sprite.spritecollide(player3, runa_list, True)
	for hit in hits:
		if player3.hp > 0:
			player3.hp += 3
			runa = Runa()
			all_sprites.add(runa)
			runa_list.add(runa)
		elif player3.hp == 0:
			pass

	screen.blit(background, [0, 0])

	all_sprites.draw(screen)

	#Marcador
	
	#draw_text(screen, str(player.score), 25, WIDTH // 2, 10)
	
	# Escudo.
	draw_text2(screen, "P1", 20, 10, 6)
	draw_text2(screen, "P2", 20, 400, 6)
	draw_text2(screen, "P3", 20, 800, 6)
	
	draw_hp_bar(screen, 20, 5, player1.hp)
	draw_text2(screen, str(int(player1.hp)) + "/100", 10, 70, 6)
	
	draw_hp_bar(screen, 410, 5, player2.hp)
	draw_text2(screen, str(int(player2.hp))+ "/100", 10, 460, 6)
	
	draw_hp_bar(screen, 810, 5, player3.hp)
	draw_text2(screen, str(int(player3.hp))+ "/100", 10, 860, 6)
	
	draw_mana_bar(screen, 20, 15, player1.mana)
	draw_text1(screen, str(int(player1.mana))+ "/100", 10, 70, 16)
	
	draw_mana_bar(screen, 410, 15, player2.mana)
	draw_text1(screen, str(int(player2.mana))+ "/100", 10, 460, 16)
	
	draw_mana_bar(screen, 810, 15, player3.mana)
	draw_text1(screen, str(int(player3.mana))+ "/100", 10, 860, 16)

	pygame.display.flip()