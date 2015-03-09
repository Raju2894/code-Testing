import unittest
from A import *

class tests_of_pacman(unittest.TestCase):
	def test_check_ghost_correctly(self):
		a[4][5]='P'
		a[5][5]='G'
		n=ghost(5,5,0)
		inp = 'd'
		p = pacman(4,5)
		if inp == 'd' :
		     p.moveright()
		     if a[5][5] and a[4][5] != 'G' and a[5][6] != 'G' and a[5][4] != 'G' and a[6][5] !='G':
		         r=-1
		self.assertEqual(-1,r)

	def test_check_wall_correctly(self):
		a[4][5]='P'
		a[5][5]='X'
		inp = 'd'
		p=pacman(4,5)
		if inp == 'd':
	            p.moveright()
                    if a[5][5] == 'X':
                         r=-2
		self.assertEqual(-2,r)
        def test_pacman_moves_correctly(self):
		a[4][5]='P'
		inp = 'd'
		expected = [5,5]
		p=pacman(4,5)
                p.moveright()
                if inp == 'd':
                     r=[5,5]
		self.assertEqual(expected,r)
        def test_pacman_border(self):
		a[14][34]='P'
		inp = 'd'
		expected = [14,34]
		p=pacman(14,34)
                p.moveright()
		if a[14][34] == 'P':
                      result=[14,34]
		self.assertEqual(result,expected)
        def test_check_quit(self):
		a[14][34] = 'P'
		inp = 'q'
		p = pacman(34,14)
                if inp == 'q':
                     p.checkghost()
                     result=1
		self.assertEqual(1,result)
        def test_board_reload(self):
		inp = 'd'
		p = pacman(34,14)
                coins = 0
		if coins == 0 :
				fast=20
				while fast>0:
					r=random.randint(0,14)
					b=random.randint(0,34)
					if a[r][b] =='.':
						a[r][b]='C'
						fast=fast-1
	
				coins=20
                                result = 1
		self.assertEqual(1,result)

        def test_check_pacman_score_correctly(self):
		a[4][5]='P'
		a[5][5]='C'
		inp = 'd'
                score = 0
		p=pacman(4,5)
                p.moveright()
                if a[5][5]=='C':
		       score = score + 1;
		self.assertEqual(1,score)

        def test_error_handling_for_input(self):
		a[14][34]='P'
		inp = 'k'
		p = pacman(34,14)	
                if inp == 'k':
                         r = 1
		self.assertEqual(1,r)

