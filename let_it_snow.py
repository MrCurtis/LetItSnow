import pygame
import sys
import random
import cmath

def plot_line(c,v,background):
	pygame.draw.line(background, (255,255,255), (c.imag, c.real), (c.imag + v.imag, + c.real + v.real), 1)

def plot_flake(c1,v1,nn, flake_data, num_k, background):
	nn = nn-1	
	mm = flake_data[nn][1].mm
	for m in range(mm):
		theta = 1.0j*m/mm
		v2 = v1*cmath.exp(2*cmath.pi*theta)
		plot_line(c1,v2,background)
		for k in range(1,num_k[nn]):			
			if nn > 0:
				alpha = flake_data[nn][k].alpha
				beta = flake_data[nn][k].beta
				c2 = c1 + alpha * v2
				v3 = alpha * beta * v2
				plot_flake(c2,v3,nn,flake_data,num_k,background) 

class FlakeData():
	def __init__(self):
		self.alpha = random.random()
		self.beta = random.random()
		self.mm = 6
		
def GetFlake():
	background = pygame.Surface((101,101))
	background = background.convert()
	background.fill((0,0,0))
	flake_data = [[FlakeData() for i in range(1,4)] for j in range(n_max)]
	num_k = [random.randint(1,3) for i in range(n_max)]
	c0 = 50 + 50j
	v0 = 30j
	plot_flake(c0,v0,n_max,flake_data,num_k,background)	
	return background

class Snowflake:
	def __init__(self,h,v):		
		self.image = GetFlake()	
		self.rotate = random.randint(-1,1)
		self.speed = random.random()*0.95 +0.05
		self.h = h
		self.v = v
		self.i = 0

pygame.init()

n_max = 4


screen_res = (1024, 768)

pygame.mouse.set_visible(False)


screen = pygame.display.set_mode(screen_res, pygame.FULLSCREEN)

background = pygame.Surface(screen.get_size())
background = background.convert()

flake = []
for i in range(50):
	flake.append(Snowflake(random.randint(10,screen_res[0]-110), random.randint(-100,screen_res[1]+100)))
	flake[i].image = flake[i].image.convert()
	flake[i].image.set_colorkey((0,0,0))

loop = 1;
while(loop):
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			sys.exit()
			loop = 0
	screen.blit(background,(0,0))	
	for j in range(50):		
		flakey1 = pygame.transform.rotozoom(flake[j].image,flake[j].rotate*flake[j].i, flake[j].speed)
		flakey1.set_colorkey((0,0,0))		
		syze1 = flakey1.get_size()
		h_offset1 = (syze1[0] - 101)/2
		v_offset1 = (syze1[1] - 101)/2
		screen.blit(flakey1,(flake[j].h - h_offset1,flake[j].v - v_offset1 +flake[j].i*flake[j].speed))
		flake[j].i = flake[j].i +1
		if flake[j].i*flake[j].speed > screen_res[1] + 120:
			flake[j] = Snowflake(random.randint(10,screen_res[0]-110), -120)
			flake[j].image.set_colorkey((0,0,0))
	pygame.display.flip()
		#pygame.time.delay(1)


