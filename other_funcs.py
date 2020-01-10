from graphics import *

def fillSquare(win, x, y, color):
        tmp_x = x*40
        tmp_y = y*40
        square = Rectangle(Point(tmp_x, tmp_y), Point(tmp_x+40, tmp_y+40))
        square.setFill(color)
        square.draw(win)

def getColor(n):
    switcher = {
        0: "grey",
        1: "red",
        2: "black",
        3: "green",
        4: "dark orange",
        5: "gold4",
        6: "maroon",
        7: "blue",
        8: "cyan",
        9: "IndianRed2",
        10: "DarkOrchid4",
        11: "yellow",
    }
    return switcher.get(n)
        
def getSelected(block, selected_squares):
        block = Rectangle(Point(selected_squares[0][0]*40, selected_squares[0][1]*40), Point((selected_squares[len(selected_squares)-1][0]+1)*40, (selected_squares[len(selected_squares)-1][1]+1)*40))
        block.setOutline('white')
        block.setWidth(3)
        return block

def clearWindow(win):
    for item in win.items[:]:
        item.undraw()
    win.update()

def levelSelection(win):
        choice_message = Text(Point(300,79),str('Please choose one of the levels'))
        choice_message.setSize(20)
        choice_message.draw(win)
        lvl_num = 1
        for i in range (1,10,3):
                for j in range(4,9,4):
                        tmp_x = i*60
                        tmp_y = j*40
                        option_outline = Rectangle(Point(tmp_x, tmp_y),Point(tmp_x+120, tmp_y+120))
                        lvl_num_display = Text(Point(tmp_x+60,tmp_y+60),str(lvl_num))
                        lvl_num_display.setSize(30)
                        option_outline.setWidth(3)
                        option_outline.draw(win)
                        lvl_num_display.draw(win)
                        lvl_num+=1

        block_is_selected = False
        while(not block_is_selected):                       
                mouse = win.getMouse()
                click_x_raw = mouse.getX()
                click_y_raw = mouse.getY()
                if click_x_raw >= 600 and click_y_raw >= 600:
                        continue
                        
                if 160<=click_y_raw and click_y_raw<=280:
                        if 60<=click_x_raw and click_x_raw<=180:
                                choice = 1
                                block_is_selected = True
                        if 240<=click_x_raw and click_x_raw<=360:
                                choice = 3
                                block_is_selected = True
                        if 420<=click_x_raw and click_x_raw<=540:
                                choice = 5
                                block_is_selected = True
                if 320<=click_y_raw and click_y_raw<=440:
                        if 60<=click_x_raw and click_x_raw<=180:
                                choice = 2
                                block_is_selected = True
                        if 240<=click_x_raw and click_x_raw<=360:
                                choice = 4
                                block_is_selected = True
                        if 420<=click_x_raw and click_x_raw<=540:
                                choice = 6
                                block_is_selected = True
        return choice