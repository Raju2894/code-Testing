import random
class gen():
	def __init__(self):
		self.z = ['.' for y in range(35) for x in range(15)]
		self.no_coins = 0
	def create_board(self, m, n):
		self.z=[['.' for _ in range(m)] for _ in range(n)]
		x = random.randint(1,33)
		y = random.randint(1,13)
		for r in range(14):
			self.z[r][x] = 'X'
		for r in range(34):
		 	self.z[y][r] = 'X'
		xnew1 = random.randint(0,x-1)
		xnew2 = random.randint(x+1,34)
		ynew1 = random.randint(0,y-1)
		ynew2 = random.randint(y+1,14)
		self.z[y][xnew1] = '.'
		self.z[y][xnew2] = '.'
		self.z[ynew1][x] = '.'
		self.z[ynew2][x] = '.'
	def coins(self):  		#this function puts 25 coins on the board except the wall positions
		self.no_coins=0
		while 1:
			e = random.randint(0,34) 
			f = random.randint(0,14)
			if self.z[f][e] == '.' :
				self.z[f][e] = 'C'
				self.no_coins += 1
			if self.no_coins == 25:
				break
def initialpac():
	global xt,yt #this has the initial pacman position
	xt = random.randint(0,34)
	yt = random.randint(0,14)
	gen1.z[yt][xt] = 'P'

def initialghost():	#it has initial ghost position
	global x1,y1
	x1 = random.randint(0,34)
	y1 = random.randint(0,14)
	if gen1.z[y1][x1] == '.':
		gen1.z[y1][x1] = 'G'
	else:
		return initialghost()

class Person(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y


class Pacman(Person):			#this class of pacman inherits the "Person" class
	def __init__(self, x, y, score, input):
		Person.__init__(self,x,y)
		self.state = 1
		self.score = score
		self.position = [x,y]
		self.nextx = 0
		self.nexty = 0
		self.input = input
	def check_reload(self):
		if self.score % 25 == 0 and self.score != 0 :
			return 1
		return 0

	def checkGhost(self):
		global xp,yp
		if yp == newghost.y and xp == newghost.x:
			self.state = -1

	def checkWall(self):
		global xp,yp
		if gen1.z[yp][xp] == 'X':
			self.state = -2
	def collectCoin(self):
		global xp,yp
		if gen1.z[yp][xp] == 'C':
			self.score += 1
		return self.score

	def newquit(self):
		if self.input == 'q' :
			return 1
		return 0

	def  predict_next(self, input):
		global xp,yp
		if input == 'w':
			xp = self.x
			if self.y-1 > -1:
				yp = self.y - 1
			else:
				yp = 14

		elif input == 's':
			xp = self.x
			if self.y + 1 < 15:
				yp = self.y + 1
			else:
				yp = 0

		elif input == 'a':
			if self.x -1 > -1:
				xp = self.x - 1
			else:
				xp = 34
			yp = self.y
		elif input == 'd':
			if self.x + 1 < 35:
				xp = self.x + 1
			else:
				xp = 0
			yp = self.y

		self.nexty = yp
		self.nextx = xp

	def changepos(self):
		if self.state != -1 and self.state != -2:
			gen1.z[yp][xp] = 'P'
			gen1.z[self.y][self.x] = '.'
		else:
			load = 1

class Ghost(Person):		#the ghost class also inherits person class
	def __init__(self,x,y):
		Person.__init__(self,x,y)
		self.newgx = 0
		self.newgy = 0

	def predictnew(self):
		global ghostx,ghosty
		while 1:
			effect = random.randint(1,4)
			if effect == 1 and self.y +1 < 15:
				self.newgx = self.x
				self.newgy = self.y +1
				break
			elif effect == 2 and self.y -1 > -1:
				self.newgx = self.x
				self.newgy = self.y -1
				break
			elif effect == 3 and self.x - 1 > -1:
				self.newgx = self.x-1
				self.newgy = self.y
				break
			elif effect == 4 and self.x + 1 < 35:
				self.newgx = self.x + 1
				self.newgy = self.y
				break
		#print ghosty,ghostx

gen1 = gen()
gen1.create_board(35,15)  #this imports board created with walls placed  initially

gen1.coins()
initialpac()
initialghost()
scored = 0

new_maze = Pacman(xt,yt,scored,0)		#class instance created here--->polymorphism
newghost = Ghost(x1,y1)

