import random
import Combat
Mplayinput=""


def Mplayerinput(text="", cap=False,strip=True):
   global Mplayinput
   Mplayinput = input(text)
   if cap == False:
       Mplayinput = Mplayinput.lower()
   if strip== True:
      Mplayinput.strip()
   return (Mplayinput)

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
        self.staird=False
        self.murder=False
    def get_murder(self):
        return self.murder
    def murdering(self, status=True):
        self.murder=status
    def stairify(self, status=True):
            self.staird=status
    def get_stair(self):
        return self.staird
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
        if self.staird:
            disp= "\033[1;33m┌───┐\033[0m"
            if self.nw == False:
               disp = "\033[1;33m┌   ┐\033[0m"
        else:
            disp = "┌───┐"
            if self.nw == False:
                disp = "┌   ┐"
        return disp

    def print_cell_mid(self):
        if self.cp:
            disp = "| \033[1;31m@\033[0m |"
            if self.ew == False and self.ww == False:
                disp = "  \033[1;31m@\033[0m  "
            elif self.ew == False:
                disp = "| \033[1;31m@\033[0m  "
            elif self.ww == False:
                disp = "  \033[1;31m@\033[0m |"
        elif self.staird:
            disp = "\033[1;33m|   |\033[0m"
            if self.ew == False and self.ww == False:
                disp = "     "
            elif self.ew == False:
                disp = "\033[1;33m|    \033[0m"
            elif self.ww == False:
                disp = "\033[1;33m    |\033[0m"
        else:
            disp = "|   |"
            if self.ew == False and self.ww == False:
                disp = "     "
            elif self.ew == False:
                disp = "|    "
            elif self.ww == False:
                disp = "    |"
        return disp

    def print_cell_bot(self):
        if self.staird:
            disp = "\033[1;33m└───┘\033[0m"
            if self.sw == False:
                disp = "\033[1;33m└   ┘\033[0m"
        else:
            disp = "└───┘"
            if self.sw == False:
                disp = "└   ┘"
        return disp

    def vist(self,state=True):
        self.visted = state

    def add_connection(self, direct):
        self.connections.append(direct)

    def get_connections(self, specified="none"):
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
    def dispConnections(self):
        string=""
        if "nw" in self.connections:
            string+="North "
        if "sw" in self.connections:
            string+="South "
        if "ew" in self.connections:
            string+="East "
        if "ww" in self.connections:
            string+="West "
        return string


class Maze:
    def __init__(self, row=10, column=10, level=1, intialize=True):
        self.maze = []
        self.row = row
        self.column = column
        self.level=level
        if intialize:
            self.set_maze()
            self.dfs()

    def set_maze(self):
        self.maze = []
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

        x, y = random.randrange(0, self.column - 1, 2), random.randrange(0, self.row-1, 2)
        print(y)
        print(self.row)
        print(self.maze[y])
        self.maze[y][x].stairify()
        x, y = random.randrange(0, self.column-1, 2), random.randrange(0, self.row-1, 2)
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
                murder=random.randint(1,10)
                self.maze[ny][nx].vist()
                self.maze[y][x].break_wall(direct)
                self.maze[ny][nx].break_wall(idirect)
                if murder==5:
                    self.maze[ny][nx].murdering(True)
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
                    return row, col
    def move(self, check=False):
        #first get player cell
        y,x =self.find_p()
        levelstr=str(self.level)
        print("Maze Depth "+levelstr)
        #combat
        if self.maze[y][x].get_murder():
            Combat.spawnEnemies(1,self.level)
            print("You've been attacked do do do doo")
            Combat.combat()
            self.maze[y][x].murdering(False)
            self.print_maze()
        #run goal code
        if self.maze[y][x].get_stair():
            self.level += 1
            
            if check:
                self.set_maze()
                self.dfs()
                self.print_maze()
            else:
                return True, self.level
        #second get input for movement
        movedir=Mplayerinput("Where do you want to go Avalible directions:"+self.maze[y][x].dispConnections()+"\n")
        if movedir=="s" or movedir=="down" or movedir=="south":
            if y + 1 > self.row-1 or self.maze[y][x].get_connections("sw")==False:
                print("Can't go there")
            else:
                self.maze[y + 1][x].set_p()
                self.maze[y][x].set_p(False)
        elif movedir=="w" or movedir=="up" or movedir=="north":
            if y - 1 < 0 or self.maze[y][x].get_connections("nw")==False:
                print("Can't go there")
            else:
                self.maze[y - 1][x].set_p()
                self.maze[y][x].set_p(False)
        elif movedir=="a" or movedir=="left" or movedir=="west":
            if x - 1 < 0 or self.maze[y][x].get_connections("ww")==False:
                print("Can't go there")
            else:
                self.maze[y][x - 1].set_p()
                self.maze[y][x].set_p(False)
        elif movedir=="d" or movedir=="right" or movedir=="east":
            if x + 1 > self.column - 1 or self.maze[y][x].get_connections("ew")==False:
                print("Can't go there")
            else:
                self.maze[y][x + 1].set_p()
                self.maze[y][x].set_p(False)
        else:
            print("not a command")
        return False,False

    def change_cell(self,x,y):
        self.maze[x][y].set_p()


ms = Maze(2, 12)
ms.print_maze()
r = ms.get_maze()
while Mplayinput!="quit":
    c,l=ms.move()
    if c:
        r=ms.get_rows()
        r+=1
        co=ms.get_column()
        co+=1
        ms=Maze(r,co,l)
        ms.print_maze()
    else:
        ms.print_maze()

for row in range(len(r)):
    for column in range(len(r[row])):
        cv = r[row][column]
        print(cv.get_connections())
#
# # m1=Maze()
# # m2=Maze()
# # runing=True
# # while runing==True:
# #     a=input("type")
# #     if a=="1":
# #         m1.print_maze()
# #     if a=="2":
# #         m2.print_maze()
# #     if a=="3":
# #         runing=False
