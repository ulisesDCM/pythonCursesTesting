import curses
from curses import wrapper
import time

# Basic string in the main screen
def test1(stdscr):
    stdscr.clear()
    for i in range(1,11):
        v = i-0
        stdscr.addstr(i, 0, '10 divided by {} is {}'.format(v, 10/v))
    stdscr.refresh()
    stdscr.getkey()

# Window example 1
def test2(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_YELLOW)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_WHITE)
    BLUE_AND_YELLOW = curses.color_pair(1)
    GREEN_AND_BLACK = curses.color_pair(2)
    RED_AND_WHITE = curses.color_pair(2)

    newWindow = curses.newwin(1, 20, 10, 10)

    for i in range(100):
        newWindow.clear()

        color = BLUE_AND_YELLOW
        if i % 2 == 0:
            color = GREEN_AND_BLACK

        newWindow.addstr(f"Count {i}",color)
        newWindow.refresh()
        time.sleep(0.5)
    
    stdscr.getch()

# Window example 2
def test3(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLUE)
    newWindow = curses.newwin(1, 20, 10, 10)
    newWindow.clear()
    # newWindow.bkgd(curses.color_pair(1))
    newWindow.addstr(f"lines: {curses.LINES-1} " + f"/cols:{curses.COLS-1}", curses.color_pair(1))
    newWindow.getch()
    
    newWindow.mvwin(10,15)
    # newWindow.refresh()
    newWindow.getch()

    newWindow.mvwin(10,15)
    newWindow.refresh()
    newWindow.getch()

    # stdscr.getch()

# Pad example
def test4(stdscr):
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_GREEN)
    pad = curses.newpad(100,100)
    stdscr.refresh()

    for i in range(100):
        for j in range(26):
            char = chr(67+j)
            pad.addstr(char, curses.color_pair(1))
    
    for i in range(50):
        pad.refresh(0, i, 5, 5, 10, 25)
        time.sleep(0.2) 
    stdscr.getch()  #Stop program execution

# Testing first ball movement through the screen
def test5(stdscr):
    ballInitPosX = 0
    ballInitPosY = 0
    ballWinWidth = 2
    ballWinHeight = 1
    ballShape = "@"
    ballSpeedX = 1
    ballSpeedY = 2
    ballNewPosX = 0
    ballNewPosY = 0
    ballCurrPosX = ballInitPosX
    ballCurrPosY = ballInitPosY

    curses.curs_set(0)
    ball = curses.newwin(ballWinHeight,
                            ballWinWidth,
                            ballInitPosX,
                            ballInitPosY)
    ball.clear()
    ball.addstr(ballShape)
    
    while(1):
        # Calculate new ball position
        ballNewPosX = ballCurrPosX + ballSpeedX
        ballNewPosY = ballCurrPosY + ballSpeedY
        
        # Check screen max limit condition in X axis
        if(ballNewPosX >= curses.COLS-2):
            ballSpeedX = ballSpeedX * -1
            ballNewPosX = curses.COLS-2
        elif(ballNewPosX < 0):
            ballSpeedX = ballSpeedX * -1
            ballNewPosX = 0

        # Check screen max limit condition in Y axis
        if(ballNewPosY >= curses.LINES-1):
            ballSpeedY = ballSpeedY * -1
            ballNewPosY = curses.LINES-1
        elif(ballNewPosY < 0):
            ballSpeedY = ballSpeedY * -1
            ballNewPosY = 0

        # Draw the ball
        stdscr.clear()
        stdscr.refresh()
        ball.mvwin(ballNewPosY,ballNewPosX)
        ball.refresh()
        time.sleep(0.01)

        # Update the current position variables
        ballCurrPosX = ballNewPosX
        ballCurrPosY = ballNewPosY

if __name__ == '__main__':
    # wrapper(test1)
    # wrapper(test2)
    # wrapper(test3)
    # wrapper(test4)
    wrapper(test5)