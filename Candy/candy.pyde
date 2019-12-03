RESOLUTIONX= 1125
RESOLUTIONY= 625
NUM_COLS = 45
NUM_ROWS = 25
Length = RESOLUTIONX//NUM_COLS
Width = RESOLUTIONY//NUM_ROWS


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
        self.angle = 0
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
    def elements(self): #Displaying the white rectangles
        for r in range(NUM_ROWS):
            for c in range(NUM_COLS):
                if self.board[r][c] == "0" or self.board[r][c] == "p" or self.board[r][c] == "d" or self.board[r][c] == "2" or self.board[r][c] == "c":
                    fill(255)
                    strokeWeight(3)
                    rect(c*RESOLUTIONX//NUM_COLS, r*RESOLUTIONY//NUM_ROWS, RESOLUTIONX//NUM_COLS,RESOLUTIONY//NUM_ROWS)
                    
    def opponent(self):
        for r in range(NUM_ROWS):
            for c in range(NUM_COLS):
                if self.board[r][c] == "p" or self.board[r][c] == "c":
                    translate(c*Width+12.99, r*Length+12.99)
                    rotate(self.angle)
                    fill(0, 140, 0)
                    stroke(0)
                    line(0, 0, c*1000, r*1000)
                    circle(0,0,25)
                    self.angle += 0.001
        
     
                    
                                   
                                                                 
                    
                    
    def show_checkpoint(self):
        for r in range(NUM_ROWS):
            for c in range(NUM_COLS):
                if self.board[r][c] == "d":
                    fill(255, 255, 51)
                    strokeWeight(3)
                    circle(c*Width+12.99, r*Length+12.99, 25)
                    #circle(c*RESOLUTIONX//NUM_COLS+Length//2, r*RESOLUTIONY//NUM_COLS+Width//2, Length)
                    
    
                    
    # def rotation(self):
    #     for r in range(NUM_ROWS):
    #         for c in range(NUM_COLS):
    #             if self.board[r][c] == "d":
    #                 fill(255, 255, 51)
    #                 strokeWeight(3)
    #                 circle(c*Width+25, r*Length-7.5, Length//2)
    #                 background(255)
    #                 translate(400, 400)
    #                 rotate(a.angle)
    #                 fill(0, 140, 0)
    #                 stroke(50)
    #                 g.show_grids()
    #                 line(0, 0, 500, 500)
    #                 circle(0,0,40)
    #                 line(500, 500, 500, 500)
    #                 a.angle += 0.01
        
    
    

            
    def show_player(self):
        for r in range(NUM_ROWS):
            for c in range(NUM_COLS):
                if self.board[r][c] == "p":
                    fill(0, 128, 255)
                    strokeWeight(1)
                    circle(c*Width+12.99, r*Length+12.99, 25)
                    
    
    
        
                    
    def show_candy(self):
        for r in range(NUM_ROWS):
            for c in range(NUM_COLS):
                if self.board[r][c] == "c":
                    fill(255, 0,0)
                    strokeWeight(1)
                    circle(c*Width+12.99, r*Length+12.99, 25)
        


# class Angle:
#     def __init__(self):
#         self.angle = 0
        
class GameFunctionalities:
    def __init__(self):
        self.c = 0
    
    def setting(self):
        textSize(50)
        text("Settings", 1175, 700)
    def timer(self):
        pass
    def instructions(self):
        pass
    def help(self):
        pass
    def reset(self):
        pass    
g = Grids()
gf = GameFunctionalities()       
# a = Angle()

def setup():
    size(1200,800)
    g.load_csv()
    

    
def draw():
    g.show_maze()
    g.show_maze2()
    g.elements()
    g.show_player()
    g.show_candy()
    g.show_checkpoint()
    g.opponent()
    gf.setting()
    # g.rotation()
    # background(255)
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
    


    
    
    
    
    
