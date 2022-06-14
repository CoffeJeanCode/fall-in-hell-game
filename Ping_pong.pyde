'''
[] storySection
[X] Instrutions
[] Connection to robotcito
'''

# add_library("serial")

# connection
# portIndex = 0
# myPort = Serial(this, Serial.list()[portIndex], 9600)

# Game
isPlaying = False
isGameOver = False
isPause = False
storySection = False
timer = 0

# Bar
xBar = 0
yBar = 0
sBar = 15
wBar = 0
hBar = 0 

# Ball
yBall = 0
xBall = 0
speedXBall = 0
speedYBall = 0
sizeBall = 0

# Point
points = 0

# Desing
gameGap = 10
ballImage = ""
pauseButtonImage = ""
backgroundImage = ""
upKeyUpImage = ""
downKeyUpImage = ""
leftKeyUpImage = ""
rightKeyUpImage = ""

def setup():
    global xBar, yBar, yBall, xBall, sBall, speedYBall, speedXBall, sizeBall, wBar, hBar, gameGap, ballImage, pauseButtonImage, backgroundImage, upKeyUpImage, downKeyUpImage, rightKeyUpImage, leftKeyUpImage, timer, storySection
    size(800, 600)
    smooth(4)
    
    # Bar
    xBar = width / 2
    yBar = height / 1.2
    wBar = width / 5
    hBar = height / 20
    
    # Ball
    sizeBall = width / 20
    xBall = random(width - sizeBall)
    speedBall = width / 200
    yBall = height / 4
    speedXBall = -speedBall if xBall > width / 2 else speedBall
    speedYBall = speedBall
    
    # Desing
    gameGap = width / 90
    ballImage = loadImage("./images/devil.png")
    pauseButtonImage = loadImage("./images/pausa.png")
    backgroundImage = loadImage("./images/background.jpg")
    upKeyUpImage = loadImage("./images/up.png")
    downKeyUpImage = loadImage("./images/down.png")
    rightKeyUpImage = loadImage("./images/right.png")
    leftKeyUpImage = loadImage("./images/left.png")

    # Game
    timer = 0
    
    # Connection
    # print("Lista", Serial.list())
    # myPort.bufferUntil(10)
    
    
