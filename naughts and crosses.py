from tkinter import *
import random
import copy



def begin(event):
    global grid
    global shape
    global win

    c.configure(bg="light blue")
    c.delete("all")
    win = "None"
    shape = "O"
    grid = [["_", "_", "_"],
            ["_", "_", "_"],
            ["_", "_", "_"]]


    c.create_line(200, 0, 200, 600, fill="white", width="10")
    c.create_line(400, 0, 400, 600, fill="white", width="10")

    c.create_line(0, 200, 600, 200, fill="white", width="10")
    c.create_line(0, 400, 600, 400, fill="white", width="10")
    c.bind("<Button-1>", run)
def run(event):
    global shape


    if win != "None":
        GameWon()
    else:
        click(event)
        lineori, col = check()
        if shape == "X":

            if win == "X" or win == "O":

                if lineori == "v":
                    c.create_line(20, (col * 200)+100 , 580, (col * 200)+100 , fill="green", width="20")
                elif lineori == "h":
                    c.create_line((col * 200)+100, 20, (col * 200)+100, 580, fill="green", width="20")
                elif lineori == "d":
                    if col == 1:
                        c.create_line(20, 20, 580, 580, fill="green", width="20")
                    elif col == 2:
                        c.create_line(580, 20, 20, 580, fill="green", width="20")
            else:
                AIturn()
                lineori, col = check()
                if win == "draw":
                    GameWon()
                if win == "X" or win == "O":

                    if lineori == "v":
                        c.create_line(20, (col * 200) + 100, 580, (col * 200) + 100, fill="green", width="20")
                    elif lineori == "h":
                        c.create_line((col * 200) + 100, 20, (col * 200) + 100, 580, fill="green", width="20")
                    elif lineori == "d":
                        if col == 1:
                            c.create_line(20, 20, 580, 580, fill="green", width="20")
                        elif col == 2:
                            c.create_line(580, 20, 20, 580, fill="green", width="20")
def click(event):
    global shape
    global grid
    global win

    across = int(c.canvasx(event.x)/200)
    down = int(c.canvasy(event.y)/200)
    if grid[down][across] == "_":


        c.create_oval(
            (across*200)+20 , (down*200)+20,
            ((across+1)*200)-20 ,((down+1)*200) -20,
            outline = "yellow", width = "20"
        )
        shape = "X"
        grid[down][across] = "O"




def AIturn():
    global shape
    selected = False

    for a in range(0,3):
        for b in range(0,3):

            testbord = copy.deepcopy(grid)


            if testbord[a][b] == "_":
                testbord[a][b] = "X"
                won = testcheckai(testbord)
                if won == True:
                    across = b
                    down = a
                    selected = True
    if selected == False:
        for a in range(0, 3):
            for b in range(0, 3):
                testbord = copy.deepcopy(grid)
                if testbord[a][b] == "_":
                    testbord[a][b] = "O"

                    pwon = testcheckplayer(testbord)
                    if pwon == True:
                        across = b
                        down = a
                        selected = True

    if selected == False:
        if grid == [["_", "O", "_"],["_", "_", "_"],["_", "_", "_"]] or grid == [["_", "_", "_"],["_", "_", "O"],["_", "_", "_"]]:
            across = 2
            down = 0
            selected = True
        elif grid == [["_", "_", "_"],["_", "_", "_"],["_", "O", "_"]] or grid == [["_", "_", "_"],["O", "_", "_"],["_", "_", "_"]]:
            across = 0
            down = 2
            selected = True
    if selected == False:
        testbord = copy.deepcopy(grid)
        if testbord[1][1] == "_":
            across = 1
            down = 1
            selected = True
    if selected == False:
        testbord = copy.deepcopy(grid)
        if (testbord[0][0] == "O" and testbord[2][2] == "O") or (testbord[0][2] == "O" and testbord[2][0] == "O"):
            while True:
                number = random.randint(1,5)
                if number == 1:
                    if testbord[0][1] == "_":
                        across = 1
                        down = 0
                        selected = True
                elif number == 2:
                    if testbord[1][0]== "_":
                        across = 0
                        down = 1
                        selected = True
                elif number == 3:
                    if testbord[1][2]== "_":
                        across = 2
                        down = 1
                        selected = True
                elif number == 4:
                    if testbord[2][1]== "_":
                        across = 1
                        down = 2
                        selected = True
                if selected == True:
                    break
                if testbord[0][1] != "_" and testbord[1][0] != "_" and testbord[1][2] != "_" and testbord[2][1] != "_":
                    break

    if selected == False:
        testbord = copy.deepcopy(grid)
        if testbord[0][0] == "_" or testbord[2][0] == "_" or testbord[0][2] == "_" or testbord[2][2] == "_":
            while True:
                number = random.randint(1,5)
                if number == 1:
                    if testbord[0][0] == "_":
                        across = 0
                        down = 0
                        selected = True
                elif number == 2:
                    if testbord[2][0]== "_":
                        across = 0
                        down = 2
                        selected = True
                elif number == 3:
                    if testbord[0][2]== "_":
                        across = 2
                        down = 0
                        selected = True
                elif number == 4:
                    if testbord[2][2]== "_":
                        across = 2
                        down = 2
                        selected = True
                if selected == True:
                    break

    if selected == False:
        if testbord[0][1] == "_" or testbord[1][0] == "_" or testbord[1][2] == "_" or testbord[2][1] == "_":
            while True:
                number = random.randint(1,5)
                if number == 1:
                    if testbord[0][1] == "_":
                        across = 1
                        down = 0
                        selected = True
                elif number == 2:
                    if testbord[1][0]== "_":
                        across = 0
                        down = 1
                        selected = True
                elif number == 3:
                    if testbord[1][2]== "_":
                        across = 2
                        down = 1
                        selected = True
                elif number == 4:
                    if testbord[2][1]== "_":
                        across = 1
                        down = 2
                        selected = True
                if selected == True:
                    break
    if selected == True:

        c.create_line(
            (across * 200) + 20, (down * 200) + 20,
            ((across + 1) * 200) - 20, ((down + 1) * 200) - 20,
            fill="red", width="20"
        )
        c.create_line(
            (across * 200) + 20, ((down + 1) * 200) - 20,
            ((across + 1) * 200) - 20, (down * 200) + 20,
            fill="red", width="20"
        )
        shape = "O"
        grid[down][across] = "X"
