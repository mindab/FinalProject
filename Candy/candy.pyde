add_library('sound')
# add_library('minim')
import random




RESOLUTIONX= 1125
RESOLUTIONY= 625
NUM_COLS = 45
NUM_ROWS = 25
Length = RESOLUTIONX//NUM_COLS
Width = RESOLUTIONY//NUM_ROWS
CIRCUM = 20
board = []
GAME_TIME_ALLOWED = 50 #seconds
FINAL_TIME = 0





with open("./file.csv", "r") as filename:
    for file in filename:
        file = file.strip().split(",")
        board.append(file)
        board[0][0] = "0"



                
                
class Grids:
    def __init__(self):
        self.angle=0            
    def show_maze(self): # Displaying the white cells
        for r in range(NUM_ROWS):
            for c in range(NUM_COLS):
                if board[r][c] == "1":
                    fill(0,0,0)
                    stroke(0)
                    strokeWeight(3)
                    rect(c*RESOLUTIONX//NUM_COLS, r*RESOLUTIONY//NUM_ROWS, RESOLUTIONX//NUM_COLS,RESOLUTIONY//NUM_ROWS)
    def show_maze2(self): #Displaying the black cells
        for r in range(NUM_ROWS):
            for c in range(NUM_COLS):
                if board[r][c] == "0":
                    fill(255)
                    stroke(0)
                    strokeWeight(3)
                    rect(c*RESOLUTIONX//NUM_COLS, r*RESOLUTIONY//NUM_ROWS, RESOLUTIONX//NUM_COLS,RESOLUTIONY//NUM_ROWS)
    def elements(self): 
        for r in range(NUM_ROWS):
            for c in range(NUM_COLS):
                if board[r][c] == "0" or board[r][c] == "p" or board[r][c] == "d" or board[r][c] == "2" or board[r][c] == "c":
                    fill(255)
                    noStroke()
                    rect(c*RESOLUTIONX//NUM_COLS, r*RESOLUTIONY//NUM_ROWS, RESOLUTIONX//NUM_COLS,RESOLUTIONY//NUM_ROWS)
                    
    def show_candy(self):
        for r in range(NUM_ROWS):
            for c in range(NUM_COLS):
                if board[r][c] == "c":
                    fill(255, 0, 21)
                    noStroke()
                    circle(c*Length + Length//2, r*Width + Width//2, 25)
        
                    

                          
   
                    
    def show_checkpoint(self):
        for r in range(NUM_ROWS):
            for c in range(NUM_COLS):
                if board[r][c] == "d":
                    fill(249, 166, 2)
                    stroke(249, 166, 2)
                    beginShape()
                    vertex(c*Length + Length//2, r*Width)
                    vertex(c*Length, r*Width + Width//2)
                    vertex(c*Length + Length, r*Width + Width//2)
                    vertex(c*Length + Length//2, r*Width + Width)
                    endShape()





class Body:
    def __init__(self, r, c, xspeed, yspeed, frames):
        
        self.r=r
        self.c=c
        self.angle = 0
        self.xspeed= xspeed
        self.yspeed= yspeed
        self.key_handler = {LEFT:False, RIGHT:False, UP:False, DOWN:False}
        self.start=False
        self.reset=False
        self.slice=0
        self.frames=frames
        self.black_cells=[]
        self.lasers=[]
        self.diamonds=[]
        self.candy_position = []
        self.laser_position = []
        self.sound = False
        self.Rotation_timer = 3
        self.timer=Timer()
        
        
    def show_body(self):
        
        fill(0, 128, 255)
        noStroke()
        circle((self.c*Length) + Length//2, (self.r*Width) + Width//2, CIRCUM)
    def show_candy(self):
        for r in range(NUM_ROWS):
            for c in range(NUM_COLS):
                if board[r][c] == "c":
                    self.candy_position.append([r, c])
                    fill(255, 0, 21)
                    noStroke()
                    circle(c*Length + Length//2, r*Width + Width//2, 25)
    def show_opponent(self):
        for r in range(NUM_ROWS):
            for c in range(NUM_COLS):
                if board[r][c] == "2":
                    fill(0,140,0)
                    noStroke()
                    circle(c*Length+Length/2, r*Width+Width/2,CIRCUM)
    def move(self): # Controls the movement of the player
        for i in range(NUM_ROWS):
            for j in range(NUM_COLS):
                if board[i][j]=="1":
                    self.black_cells.append([i,j])
                elif board[i][j]=="2":
                    self.lasers.append([i,j])
                elif board[i][j]=="d":
                    self.diamonds.append([i,j])
    
        
        if self.key_handler[LEFT] == True and [self.r, self.c-1] not in self.black_cells and [self.r, self.c-1]  not in self.lasers and [self.r, self.c-1]not in self.diamonds and (self.c-1)*Length>=0:
            self.xspeed = -1
            self.yspeed= 0
            self.direction = LEFT
            self.r += self.yspeed
            self.c += self.xspeed
        elif self.key_handler[RIGHT] == True and [self.r, self.c+1] not in self.black_cells and [self.r, self.c+1] not in self.lasers and[self.r, self.c+1] not in self.diamonds and (self.c+1)*Length<1125:
            self.xspeed = 1
            self.yspeed= 0
            self.direction = RIGHT
            self.r += self.yspeed
            self.c += self.xspeed
        elif self.key_handler[UP]==True and [self.r-1, self.c] not in self.black_cells and [self.r-1, self.c] not in self.lasers and [self.r-1, self.c] not in self.diamonds and (self.r-1)*Length>-25:
            self.yspeed = -1
            self.xspeed =0
            self.r += self.yspeed
            self.c += self.xspeed
        elif self.key_handler[DOWN]==True and [self.r+1, self.c] not in self.black_cells and not [self.r+1, self.c] in self.lasers and [self.r+1, self.c] not in self.diamonds and (self.r+1)*Length<625:
            self.yspeed=1
            self.xspeed=0
            
            self.r += self.yspeed
            self.c += self.xspeed
        if frameCount % 10 == 0 and self.xspeed != 0 and self.yspeed == 0:
            self.slice = (self.slice + 1) % self.frames            


     # Checks if player have found the candy   
    def collision(self):
        global FINAL_TIME
        if self.r ==21 and self.c ==4:
            self.start = False
            background(0)
            fill(255, 255, 255)
            textSize(30)
            text("Congratulations! You won",  500, 300)
            fill(255, 255, 255)
            textSize(30)
            text("Time taken:",  600, 350)
            fill(255, 255, 255)
            textSize(30)
            text(str(int(FINAL_TIME)) + " seconds",  800, 350)
            fill(255, 255, 255)
            textSize(30)
            text('Click reset then click start to play again',  500, 400)
                
                
    # Shows and rotates the laser: Basically causing a slowdown in the game
    def Rotate(self):
        for r in range(NUM_ROWS):
            for c in range(NUM_COLS):
                if board[r][c] == "2":
                    fill(0,140,0)
                    noStroke()
                    circle(c*Length+Length/2, r*Width+Width/2,CIRCUM)
        
                    self.angle += 0.001
                    
                    ori_x = c*Length + Length/2
                    ori_y = r*Width + Width/2
                    
                    current_r, current_c = r*Width, c*Length       
                    laser_length = 0
                    while True:
                        laser_length += 1
                        x = (c*Length) + (laser_length * cos(self.angle+(c/6)))
                        y = (r*Width) + (laser_length * sin(self.angle+(c/6)))
                        
                        current_c = int(x/Length)
                        current_r = int(y/Width)
                        self.laser_position.append([current_r, current_c])
                    
                        
                        
                        if current_r < 0 or current_c < 0 or current_r >= NUM_ROWS or current_c >= NUM_COLS:
                            break
                        if board[current_r][current_c] == "1" or board[current_r][current_c] == "d":
                            break
                        
                    
                        # The conditions below are detecting collision b/n the player and the lasers
                        if current_r == self.r and current_c == self.c and self.r < 12 and self.c < 18 and self.r !=2 and self.c !=2:
                            self.r = 10
                            self.c = 9
                        elif current_r == self.r and current_c == self.c and self.r < 12 and 18<= self.c < 32:
                            self.r = 7
                            self.c = 23
                        elif current_r == self.r and current_c == self.c and self.r < 12 and self.c > 32:
                            self.r = 8
                            self.c = 41
                        elif current_r == self.r and current_c == self.c and self.r > 12 and self.c < 18:
                            self.r = 22
                            self.c = 12
                        elif current_r == self.r and current_c == self.c and self.r > 12 and 18 <= self.c < 32:
                            self.r = 13
                            self.c = 31
                        elif current_r == self.r and current_c == self.c and self.r > 12 and self.c > 32:
                            self.r = 20
                            self.c = 41
                    stroke(0,140,0)
                    strokeWeight(5)
                    line(ori_x, ori_y, x, y)
                            
                            
                    
           
        
                             
                        
                   
                    
    
         
                    
                               
class Timer:
    def __init__(self):
        self.time = GAME_TIME_ALLOWED
        self.total_time_taken = 0
        
    def countDown(self):
        global FINAL_TIME

        
        
        background(255)
        fill(255)
        stroke(0, 140, 0)
        strokeWeight(3)
        fill(255)
        stroke(0, 140, 0)
        rect(1250, 40, 100, 40)
        fill(0)
        text(":", 1303, 70)
        if game.b.start == False:
            fill(0)
            text(":", 1303, 70)
            text("00", 1267, 70)
            text("00", 1310, 70)
                
                
                #Incrementing time
        # while True
        
        if game.b.start == True:
            self.total_time_taken += 1/frameRate
            self.time -= 1/frameRate
            FINAL_TIME = self.total_time_taken
        
        
            
        self.t = [self.time, ":", int(self.time/60)] # keeping it in a list in the form (minutes:secondes)
        
        
        #Dealing with seconds
        if game.b.start == True and self.t[0] <= 60:
            fill(0)
            text(int(self.t[0]), 1320, 70)
            
        if self.time < 10 and game.b.start == True:
            fill(0)
            text("0", 1308, 70)
    
    
        #Dealing with minutes
        
        if self.time > 60:
            fill(0)
            text(self.t[2], 1280, 70)
            text(int(self.t[0] % 60),  1320, 70)
            
        if self.time < 60 and game.b.start == True:
            fill(0)
            text("0", 1290, 70)
            text("0", 1275, 70)
            
        if self.time > 60 and int(self.time/60) < 10 and game.b.start == True:
            fill(0)
            text("0", 1265, 70)
            
    
        if game.b.reset == True:
            self.time = GAME_TIME_ALLOWED 
            
    
            
                
                    
class GameFunctionalities:
    #Initializing
    def __init__(self):
        self.over_box=False
        self.over_box2=False
        
    def setting(self):
        pass
    def timer(self):
        pass
    # Displays the instruction
    def instructions(self):
        stroke(0, 140, 0)
        fill(255,255, 255)
        strokeWeight(3)
        rect(1140, 310, 220, 150)
        fill(0, 0, 0)
        textSize(15)
        s=s="Reach the candy while avoiding opponents and lasers! Use arrow keys to move the player."
        text(s, 1150,320, 200, 100)
       
   # Displays the start button
    def start_button(self):
        fill(255,255, 255)
        stroke(0, 140, 0)
        strokeWeight(3)
        rect(1140, 150, 200, 40)
        fill(0, 0, 0)
        textSize(25)
        text('START', 1150, 160, 200, 50)
        
        if mouseX>1140 and mouseX<1340 and mouseY>160 and mouseY<210:
            self.over_box=True
        else:
            self.over_box=False
        
    #Displays the reset button
    def reset_button(self):
        fill(255,255, 255)
        stroke(0, 140, 0)
        strokeWeight(3)
        rect(1140, 230, 200, 40)
        fill(0, 0, 0)
        textSize(25)
        text('RESET', 1150, 240, 200, 50)
        
        if mouseX>1140 and mouseX<1340 and mouseY>230 and mouseY<280:
            self.over_box2=True
        else:
            self.over_box2=False
        


                
                        

class Game:
    def __init__(self):
        self.f= GameFunctionalities()    
        self.g = Grids()       
        self.b = Body(2, 2, 0, 1000,700)
        self.time = Timer()
        

    def show(self):
        
        # self.time.countUp()
        self.time.countDown()
            
        
        self.g.elements()
        
        self.b.show_opponent()
        self.g.show_maze()
        self.g.show_maze2()
        self.b.show_body()
        self.g.show_candy()
        
        if self.b.start ==True:
            # self.b.Rotate()
            self.b.move()
        if self.time.time <= 0:
            game.b.start = False
            background(0)
            fill(255,255, 255)
            textSize(20)
            text("Time Over", 500, 300)
            fill(255,255, 255)
            textSize(20)
            text("Click reset then start to play again", 500, 350)
        
        self.b.collision()
        self.f.instructions()
        self.f.start_button()
        self.f.reset_button()
        if self.b.reset==True:
            self.b.r=2
            self.b.c=2
            self.b.start=False
        self.b.reset=False
        if self.b.start ==True:
            self.b.move()
        self.g.show_checkpoint()
        
            
        
        



game = Game()
# file = SoundFile(this, "old_town.mp3")
# musicPlaying = False

def setup():
    size(2000,625)

def draw():
    # global file,musicPlaying
    background(255)
    # if game.b.start and (not musicPlaying or game.time.total_time_taken%123==0):
    #     file.play()
    #     musicPlaying = True
    # if game.b.start == False:
    #     file.stop()
    game.show()

    
    
def keyPressed():
    if keyCode == LEFT:
        game.b.key_handler[LEFT] = True
    elif keyCode == RIGHT:
        game.b.key_handler[RIGHT] = True
    elif keyCode == UP:
        game.b.key_handler[UP] = True   
    elif keyCode == DOWN:
        game.b.key_handler[DOWN]=True
def keyReleased():
    if keyCode == LEFT:
        game.b.key_handler[LEFT] =False
    elif keyCode == RIGHT:
        game.b.key_handler[RIGHT] = False
    elif keyCode == UP:
        game.b.key_handler[UP] = False  
    elif keyCode ==DOWN:
        game.b.key_handler[DOWN]=False
        
def mouseClicked():
    global b 
    if game.f.over_box == True:
        game.b.start=True
    elif game.f.over_box2 == True:
        game.b.reset=True
        
    else:
        pass
        
        

        
    

    