def draw():
    global xBar, yBar, yBall, xBall, sBall, speedYBall, speedXBall, sizeBall, wBar, hBar, gameGap, points, isPlaying, isGameOver, pauseButtonImage, backgroundImage, ballImage, upKeyUpImage, downKeyUpImage, leftKeyUpImage, rightKeyUpImage, timer, storySection

    # Background 
    background(0)
    tint(100)
    imageMode(CORNER)
    image(backgroundImage, 0, 0, width, height)
    
    noTint()
    
    # Home 
    if not isPlaying and not isGameOver and not isPause:
        home()


    # storySection
    if storySection:
        fill(0)
        rectMode(CORNER)
        rect(0, 0, width, height)
        
        fill(255)
        textAlign(CENTER)
        textSize(40)
        text("HISTORIA", width / 2, height / 10)
        textSize(25)
        text("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sit amet lectus nisi. Proin commodo sem commodo aliquet porttitor. Nulla in venenatis orci. Maecenas gravida magna et mi congue malesuada. Morbi urna magna, tempus ut augue vitae, condimentum elementum nisi. Ut congue malesuada elit, at dictum libero luctus vel. Proin eu tellus vel enim tempor pulvinar. Duis risus neque, faucibus non laoreet eu, facilisis vel purus. Nam ornare tincidunt ipsum, in aliquet felis. Nunc ultrices mi et massa condimentum, in cursus magna fermentum.", 40, 40, width, height)

    # Pause
    if isPause:
        textAlign(CENTER)
        textMode(CENTER)
        text("PAUSA", width / 2, height / 3)
        imageMode(CENTER)
        image(pauseButtonImage, width / 2, height / 1.5, width / 10, width / 10)
    
    # Game
    if isPlaying and not isGameOver:    

        # Instructions
        if  timer < 20000:
            fill(color(255, 100))
            textAlign(CENTER)
            text("COMO JUGAR", width / 2, height / 3)
            
            tint(255, 100)
            imageMode(CENTER)
            image(loadImage("./images/right.png"), width / 2 + width / 10, height / 2, width / 10, width / 10)
            image(loadImage("./images/left.png"), width / 2 - width / 10, height / 2, width / 10, width / 10)

        # Ball
        fill(250,10,0)
        tint(255, 255)
        noStroke()
        image(ballImage, xBall, yBall, sizeBall, sizeBall)
        
        # Bar
        rectMode(CENTER)
        fill(255)
        noStroke()
        rect(xBar, yBar, wBar, hBar)

        
        # Game Points
        textSize(width / 15)
        textAlign(LEFT)
        text(str(points), width / 55, height / 10)
            
        xBall += speedXBall
        yBall += speedYBall

        # Right
        if xBall + sizeBall  >= width + gameGap:
            speedXBall = -speedXBall
            xBall = (width + gameGap) - sizeBall
            
        # Left
        elif xBall <= gameGap: 
            speedXBall = -speedXBall
            xBall = sizeBall - gameGap
            
        # Bottom
        if yBall + sizeBall > (height + gameGap):
            isPlaying = False
            isGameOver = True
            yBall = height - sizeBall
        
        # Top    
        elif (yBall <= gameGap):
            speedYBall = -speedYBall
            yBall = sizeBall - gameGap
            
            points += 1
            speedXBall += 0.3
            speedYBall += 0.3

    
        # Collition
        if xBall > xBar - wBar / 2 and xBall < xBar + wBar / 2 and yBall > yBar - sizeBall and yBall < yBar + sizeBall:
            speedYBall = -speedYBall
        
        # Limits bar
        if xBar > (width - gameGap) - wBar / 2:
            xBar = (width - gameGap) - wBar / 2
    
        if xBar < gameGap + wBar / 2:
            xBar = gameGap + wBar / 2
    
        timer = millis()     
    
    # Gamer Over
    if isGameOver and not isPlaying:
        textAlign(CENTER)
        textSize(60)
        text("GAME OVER", width / 2, height / 2)
        textSize(15)
        text("Presione ESPACIO para volver a jugar", width / 2, height / 1.7)
    
    # if myPort.available() > 0:
    #     val = myPort.read()
    #     if val == 65:
    #         xBar -= sBar
    #     if val == 66:
    #         xBar += sBar
    # stroke(255)
    # line(width / 2, 0, width / 2, height)
    # line(0, height / 2, width, height / 2)
def keyPressed():
    global xBar, sBar, isPlaying, isGameOver, isPause, storySection
    
    if keyCode == 80:
        isPlaying = True
    
    if isPlaying:
        if keyCode == LEFT:
            xBar -= sBar
        if keyCode == RIGHT:
            xBar += sBar
    
    if not isGameOver:
        if keyCode == DOWN:
            isPlaying = False
            isPause = True
        if keyCode == UP:
            isPlaying = True
            isPause = False

    if not isPlaying and not isGameOver:
        if keyCode == 72:
            isPlaying = False
            storySection = not storySection
    if keyCode == 32 and isGameOver:
        resetGame()
        

def resetGame():
    global xBar, yBar, yBall, xBall, sBall, speedYBall, speedXBall, sizeBall, wBar, hBar, gameGap, ballImage, pauseButtonImage, backgroundImage, isGameOver, isPause, isPlaying, points, timer
    
    xBar = width / 2
    yBar = height / 1.2
    wBar = width / 5
    hBar = height / 20
    
    
    sizeBall = width / 20
    xBall = random(width - sizeBall)
    yBall = height / 4
    speedXBall = -3 if xBall > width / 2 else 3
    speedYBall = 3
    
    gameGap = width / 80
    ballImage = loadImage("./images/devil.png")
    pauseButtonImage = loadImage("./images/pausa.png")
    backgroundImage = loadImage("./images/background.jpg")
    isGameOver = False
    timer = 0

    points = 0


def home():
        noStroke()
        rectMode(CORNER)
        fill(color(164, 22, 26, 100))
        rect(0, 0, width, height)
        
        fill(255)
        textAlign(CENTER)
        textSize(70)
        text("Fall in Hell", width / 2, height / 2.3)

        rectMode(CENTER)
        rect(width / 2, height / 1.3, 150, 60)
        fill(0)
        textSize(20)

        noFill()
        stroke(0)
        rect(width / 1.79, height / 1.29, 30, 30, 10, 10, 10, 10)

        text("JUGAR", width / 2.1, height / 1.28)
        text("P", width / 1.8, height / 1.28)