def testcheckplayer(testbord):
    pwon = False
    for i in range(0, 3):

        if testbord[i] == ["O", "O", "O"]:
            pwon = True

    for i in range(0, 3):

        coloum = testbord[0][i] + testbord[1][i] + testbord[2][i]
        print(coloum)
        if coloum == "OOO":
            pwon = True

    diagonal1 = testbord[0][0] + testbord[1][1] + testbord[2][2]
    diagonal2 = testbord[2][0] + testbord[1][1] + testbord[0][2]

    if diagonal1 == "OOO" or diagonal2 == "OOO":
        pwon = True



    return pwon
def testcheckai(testbord):
    won = False
    for i in range(0,3):

        if testbord[i] == ["X","X","X"]:
            won = True


    for i in range(0, 3):

        coloum = testbord[0][i] + testbord[1][i] + testbord[2][i]

        if coloum == "XXX":
            won = True

    diagonal1 = testbord[0][0] + testbord[1][1] + testbord[2][2]
    diagonal2 = testbord[2][0] + testbord[1][1] + testbord[0][2]

    if diagonal1 == "XXX" or diagonal2 == "XXX":
        won = True

    return won

def check():

    global win

    lineori = ""

    col = 0

    emptyspace = 0

    for i in range(0,3):

        if grid[i] == ["X","X","X"]:
            win = "X"
            lineori = "v"
            col = i

            return lineori,col
        elif grid[i] == ["O","O","O"]:
            win = "O"
            lineori = "v"
            col = i
            return lineori,col
    for i in range(0, 3):

        coloum = grid[0][i] + grid[1][i] + grid[2][i]

        if coloum == "XXX":
            win = "X"
            lineori = "h"
            col = i
            return lineori,col
        elif coloum == "OOO":
            win = "O"
            lineori = "h"
            col = i
            return lineori, col
    diagonal1 = grid[0][0] + grid[1][1] + grid[2][2]
    diagonal2 = grid[2][0] + grid[1][1] + grid[0][2]

    if diagonal1 == "XXX":
        win = "X"
        lineori = "d"
        col = 1
        return lineori, col
    elif diagonal2 == "XXX":
        win = "X"
        lineori = "d"
        col = 2
        return lineori, col
    elif diagonal1 == "OOO":
        win = "O"
        lineori = "d"
        col = 1
        return lineori, col
    elif diagonal2 == "OOO":
        win = "O"
        lineori = "d"
        col = 2
        return lineori, col
    if win == "None":
        for a in range(0,3):
            for b in range(0,3):
                if grid[a][b] == "_":
                    emptyspace =+ 1
        if emptyspace == 0:
            win = "draw"
    return lineori,col

def GameWon():

    c.delete("all")
    if win == "X":
        c.configure(bg = "red")
        c.create_text(300, 300, fill="white", font=("Lucida Console", 30),
                      text="Crosses won the game!")
    elif win == "O":
        c.configure(bg="yellow")
        c.create_text(300, 300, fill="black", font=("Lucida Console", 30),
                      text="Naughts won the game!")
    else:
        c.configure(bg="green")
        c.create_text(300, 300, fill="white", font=("Lucida Console", 30),
                      text="Its a Draw!")
    c.create_text(300, 400, fill="black", font=("Lucida Console", 20),
                      text="[Press enter to play again]")
main = Tk()

c = Canvas(main, width=600, height = 600, bg = "light blue")
c.pack()

c.create_text(300,300,fill="white",font=("Lucida Console", 30),
                        text="[Press enter to begin]")
main.bind("<Return>", begin)


mainloop()