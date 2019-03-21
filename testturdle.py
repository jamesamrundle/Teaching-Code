import turtle

### code for visual teaching tool for introductory coding skills
######### running as is, lets user draw simple rectagles for maps. clicking upper left corner and lower right corner to draw rectangle
###if map is drawn, and user uses original control methods (excluding forward) and created move(turtle,blocks_forward) method, 
	####game will show warning method if the turtle runs into a barrier(red rect), or winning message if they get to the goal (blue rect)

screen = turtle.Screen()
screen.setup(150,150)

GOAL = 1
BARRIER = 0

# screen.bgpic('./images/grid.png')

screen.screensize(50,50)
screen.setworldcoordinates(0,150,150,0)

bill = turtle.Turtle();
bill.pensize(1)
bill.color("silver")
bill.speed(10000)
bill.hideturtle()




def makeBorder():
    #######First make border
    bill.pensize(2)
    bill.forward(150)
    bill.left(90)
    bill.forward(150)
    bill.left(90)
    bill.forward(150)
    bill.left(90)
    bill.forward(150)
    bill.setpos(0, 0)
    bill.left(90)
    ##############

def makeShape(uL,lR,type): #draws shape to grid
    if(type==GOAL):
        bill.color("cyan")
    else:
        bill.fillcolor("red")

    bill.penup()

    bill.begin_fill()
    bill.setpos(uL[0] * 10, uL[1] * 10)
    bill.setpos(lR[0] * 10, uL[1] * 10)
    bill.setpos(lR[0] * 10, lR[1] * 10)
    bill.setpos(uL[0] * 10, lR[1] * 10)
    bill.setpos(uL[0] * 10, uL[1] * 10)
    bill.penup()
    bill.end_fill()
    registerShape(uL,lR,type)

shapes = [["" for i in range(150)] for j in range(150)]
printableshapes = [["" for i in range(15)] for j in range(15)]


def registerShape(uL,lR,type): # registers shape to collision and printable array
    char = "X"
    if(type == GOAL):
        char = "O" ## capital letter "o"

    for x in range(uL[0]*10,lR[0]*10): #registers in collision array
        for y in range(uL[1]*10,lR[1]*10):
            shapes[x][y] = char

    for x in range(uL[0],lR[0]): # registers in printable array
        for y in range(uL[1],lR[1]):
            printableshapes[y][x] = char

    for i in range(15): #prints updated array to console
        print(i,printableshapes[i])


clickX = None
clickY = None


clickList= []
clickList2= []


def getClick(x,y): #register clicks for barrier panels
    print("in getclick")
    global clickList
    clickX = roundNum(x)
    clickY = roundNum(y)
    clickList.append((clickX,clickY))
    print("clicked:",clickX,clickY)
    print("clicklist : ",clickList)
    if (len(clickList) > 1): #list to only store 2 values upper left and lower right corners of polygon
        makeShape(clickList[0],clickList[1],BARRIER)
        clickList = []

def getClick2(x,y): # registers clicks for drawing goal panels
    print("in getclick goal")
    global clickList2
    clickX = roundNum(x)
    clickY = roundNum(y)
    clickList2.append((clickX,clickY))
    print("clicked2:",clickX,clickY)
    print("clicklist2 : ",clickList)
    if (len(clickList2) > 1): #see getClick
        makeShape(clickList2[0],clickList2[1],GOAL)
        clickList2 = []

releaseX = None
releaseY = None

def getRelease(x,y): ## apparently useless for current code
    print("in release")
    releaseX = roundNum(x)
    releaseY = roundNum(y)
    print("released",releaseX,releaseY)
    if((clickX == releaseX) and (clickY == releaseY)):
        makeShape((clickX,clickY),(releaseX,releaseY),BARRIER)
    else:
        makeShape((clickX,clickY),(releaseX,releaseY),GOAL)

def roundNum(num): ## helper fctn for drawing shapes to grid lines
    if((num % 10) < 5):
        return int((num - (num % 10))/10)
    elif((num%10)>=5):
        return int((num + (10 -(num%10)))/10)

def makeLines(iteration):

#######function to draw gridlines
    bill.pensize(1)
    bill.color("silver")
    bill.speed(10000)
    bill.hideturtle()

    xCoord = 0
    yCoord = 0+ 10 * iteration
    if(iteration < 15):
        makeLines( iteration+1 )

    bill.penup()
    bill.setpos(xCoord,yCoord)

    bill.pendown()

    bill.forward(150)

    bill.penup()
    bill.setpos(yCoord,xCoord)
    bill.pendown()
    bill.left(90)
    bill.forward(150)
    bill.right(90)


# shapes = [["" for i in range(150)] for j in range(150)]
# for i in range(0+150,5+150):
#     for j in range(125,25+150):
#         shapes[j][i] = "X"
#
# for i in range(150):
#     print(shapes[i])



makeBorder()
makeLines(0)

##### Example for pre generated map #####
# makeShape((5,3),(6,11),BARRIER)
# makeShape((7,3),(8,11),BARRIER)
# # makeShape((2,0),(3,2),BARRIER)
# makeShape((6,6),(7,7),GOAL)
#
# doug = turtle.Turtle()
# doug.tilt(135)
# doug.penup()


# doug.setpos(3,3)
#
# move(doug,6)
# doug.left(90)
# move(doug,7)
# doug.right(90)
# move(doug,6)
########################

def move(doug,x): # moves 
    for i in range(x*10):
        doug.forward(1)
        x = int(doug.xcor())
        y = int(doug.ycor())
        print("x=",x,"y=",y," : ",shapes[x][y])
        if(shapes[x][y] == "X"):
            doug.write("OH NO!")
            doug.forward(-1)
            break
        if(shapes[x][y] == "O"):
            doug.write("U DA WINNER")
            break


    for i in range(50):
        if(i%2 == 0):
            bill.pendown()
        else:
            bill.penup()
        bill.forward(6)
        bill.pendown()

print("listening")

screen.listen()
screen.onclick(getClick,1)
screen.onclick(getClick2,2) # for me, this is a wheel click. Documentation says it should be both l and r mouse buttons
x = 0






turtle.done()
