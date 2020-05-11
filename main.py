from tkinter import *
from tkinter import messagebox

global numClick
numClick = 0
grid = [[0,0,0],[0,0,0],[0,0,0]]



playScreen = Tk()
playScreen.geometry("450x450")
playScreen.title("Tic Tac Toe")
def createX(xLoc,yLoc):
    scale_factor = 30
    canvas.create_rectangle(xLoc * 140, yLoc * 140, xLoc * 140 + 140, yLoc * 140 + 140,
                            fill="#957DAD", outline="black", width=3, tag=f"123")
    canvas.create_line((xLoc*140)+scale_factor,(yLoc*140)+scale_factor,
                       (xLoc*140+140)-scale_factor,(yLoc*140+140)-scale_factor,fill="red", width= 5)
    canvas.create_line((xLoc * 140)+scale_factor, (yLoc * 140+140)-scale_factor,
                       (xLoc * 140 + 140) - scale_factor, (yLoc * 140) + scale_factor ,
                       fill="red", width=5)


def createO(xLoc,yLoc):
    scale_factor = 30
    canvas.create_rectangle(xLoc * 140, yLoc * 140, xLoc * 140 + 140, yLoc * 140 + 140,
                            fill="#957DAD", outline="black", width=3,tag=f"123")
    canvas.create_oval(xLoc*140 + scale_factor,yLoc*140 + scale_factor,
                       xLoc*140+140 - scale_factor,yLoc*140+ 140 - scale_factor,
                       fill="#957DAD", outline="#FFDFD3", width=5 )




def checkWinner():
    global Owin
    global Xwin
    global tie
    Owin = False
    Xwin = False
    tie = False
    for index in range(3):
        if grid[index][0] == 1 and grid[index][1] == 1 and grid[index][2] == 1:
            Xwin=True
            break

        if grid[index][0] == 2 and grid[index][1] == 2 and grid[index][2] == 2:
            Owin=True
            break
    for index in range(3):
        if grid[0][index] == 1 and grid[1][index] == 1 and grid[2][index] == 1:
            Xwin = True

        if grid[0][index] == 2 and grid[1][index] == 2 and grid[2][index] == 2:
            Owin = True


    if grid[0][0] == 2 and grid[1][1] == 2 and grid[2][2] == 2:
        Owin = True
    if grid[0][0] == 1 and grid[1][1] == 1 and grid[2][2] == 1:
        Xwin = True
    if grid[2][0] == 2 and grid[1][1] == 2 and grid[0][2] == 2:
        Owin = True
    if grid[2][0] == 1 and grid[1][1] == 1 and grid[0][2] == 1:
        Xwin = True

    options = ""
    for row in grid:
        for item in row:
            options += str(item)
    if "0" not in options and not (Xwin or Owin):
        tie = True

canvas = Canvas(playScreen,bg="blue",height=420,width=420)
canvas.pack()

def passa(event):
    pass
def buttonClick(event):
    global Owin
    global Xwin
    global tie
    id = event.widget.find_closest(event.x, event.y)
    coords = event.widget.gettags(id)[0]
    xLoc = int(coords[0])
    yLoc = int(coords[2])
    global numClick
    numClick += 1
    if numClick % 2 == 0:
        createO(xLoc, yLoc)
        grid[xLoc][yLoc] = 2
    else:
        createX(xLoc,yLoc)
        grid[xLoc][yLoc] = 1
    checkWinner()
    if Owin:
        messagebox.showinfo("O ganhou", message="O ganhou")
        playScreen.destroy()
    elif Xwin:
        messagebox.showinfo("X ganhou", message="X ganhou")
        playScreen.destroy()
    elif tie:
        messagebox.showinfo("O jogo empatou",message="O jogo empatou")
        playScreen.destroy()

    
        






for row in range(3):
    for column in range(3):
        canvas.create_rectangle(row*140,column*140,row*140 + 140,column*140 + 140,
                                fill="#957DAD",outline="black",tag=f"{row},{column}", width=3)
        canvas.tag_bind(f"{row},{column}",'<ButtonPress-1>', buttonClick)


playScreen.mainloop()






