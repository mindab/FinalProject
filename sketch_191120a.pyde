RESOLUTIONX= 1000
RESOLUTIONY= 800

NUM_COLS = 45
NUM_ROWS = 25


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
        with open("csv_file.csv", "r") as filename:
            for file in filename:
                file = file.strip().split(",")
                self.board.append(file)
    def show_maze(self):
        for r in range(NUM_ROWS):
            for c in range(NUM_COLS):
                if self.board[r][c] == "1":
                    fill(0,0,0)
                    strokeWeight(5)
                    rect(c*RESOLUTIONX//NUM_COLS, r*RESOLUTIONY//NUM_ROWS, RESOLUTIONX//NUM_COLS,RESOLUTIONY//NUM_ROWS)
    def show_maze2(self):
        for r in range(NUM_ROWS):
            for c in range(NUM_COLS):
                if self.board[r][c] == "0":
                    fill(255)
                    strokeWeight(5)
                    rect(c*RESOLUTIONX//NUM_COLS, r*RESOLUTIONY//NUM_ROWS, RESOLUTIONX//NUM_COLS,RESOLUTIONY//NUM_ROWS)


class Angle:
    def __init__(self):
        self.angle = 0
        
        
g = Grids()       
a = Angle()

def setup():
    size(1600,1600)
    
    g.load_csv()
    

    
def draw():
    g.show_maze()
    g.show_maze2()
    # background(255)
    # translate(400, 400)
    # rotate(a.angle)
    # fill(0, 140, 0)
    # stroke(50)
    # g.show_grids()
    # line(0, 0, 500, 500)
    # circle(0,0,40)
    # line(100, 100, 500, 500)
    # a.angle += 0.01
    
