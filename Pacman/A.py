#!/usr/bin/python
import random
from A1 import *

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

for i in a:
    a[i] = ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
k = 0
fast = 20
while fast > 0:
    r = random.randint(0, 14)
    b = random.randint(0, 34)
    if a[r][b] == '.':
        a[r][b] = 'C'
        fast = fast - 1
        k = k + 1
	





for h in range(30):
	y = random.randint(0, 14)
	l = random.randint(0, 34)
	if a[y][l] == '.':
		a[y][l] = 'X'
l = []
for i in range(1):
	eg9 = random.randint(1, 13)
	eg10 = random.randint(1, 33)
	if a[eg9][eg10] == '.':
		a[eg9][eg10] = 'P'
cnt = 4
while cnt > 0:
	eg7 = random.randint(1, 13)
	eg8 = random.randint(1, 33)
	if a[eg7][eg8] == '.':
		a[eg7][eg8] = 'G'
		l.append(eg7)
		l.append(eg8)
		cnt = cnt - 1


flag = 0
coins = 20
score = 0
eg = 0



class ghost(person):
	def __init__(self, x, y, risk):
		person.__init__(self, x, y)
		global eg
		self.prev = 0
		self.flag1 = risk

	def left1(self):
		if self.y != 0:
			if a[self.x][self.y-1] == 'X' or a[self.x][self.y-1] == 'G':
				pass
			elif a[self.x][self.y-1] == 'C' or a[self.x][self.y-1] == '.':
				if self.prev == 1:
					a[self.x][self.y] = 'C'
				else:
					a[self.x][self.y] = '.'
				self.prev = 0
				if a[self.x][self.y-1] == 'C':
					self.prev = 1
				a[self.x][self.y-1] = 'G'
				self.y = self.y-1
	def right1(self):
		if self.y != 34:
			if a[self.x][self.y+1] == 'X' or a[self.x][self.y+1] == 'G':
				pass
			elif a[self.x][self.y+1] == 'C' or a[self.x][self.y+1] == '.':
				if self.prev == 1:
					a[self.x][self.y] = 'C'
				else:
					a[self.x][self.y] = '.'
				self.prev = 0
				if a[self.x][self.y+1] == 'C':
					self.prev = 1
				a[self.x][self.y+1] = 'G'
				self.y = self.y+1

		

	def up1(self):
		if self.x != 0:
			if a[self.x-1][self.y] == 'X' or a[self.x-1][self.y] == 'G':
				pass
			elif a[self.x-1][self.y] == 'C' or a[self.x-1][self.y] == '.':
				if self.prev == 1:
					a[self.x][self.y] = 'C'
				else:
					a[self.x][self.y] = '.'
				self.prev = 0
				if a[self.x-1][self.y] == 'C':
					self.prev = 1
				a[self.x-1][self.y] = 'G'
				self.x = self.x - 1

		
	def down1(self):
		if self.x != 14:
			if a[self.x+1][self.y] == 'X' or a[self.x+1][self.y] == 'G':
				pass
			elif a[self.x+1][self.y] == 'C' or a[self.x+1][self.y] == '.':
				if self.prev == 1:
					a[self.x][self.y] = 'C'
				else:
					a[self.x][self.y] = '.'
				self.prev = 0
				if a[self.x+1][self.y] == 'C':
					self.prev = 1
				a[self.x+1][self.y] = 'G'
				self.x = self.x+1



	def Ghostposition(self):
#			ghost movement
			pass




