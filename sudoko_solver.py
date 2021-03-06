import time

class Sudoko(object):
	"""docstring for Sudoko"""
	def __init__(self, grid,print_grid=False):
		super(Sudoko, self).__init__()
		self.grid = grid
		self.sleep= None
		self.print_grid = print_grid
	def sleepAndPrint(self,Time=0.2):
		self.sleep=Time

	def printGrid(self):
		for i in range(9):
			if i%3==0 and i!=0:
				print("- - - - - - - - - - -")
			for j in range(9):
				if j%3==0 and j!=0:
					print("|",end=" ")
				print(self.grid[i][j],end=" ")

			print("")
	def getGrid(self):
		return self.grid
	def setPrintGrid(self,flg):
		self.print_grid=flg

	def findEmpty(self):
		'''return empty cell co-ordinate from grid'''
		''' as tuple (y,x)'''
		for y in range(9):
			for x in range(9):
				if self.grid[y][x]==0:
					return (y,x)
		return None

	def isValid(self,n,y,x):
		"""Find No: n is valid in block grid[y][x] """

		sub_y=(y//3)*3	#to get start for 3x3 subGrid
		sub_x=(x//3)*3	

		for i in range(9):
			#check if no n is exist in column y
		 	if i!=y and self.grid[i][x]==n:
		 		return False
		 	#check if no n is exist in row x
		 	if i!=x and self.grid[y][i]==n:
		 		return False

		#To check if no exist 3x3 subGrid
		for i in range(sub_y,sub_y+3):
			for j in range(sub_x,sub_x+3):
				if x!=j and y!=i and self.grid[i][j]==n:
					return False

		return True
	def solve(self):
		if self.sleep:
			time.sleep(self.sleep/2)
			if self.print_grid:
				self.printGrid()
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

if __name__ == '__main__':
	g=Sudoko(grid)
	g.sleepAndPrint()
	g.printGrid()
	g.solve()
	g.printGrid()
	g.printGrid()

	