RESOLUTIONX= 1125
RESOLUTIONY= 625
NUM_COLS = 45
NUM_ROWS = 25
Length = RESOLUTIONX//NUM_ROWS
Width = RESOLUTIONY//NUM_COLS


class Grid:
    def __init__(self, r, c):
        self.r = r
        self.c = c
    
    def show(self):
        fill(0)
        noStroke()
        rect(self.c * RESOLUTIONX/NUM_COLS, self.r * RESOLUTIONY/NUM_ROWS, RESOLUTIONX/NUM_COLS, RESOLUTIONY/NUM_ROWS)
        
    
class Grids(list):
    def __init__(self):
        self.board = []
        for r in range(NUM_ROWS):
            for c in range(NUM_COLS):
                self.append(Grid(r, c))


    def show_grids(self):
        for grid in self:
            grid.show()
            
            
    def load_csv(self):
        with open("file.csv", "r") as filename:
            for file in filename:
                file = file.strip().split(",")
                self.board.append(file)
    
                
                
                
    def show_maze(self): # Displaying the white rectangles
        for r in range(NUM_ROWS):
            for c in range(NUM_COLS):
                if self.board[r][c] == "1":
                    fill(0,0,0)
                    strokeWeight(3)
                    rect(c*RESOLUTIONX//NUM_COLS, r*RESOLUTIONY//NUM_ROWS, RESOLUTIONX//NUM_COLS,RESOLUTIONY//NUM_ROWS)
    def show_maze2(self): #Displaying the black rectangles
        for r in range(NUM_ROWS):
            for c in range(NUM_COLS):
                if self.board[r][c] == "0":
                    fill(255)
                    strokeWeight(3)
                    rect(c*RESOLUTIONX//NUM_COLS, r*RESOLUTIONY//NUM_ROWS, RESOLUTIONX//NUM_COLS,RESOLUTIONY//NUM_ROWS)
    def elements(self): #Displaying the black rectangles
        for r in range(NUM_ROWS):
            for c in range(NUM_COLS):
                if self.board[r][c] == "0" or self.board[r][c] == "p" or self.board[r][c] == "d" or self.board[r][c] == "2" or self.board[r][c] == "c":
                    fill(255)
                    strokeWeight(3)
                    rect(c*RESOLUTIONX//NUM_COLS, r*RESOLUTIONY//NUM_ROWS, RESOLUTIONX//NUM_COLS,RESOLUTIONY//NUM_ROWS)
                    
                    
                    
    def show_checkpoint(self):
        for r in range(NUM_ROWS):
            for c in range(NUM_COLS):
                if self.board[r][c] == "d":
                    fill(255, 255, 51)
                    strokeWeight(3)
                    circle(c*RESOLUTIONX//NUM_ROWS, r*RESOLUTIONY//NUM_COLS, Length/2)
    
            
    def show_player(self):
        for r in range(NUM_ROWS):
            for c in range(NUM_COLS):
                if self.board[r][c] == "p":
                    fill(0, 128, 255)
                    strokeWeight(3)
                    circle(c*Width+Length//2, r*Length, Length/2)
    
        
                    
    def show_candy(self):
        for r in range(NUM_ROWS):
            for c in range(NUM_COLS):
                if self.board[r][c] == "c":
                    fill(255, 255, 51)
                    strokeWeight(3)
                    circle(c*RESOLUTIONY//NUM_COLS, r*RESOLUTIONX//NUM_ROWS, Length+6)
        


class Angle:
    def __init__(self):
        self.angle = 0
        
        
g = Grids()       
a = Angle()

def setup():
    size(1125,625)
    g.load_csv()
    

    
def draw():
    g.show_maze()
    g.show_maze2()
    g.elements()
    g.show_player()
    g.show_candy()
    g.show_checkpoint()
    # # background(255)
    # translate(400, 400)
    # rotate(a.angle)
    # fill(0, 140, 0)
    # stroke(50)
    # g.show_grids()
    # line(0, 0, 500, 500)
    # circle(0,0,40)
    # line(500, 500, 500, 500)
    # a.angle += 0.01
    
    
    
    
    
# class Board:
#     #Initializing
#   def show_maze(self):
#       pass
# class Player:
#     pass

# class Checkpoint:
#     pass
# class CandyTarget:
#     pass
    
# class GameFunctionalities:
#     #Initializing
    
#     def setting(self):
#         pass
#     def timer(self):
#         pass
#     def instructions(self):
#         pass
#     def help(self):
#         pass
#     def reset(self):

    
    
    
    
    