class pacman(person):
	def __init__(self, x, y):
		person.__init__(self , x, y)
		
	def moveleft(self):
		global score
		global coins
		if self.y != 0:
			if a[self.x][self.y-1] == 'X':
				pass
			elif a[self.x][self.y-1] == 'C':
				a[self.x][self.y-1] = 'P'
				a[self.x][self.y] = '.'
				self.y = self.y-1
				score = score + 1
				coins = coins-1
			elif a[self.x][self.y-1] == 'G':
				print "  OOPS! GAME OVER"
				global flag
				flag = 1
			elif a[self.x][self.y-1] == ".":
				a[self.x][self.y] = "."
		        	a[self.x][self.y-1] = "P"
				self.y = self.y-1

	def moveright(self):
		global coins
		global score
		if self.y != 34:
			if a[self.x][self.y+1] == 'X':
				pass
			elif a[self.x][self.y+1] == 'C':
				a[self.x][self.y+1] = 'P'
				a[self.x][self.y] = '.'
				self.y = self.y+1
				score = score + 1
				coins = coins-1
			elif a[self.x][self.y+1] == 'G':
				print "  OOPS! GAME OVER"
				global flag
				flag = 1
			elif a[self.x][self.y+1] == ".":
				a[self.x][self.y] = "."
			        a[self.x][self.y+1] = "P"
				self.y = self.y+1
	
	def moveup(self):
		global coins
		global score
		if self.x != 0:
			if a[self.x-1][self.y] == 'X':
				pass
			elif a[self.x-1][self.y] == 'C':
				a[self.x-1][self.y] = 'P'
				a[self.x][self.y] = '.'
				self.x = self.x-1
				score = score + 1
				coins = coins-1
			elif a[self.x-1][self.y] == 'G':
				print "  OOPS! GAME OVER"
				global flag
				flag = 1
			elif a[self.x-1][self.y] == ".":
				a[self.x][self.y] = "."
		        	a[self.x-1][self.y] = "P"
				self.x = self.x-1
	def movedown(self):
		global coins
		global score
		if self.x != 14:
			if a[self.x+1][self.y] == 'X':
				pass
			elif a[self.x+1][self.y] == 'C':
				a[self.x+1][self.y] = 'P'
				a[self.x][self.y] = '.'
				self.x = self.x+1
				score = score + 1
				coins = coins-1
			elif a[self.x+1][self.y] == 'G':
				print "  OOPS! GAME OVER"
				global flag
				flag = 1
			elif a[self.x+1][self.y] == ".":
				a[self.x][self.y] = "."
			       	a[self.x+1][self.y] = "P"
				self.x = self.x+1

	
	def collectcoins(self):
		global coins
		print "no of coins are there "
	def checkghost(self):
		global flag
		print "  OOPS!  GAME OVER"
#	print "score ="
#		print score
		flag = 1
#prints pacman 	
	def put(self):
		for k in range(15):
			for m in range(35):
				print a[k][m],
			print ('\n')



if __name__ == "__main__":

        p = pacman(eg9, eg10)
	n = ghost(l[0], l[1], 0)
	n1 = ghost(l[2], l[3], 0)
	n3 = ghost(l[4], l[5], 0)
	n2 = ghost(l[6], l[7], 0)
	p.put()
	print "score =",
	print score
	while flag != 1:
#ghost 4
		
		eg = 0
		eg = random.randint(1, 1000)
		eg = eg%4
		if eg == 0:
			n.left1()
		elif eg == 1:
			n.right1()
		elif eg == 2:
			n.up1()
		elif eg == 3:
			n.down1()
#ghost 1
		eg1 = 0
		eg1 = random.randint(1, 1000)
		eg1 = eg1%4
		if eg1 == 0:
			n1.left1()
		elif eg1 == 1:
			n1.right1()
		elif eg1 == 2:
			n1.up1()
		elif eg1 == 3:
			n1.down1()
#ghost 3
		eg3 = 0
		eg3 = random.randint(1, 1000)
		eg3 = eg3%4
		if eg3 == 0:
			n3.left1()
		elif eg3 == 1:
			n3.right1()
		elif eg3 == 2:
			n3.up1()
		elif eg3 == 3:
			n3.down1()
#ghost 2
		eg2 = 0
		eg2 = random.randint(1, 1000)
		eg2 = eg2%4
		if eg2 == 0:
			n2.left1()
		elif eg2 == 1:
			n2.right1()
		elif eg2 == 2:
			n2.up1()
		elif eg2 == 3:
			n2.down1()




#pacman to move conditions

		if flag == 0:
			var = raw_input("Enter move:")
			

			if var == 'q':
				p.checkghost()
			else:
	   			if var == 's':
	   				p.movedown()
	   			elif var == 'd':
	   				p.moveright()
		   		elif var == 'w':
	   				p.moveup()
	   			elif var == 'a':
	   				p.moveleft()
			p.put()
			print "score = ",
			print score
# this will reload the coins
			if coins == 0:
				fast = 20
				while fast > 0:
					r = random.randint(0, 14)
					b = random.randint(0, 34)
					if a[r][b] == '.':
						a[r][b] = 'C'
						fast = fast - 1
	
				coins = 20
						

				

	







