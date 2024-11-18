import random

def playerinput(text="", cap=False,strip=True):
   global playinput
   playinput = input(text)
   if cap == False:
       playinput = playinput.lower()
   if strip== True:
      playinput.strip()
   return (playinput)

class Cell:
    def __init__(self):
        self.nw = True
        self.sw = True
        self.ew = True
        self.ww = True
        self.visted = False
        self.descr = ""
        self.connections = []
        self.cp=False
        self.make_descr()


    def make_descr(self, rtype="none"):
        types = ["treasure", "empty", "fight", "tables"]
        if rtype == "none":
            ctype = random.choice(types)
        else:
            ctype = rtype
        if ctype == "treasure":
            self.descr = "treasure"
        elif ctype == "empty":
            self.descr = "empty"
        elif ctype == "fight":
            self.descr = "fight"
        elif ctype == "tables":
            self.descr = "tables"

    def get_descr(self):
        return self.descr

    def break_wall(self, wall):
        if wall == "nw":
            self.nw = False
        if wall == "sw":
            self.sw = False
        if wall == "ew":
            self.ew = False
        if wall == "ww":
            self.ww = False
        self.vist()
        self.add_connection(wall)

    def was_visted(self):
        if self.visted:
            return True
        else:
            return False

    def print_cell_top(self):
        disp = "┌──┐"
        if self.nw == False:
            disp = "┌  ┐"
        return disp

    def print_cell_mid(self):
        if self.cp:
            disp = "|◖◗|"
            if self.ew == False and self.ww == False:
                disp = " ◖◗ "
            elif self.ew == False:
                disp = "|◖◗ "
            elif self.ww == False:
                disp = " ◖◗|"
        else:
            disp = "|  |"
            if self.ew == False and self.ww == False:
                disp = "    "
            elif self.ew == False:
                disp = "|   "
            elif self.ww == False:
                disp = "   |"
        return disp

    def print_cell_bot(self):
        disp = "└──┘"
        if self.sw == False:
            disp = "└  ┘"
        return disp

    def vist(self,state=True):
        self.visted = state

    def add_connection(self, direct):
        self.connections.append(direct)

    def get_conections(self, specified="none"):
        if specified == "none":
            return self.connections
        else:
            if specified in self.connections:
                return True
            else:
                return False
    def set_p(self, state=True):
        self.cp=state
    def get_p(self):
        if self.cp:
            return True
        else:
            return False


class Maze:
    def __init__(self, row=10, column=10, intialize=True):
        self.maze = []
        self.row = row
        self.column = column
        if intialize:
            self.set_maze()
            self.dfs()

    def set_maze(self):
        for row in range(self.row):
            xrow = []
            for column in range(self.column):
                c = Cell()
                xrow.append(c)
            self.maze.append(xrow)

    def dfs(self):
        def get_unvisited_neighbors(x, y):
            neighbors = []
            if x + 1 <= self.column - 1 and self.maze[y][x + 1].was_visted() == False:
                neighbors.append((x + 1, y))
            if x - 1 >= 0 and self.maze[y][x - 1].was_visted() == False:
                neighbors.append((x - 1, y))
            if y + 1 <= self.row - 1 and self.maze[y + 1][x].was_visted() == False:
                neighbors.append((x, y + 1))
            if y - 1 >= 0 and self.maze[y - 1][x].was_visted() == False:
                neighbors.append((x, y - 1))
            return neighbors

        x, y = random.randrange(1, self.column-1, 2), random.randrange(1, self.row, 2)
        self.maze[y][x].vist()
        self.maze[y][x].set_p()
        stack = [(x, y)]

        # DFS algorithm
        while stack:
            x, y = stack[-1]
            neighbors = get_unvisited_neighbors(x, y)
            if neighbors:
                nx, ny = random.choice(neighbors)
                if ny > y:
                    direct = "sw"
                    idirect = "nw"
                elif ny < y:
                    direct = "nw"
                    idirect = "sw"
                elif nx > x:
                    direct = "ew"
                    idirect = "ww"
                elif nx < x:
                    direct = "ww"
                    idirect = "ew"
                self.maze[ny][nx].vist()
                self.maze[y][x].break_wall(direct)
                self.maze[ny][nx].break_wall(idirect)
                stack.append((nx, ny))
            else:
                stack.pop()

    def print_maze(self):
        pmaze = []
        for row in range(len(self.maze)):
            crow = []
            trow = []
            mrow = []
            brow = []
            for col in range(len(self.maze[row])):
                cell = self.maze[row][col]
                trow.append(cell.print_cell_top())
                mrow.append(cell.print_cell_mid())
                brow.append(cell.print_cell_bot())
            crow.append(trow)
            crow.append(mrow)
            crow.append(brow)
            pmaze.append(crow)

        for a in range(len(pmaze)):
            # crow is getting looped now
            for b in range(len(pmaze[a])):
                bigstring = ""
                # crow's top row, mid row, and bottom row
                for c in range(len(pmaze[a][b])):
                    bigstring += pmaze[a][b][c]
                print(bigstring)

    def get_cell(self, x, y):
        return self.maze[y][x]

    def get_maze(self):
        return self.maze

    def get_rows(self):
        return self.row

    def get_column(self):
        return self.column
    def find_p(self):
        for row in range(len(self.maze)):
            for col in range(len(self.maze[row])):
                if self.maze[row][col].get_p():
                    return row,col
    def move(self):
        #first get player cell
        y,x=self.find_p()
        #second get input for movement
        movedir=playerinput()
        self.maze[y][x].set_p(False)
        if movedir=="s" or movedir=="down":
            if y + 1 > self.column-1:
                print("Can't go there")
            else:
                self.maze[y + 1][x].set_p()
        elif movedir=="w" or movedir=="up":
            if y - 1 < 0:
                print("Can't go there")
            else:
                self.maze[y - 1][x].set_p()
        elif movedir=="w" or movedir=="left":
            if x - 1 < 0:
                print("Can't go there")
            else:
                self.maze[y][x - 1].set_p()
        elif movedir=="d" or movedir=="right":
            if x + 1 > self.row - 1:
                print("Can't go there")
            else:
                self.maze[y][x + 1].set_p()
    def change_cell(self,x,y):
        self.maze[x][y].set_p()


ms = Maze(3, 3)
ms.print_maze()
ms.move()
ms.print_maze()
print(ms.find_p())
r = ms.get_maze()
for row in range(len(r)):
    for column in range(len(r[row])):
        cv = r[row][column]
        print(cv.get_conections())

# m1=Maze()
# m2=Maze()
# runing=True
# while runing==True:
#     a=input("type")
#     if a=="1":
#         m1.print_maze()
#     if a=="2":
#         m2.print_maze()
#     if a=="3":
#         runing=False
