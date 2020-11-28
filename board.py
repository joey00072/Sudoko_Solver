import pygame
import time
from sudoko_solver import Sudoko

pygame.init()
pygame.font.init()

MYFONT = pygame.font.SysFont('Comic Sans MS', 30)
WHITE,BLACK,GRAY=(255,255,255),(0,0,0),(125,125,125)
WIDTH= 600
HIGHT= WIDTH
RUN=True
screen = pygame.display.set_mode((WIDTH,HIGHT))


class Board(Sudoko):
	"""docstring for Board"""
	def __init__(self, grid):
		super(Sudoko, self).__init__()
		self.grid = grid
		self.size=9
		self.sleep=0.2

	def drawGrid(self):
		screen.fill(WHITE)
		sq_width = sq_hight = int((1.01)/self.size * WIDTH)
		for i in range(self.size):
		        for j in range(self.size):
		                if self.grid[i][j]!=0 :
		                	num=MYFONT.render(str(grid[i][j]), False, (0, 0, 0))
		                	x_pos= int((j)/self.size * WIDTH)+ 10
		                	y_pos= int((i)/self.size * WIDTH)+ 10
		                	screen.blit(num,(x_pos,y_pos))
		                    # pygame.draw.rect(screen,WHITE,[ int((j)/self.size * WIDTH), int((i)/self.size * WIDTH)  , sq_width ,sq_hight])
		for i in range(self.size):
			pygame.draw.line(screen,BLACK,( int((i+1)/self.size * WIDTH) ,0),(int((i+1)/self.size * WIDTH),WIDTH),3 if (i+1)%3==0 else 1)
			pygame.draw.line(screen,BLACK,(0,int((i+1)/self.size * WIDTH)),(WIDTH,int((i+1)/self.size * WIDTH)),  3  if (i+1)%3==0 else 1)
		# print("HH")
	def solve(self):
		pygame.display.update()
		if self.sleep:
			time.sleep(self.sleep/2)
			self.drawGrid()
			time.sleep(self.sleep/2)
			

		yx=self.findEmpty()
		if yx:
			y,x=yx
		else:
			return True

		for n in range(1,10):
			if self.isValid(n,y,x):
				self.grid[y][x]=n
				if self.solve():
					return True
				self.grid[y][x]=0


		return False
				
		


grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0], 
        [5, 2, 0, 0, 0, 0, 0, 0, 0], 
        [0, 8, 7, 0, 0, 0, 0, 3, 1], 
        [0, 0, 3, 0, 1, 0, 0, 8, 0], 
        [9, 0, 0, 8, 6, 3, 0, 0, 5], 
        [0, 5, 0, 0, 9, 0, 6, 0, 0], 
        [1, 3, 0, 0, 0, 0, 2, 5, 0], 
        [0, 0, 0, 0, 0, 0, 0, 7, 4], 
        [0, 0, 5, 2, 0, 6, 3, 0, 0]] 

sudoko_board=Board(grid)

while RUN:
	screen.fill(WHITE)
	pygame.time.delay(100)
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
					RUN=False
					break
	# sudoko_board.drawGrid()
	# sudoko_board.printGrid()
	sudoko_board.solve()
	pygame.display.update()

