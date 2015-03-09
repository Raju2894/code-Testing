#z is board
#coins="25" fixed for one board,and it is globally declared
from pac import *


print '\n'.join([' '.join(row) for row in gen1.z])
newer = 0
load = 0
while load != 1  :
    print "Your score:"+ str(scored)
    r = raw_input('Enter your move: ')
    new_maze=Pacman(new_maze.x,new_maze.y,new_maze.score,r)		#class instance created here--->polymorphism

    if new_maze.newquit() == 1:
        load=1
        print "YOU QUIT"
        break
	#print x1,y1
    new_maze.predict_next(r)
    newghost.predictnew()
    new_maze.checkGhost()
    new_maze.checkWall()
    scored = new_maze.collectCoin()
    if new_maze.state != -1 and new_maze.state != -2:
        new_maze.changepos()
        if gen1.z[newghost.newgy][newghost.newgx] == '.':
            gen1.z[newghost.newgy][newghost.newgx] = 'G'
            gen1.z[newghost.y][newghost.x] = '.'
            newghost.x = newghost.newgx
            newghost.y = newghost.newgy
        new_maze.position[0] = new_maze.nextx
        new_maze.position[1] = new_maze.nexty
        new_maze.x = new_maze.nextx
        new_maze.y = new_maze.nexty
    else:
        print "OOPS! SORRY GAME IS OVER... TRY AGAIN"
        break
    if new_maze.state != -1 and new_maze.state != -2:
        print '\n'.join([' '.join(row) for row in gen1.z])
    if newer == 0 and new_maze.check_reload() == 1 :  		#from  this part of code, board gets reloaded when all the coins are collected
        newer+=1
        gen1.create_board(35,15)
        gen1.coins()
        initialpac()
        initialghost()
        print "---------------------------------------------"
        print "BOARD RELOADED"
        print "-----------------------------------------------"
        print '\n'.join([' '.join(row) for row in gen1.z])
        print "Your level is " + str(newer)
    elif newer != 0 :
        qed = (newer+1) * gen1.no_coins
        if scored == qed:
            newer += 1
            gen1.create_board(35,15)
            gen1.coins()
            initialpac()
            initialghost()
            print "---------------------------------------"
            print "BOARD RELOADED"
            print "----------------------------------------"
            print '\n'.join([' '.join(row) for row in gen1.z])
            print "your level is " + str(newer)
