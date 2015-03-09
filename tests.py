import unittest
from pac import *

class tests_of_pacman(unittest.TestCase):
	def test_check_ghost_correctly(self):
		gen1.create_board(35,15)
		gen1.z[4][5]='P'
		gen1.z[5][5]='G'
		newghost.y=5
		newghost.x=5
		inp = 'd'
		new_maze=Pacman(4,5,0,inp)
		new_maze.predict_next(inp)
		new_maze.checkGhost()
		self.assertEqual(-1,new_maze.state)



	def test_check_wall_correctly(self):
		gen1.create_board(35,15)
		gen1.z[4][5]='P'
		gen1.z[5][5]='X'
		inp = 'd'
		new_maze=Pacman(4,5,0,inp)
		new_maze.predict_next(inp)
		new_maze.checkWall()
		self.assertEqual(-2,new_maze.state)


	def test_check_pacman_score_correctly(self):
		gen1.create_board(35,15)
		gen1.z[4][5]='P'
		gen1.z[5][5]='C'
		inp = 'd'
		new_maze=Pacman(4,5,0,inp)
		new_maze.predict_next(inp)
		new_maze.collectCoin()
		self.assertEqual(1,new_maze.score)


	def test_pacman_moves_correctly(self):
		gen1.create_board(35,15)
		gen1.z[4][5]='P'
		inp = 'd'
		expected = [5,5]
		new_maze=Pacman(4,5,0,inp)
		new_maze.predict_next(inp)
		result = [ new_maze.nexty , new_maze.nextx ]
		self.assertEqual(result,expected)

	def test_pacman_border(self):
		gen1.create_board(35,15)
		gen1.z[14][34]='P'
		inp = 'd'
		expected = [14,0]
		new_maze=Pacman(34,14,0,inp)
		new_maze.predict_next(inp)
		result = [ new_maze.nexty , new_maze.nextx ]
		self.assertEqual(result,expected)

	def test_error_handling_for_input(self):
		gen1.create_board(35,15)
		gen1.z[14][34]='P'
		inp = 'k'
		new_maze = Pacman(34,14,0,inp)
		self.assertRaises(NameError,new_maze.predict_next(inp))

	def test_check_quit(self):
		gen1.create_board(35,15)
		gen1.z[14][34] = 'P'
		inp = 'q'
		new_maze = Pacman(34,14,0,inp)
		result = new_maze.newquit()
		self.assertEqual(1,result)

	def test_board_reload(self):
		inp = 'd'
		new_maze = Pacman(34,14,50,inp)
		result = new_maze.check_reload()
		self.assertEqual(1,result)


