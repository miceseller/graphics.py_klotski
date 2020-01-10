from graphics import *
from other_funcs import *

def gameLoop(win,level,red_squares):
    move_count = 0
    moves_string = 'Moves: ' + str(move_count)
    message = Text(Point(300, 615), moves_string)
    message.draw(win)
    selected_block = None
    game_won = False
    while(not game_won):                       
                    mouse = win.getMouse()
                    click_x_raw = mouse.getX()
                    click_y_raw = mouse.getY()
                    if click_x_raw <= 600 and click_y_raw <= 600:
                            click_x = int(click_x_raw / 40)
                            click_y = int(click_y_raw / 40)
                    else:
                            continue
                    selected_block_num = level[click_y][click_x]
                    selected_squares = []
                    if selected_block_num > 2:
                            for i in range(0,15):
                                    for j in range(0,15):
                                            if level[i][j] == selected_block_num:
                                                    selected_squares.append([j,i])
                            selected_squares_len = len(selected_squares)
                            selected_block = None
                            selected_block = getSelected(selected_block, selected_squares)
                            selected_block.draw(win)
                            move_direction = win.getKey()
                            
                            while move_direction != 'space':
                                    move_successful = None
                                    if move_direction == 'Up':
                                            move_allowed = True
                                            upper_selected_y = selected_squares[0][1]
                                            lower_selected_y = selected_squares[selected_squares_len - 1][1]
                                            if selected_squares[0][1] < 1:
                                                    move_allowed = False
                                                    break
                                            for i in range(selected_squares_len):
                                                    if selected_squares[i][1] == upper_selected_y:
                                                            above_square_color = level[selected_squares[i][1] - 1][selected_squares[i][0]]
                                                            if above_square_color > 1:
                                                                    move_allowed = False
                                                                    break
                                            if not move_allowed:
                                                    break
                                            else:
                                                    move_successful = True
                                                    for i in range(selected_squares_len):
                                                            if selected_squares[i][1] == upper_selected_y:
                                                                    level[selected_squares[i][1] - 1][selected_squares[i][0]] = selected_block_num
                                                                    fillSquare(win, selected_squares[i][0], selected_squares[i][1] - 1, getColor(selected_block_num))
                                                            if selected_squares[i][1] == lower_selected_y:
                                                                    level[selected_squares[i][1]][selected_squares[i][0]] = 0
                                                                    fillSquare(win, selected_squares[i][0], selected_squares[i][1], getColor(0))
                                                            selected_squares[i][1]-=1

                                    if move_direction == 'Down':
                                            move_allowed = True
                                            upper_selected_y = selected_squares[0][1]
                                            lower_selected_y = selected_squares[selected_squares_len - 1][1]
                                            if selected_squares[selected_squares_len - 1][1] == 14:
                                                    move_allowed = False
                                                    break
                                            for i in reversed(range(selected_squares_len)):
                                                    if selected_squares[i][1] == lower_selected_y:
                                                            under_square_color = level[selected_squares[i][1] + 1][selected_squares[i][0]]
                                                            if under_square_color > 1:
                                                                    move_allowed = False
                                                                    break
                                            if not move_allowed:
                                                    break
                                            else:
                                                    move_successful = True
                                                    for i in reversed(range(selected_squares_len)):
                                                            if selected_squares[i][1] == lower_selected_y:
                                                                    level[selected_squares[i][1] + 1][selected_squares[i][0]] = selected_block_num
                                                                    fillSquare(win, selected_squares[i][0], selected_squares[i][1] + 1, getColor(selected_block_num))
                                                    for i in range(selected_squares_len):
                                                            if selected_squares[i][1] == upper_selected_y:
                                                                    level[selected_squares[i][1]][selected_squares[i][0]] = 0
                                                                    fillSquare(win, selected_squares[i][0], selected_squares[i][1], getColor(0))
                                                            selected_squares[i][1]+=1                                
                                    
                                    if move_direction == 'Left':
                                            move_allowed = True
                                            left_selected_x = selected_squares[0][0]
                                            right_selected_x = selected_squares[selected_squares_len - 1][0]
                                            if selected_squares[0][0] < 1:
                                                    move_allowed = False
                                                    break
                                            for i in range(selected_squares_len):
                                                    if selected_squares[i][0] == left_selected_x:
                                                            left_square_color = level[selected_squares[i][1]][selected_squares[i][0] - 1]
                                                            if left_square_color > 1:
                                                                    move_allowed = False
                                                                    break      
                                            if not move_allowed:
                                                    break
                                            else:
                                                    move_successful = True
                                                    for i in range(selected_squares_len):
                                                            if selected_squares[i][0] == left_selected_x:
                                                                    level[selected_squares[i][1]][selected_squares[i][0] - 1] = selected_block_num
                                                                    fillSquare(win, selected_squares[i][0] - 1, selected_squares[i][1], getColor(selected_block_num))
                                                            if selected_squares[i][0] == right_selected_x:
                                                                    level[selected_squares[i][1]][selected_squares[i][0]] = 0
                                                                    fillSquare(win, selected_squares[i][0], selected_squares[i][1], getColor(0))
                                                            selected_squares[i][0]-=1

                                    if move_direction == 'Right':
                                            move_allowed = True
                                            left_selected_x = selected_squares[0][0]
                                            right_selected_x = selected_squares[selected_squares_len - 1][0]
                                            if selected_squares[selected_squares_len - 1][0] == 14:
                                                    move_allowed = False
                                                    break
                                            for i in range(selected_squares_len):
                                                    if selected_squares[i][0] == right_selected_x:
                                                            right_square_color = level[selected_squares[i][1]][selected_squares[i][0] + 1]
                                                            if right_square_color > 1:
                                                                    move_allowed = False
                                                                    break
                                            if not move_allowed:
                                                    break
                                            else:
                                                    move_successful = True
                                                    for i in reversed(range(selected_squares_len)):
                                                            if selected_squares[i][0] == right_selected_x:
                                                                    level[selected_squares[i][1]][selected_squares[i][0] + 1] = selected_block_num
                                                                    fillSquare(win, selected_squares[i][0] + 1, selected_squares[i][1], getColor(selected_block_num))
                                                    for i in range(selected_squares_len):
                                                            if selected_squares[i][0] == left_selected_x:
                                                                    level[selected_squares[i][1]][selected_squares[i][0]] = 0
                                                                    fillSquare(win, selected_squares[i][0], selected_squares[i][1], getColor(0))
                                                            selected_squares[i][0]+=1
                                    if move_successful:
                                            move_count+=1
                                            moves_string = 'Moves: ' + str(move_count)
                                            message.undraw()
                                            message = Text(Point(300, 615), moves_string)
                                            message.draw(win)

                                            for i in range(len(red_squares)):
                                                    tmp_y = red_squares[i][1]
                                                    tmp_x = red_squares[i][0]
                                                    if level[tmp_y][tmp_x] == 0:
                                                            fillSquare(win, tmp_x, tmp_y, 'red')

                                            if (selected_squares == red_squares):
                                                    game_won = True
                                                    continue

                                            selected_block.undraw()  
                                            selected_block = getSelected(selected_block, selected_squares)
                                            selected_block.draw(win)

                                    move_direction = win.getKey()
                            selected_block.undraw()