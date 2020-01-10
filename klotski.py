from graphics import *
import numpy as np
from loop import gameLoop
from other_funcs import *



def main():
        win = GraphWin('Klotski', 600, 630)
        win.setBackground('grey')
        level = np.genfromtxt(str(levelSelection(win)) + '.kl', dtype=None)
        red_squares = []
        for i in range(0,15):
                for j in range(0,15):
                        fillSquare(win, j, i, getColor(level[i][j]))
                        if level[i][j] == 1:
                                red_squares.append([j,i])
        
        gameLoop(win,level,red_squares)

        vict_msg_background = Rectangle(Point(120,200), Point(480,400))
        vict_msg_background.setFill('white')

        vict_msg = Text(Point(300,287), 'Game won!\nPress LMB to exit.')
        vict_msg.setSize(20)

        vict_msg_background.draw(win)
        vict_msg.draw(win)
           
        win.getMouse()
main()