#FinalProject.pyw
#Destin Attapallil
#December 5, 2013
#This program creates a GUI version of Rock, Paper, Scissors.
#It is a one player game. The player has a options to play as many times
#as they want. Each time the game is played, player is prompt for a weapon
#and then displays the winner of each hand with the point totals.

from graphics import *
from time import *
from random import randrange

#function definitions
#x1,y1 is the bottom left
#x2,y2 is the top right
def IsValidClick(win, x1, y1, x2, y2):
    p1 = win.getMouse()
    if p1.getX() >=x1 and p1.getX() <=x2 and p1.getY() >=y1 and p1.getY() <= y2:
        return True
    else:
        return False

def TextLayout(x, y, text, color, style):
    txtObject = Text(Point(x, y), text)
    txtObject.setTextColor(color)
    txtObject.setStyle(style)

    return txtObject

def GetComputer():
    randomNumber = 0
    #randomNumber as integer
    #generate a random number from 1 to 12
    randomNumber = randrange(1,13)
    tempComputer = randomNumber
    return tempComputer

def displayResults(displayText, image, win):
    TextD = Text(Point(7,4), displayText)
    TextD.setTextColor("Red")
    TextD.setStyle("bold")
    TextD.setSize(10)
    TextD.draw(win)
    image.draw(win)
    sleep(2)
    TextD.undraw()
    image.undraw()
    
def main():
    #declare and initialize variables and constants
    #Int draws =0, singleplayerwins = 0, computerwins = 0, single_player_weapon=0
    draws = 0
    singleplayerwins = 0
    computerwins = 0
    single_player_weapon = 0

    #bool isOver
    isOver = False

    #create a graphics window
    win = GraphWin("Rock, Paper, Scissors",500,500)

    #set coordinates to 10 x 10
    win.setCoords(0,0,10,10)

    #set a background color
    win.setBackground("blue")

    #create a button using a image   
    btnRules = Image(Point(5,8), "button.gif")
    btnRules.draw(win)

    #create and draw text for button
    txtRules = Text(Point(5,8), "Rules")
    txtRules.draw(win)

    #create a button using a image  
    btnGame = Image(Point(5,5), "button.gif")
    btnGame.draw(win)

     #create and draw text for button
    txtGame = Text(Point(5,5), "Play Game")
    txtGame.draw(win)

    #create a button using a image  
    btnExit = Image(Point(5,2), "button.gif")
    btnExit.draw(win)

    #create and draw text for button
    txtExit= Text(Point(5,2), "Exit")
    txtExit.draw(win)

    #display an image
    imgRules = Image(Point(5,5), "Rules.gif")
    imgBlank = Image(Point(5,5), "blank.gif")
    imgRockW = Image(Point(2,3), "rockwins.gif")
    imgPaperW = Image(Point(2,3), "paperwins.gif")
    imgScissorsW = Image(Point(2,3), "scissorswins.gif")
    imgDraw = Image(Point(2,3), "Draw.gif")
    
    
    while isOver == False:
        p1 = win.getMouse()
        if p1.getX() >= 4 and p1.getY() >= 6 and p1.getX() <= 7 and p1.getY() <= 9:
            imgRules.draw(win)
            sleep(3)
            imgRules.undraw()

            
        elif p1.getX() >= 4 and p1.getY() >= 4 and p1.getX() <= 6 and p1.getY() <= 6:
            btnRules.undraw()
            txtRules.undraw()
            btnGame.undraw()
            txtGame.undraw()
            btnExit.undraw()
            txtExit.undraw()
            imgBlank.draw(win)
            
            #set a background color
            win.setBackground("black")

            #create and draw text
            txtChoose = TextLayout(5, 9, "Choose Your Weapon", "Red", "bold")
            txtChoose.draw(win)
            
            #display an image
            #create text using TextLayout function and draw
            imgRock= Image(Point(2,7), "Rock.gif")
            imgRock.draw(win)
            txtRock = TextLayout(2,5, "Rock", "Red", "bold")
            txtRock.draw(win)

            #display an image
            #create text using TextLayout function and draw
            imgPaper= Image(Point(8,7), "Paper.gif")
            imgPaper.draw(win)
            txtPaper = TextLayout(8,5, "Paper", "Red", "bold")
            txtPaper.draw(win)

            #display an image
            #create text using TextLayout function and draw
            imgScissors= Image(Point(5,7), "Scissors.gif")
            imgScissors.draw(win)
            txtScissors = TextLayout(5,5,"Scissors", "Red","bold")
            txtScissors.draw(win)

            #Create and draw Rectangle for the button
            rectButton3 = Rectangle(Point(4.5,1), Point(5.5,1.8))
            rectButton3.setFill("red")
            rectButton3.draw(win)

            #Create and draw Text for button
            txtButton3 = TextLayout(5, 1.4, "EXIT", "black", "bold")
            txtButton3.setSize(12)
            txtButton3.draw(win)
            
            #draw on blank screen to play rest of game
            imgBlank.undraw()
            
            while isOver == False:
                x=0
                single_player_weapon=0
                computer=0
                p1 = win.getMouse()
                #if statements
                if IsValidClick(win, 1, 6, 3, 8)== True:
                    single_player_weapon = 1

                elif IsValidClick(win, 4, 6, 6, 8)== True:
                    single_player_weapon = 2 

                elif IsValidClick(win, 7.3, 5.7, 8.7, 8.3)== True:
                    single_player_weapon = 3
                elif IsValidClick(win, 4.5, 1, 5.5, 1.8)== True:
                    isOver = True
                else:
                    #invalid
                    x =10
            

                if isOver == False and x != 10:
                    #get random number using GetComputer function
                    computer = GetComputer()

                    #if statements
                    if single_player_weapon==3 and (computer > 0 and computer < 5):
                        #create text,display an image and draw using TextLayout function
                        displayResults("Paper Covers Rock, Player Wins", imgPaperW, win)
                        #Add to player wins
                        singleplayerwins += 1
                        

                    elif (computer > 4 and computer < 9) and single_player_weapon==1:
                        #create text,display an image and draw using TextLayout function
                        displayResults("Paper Covers Rock, Computer Wins", imgPaperW, win)
                        #Add to computer wins
                        computerwins += 1
                        
                    elif single_player_weapon==1 and(computer > 7 and computer < 13):
                        #create text,display an image and draw using TextLayout function
                        displayResults("Rock Smashed Scissors, Player Wins", imgRockW, win)
                        #Add to player wins
                        singleplayerwins += 1
                    
                    elif (computer > 0 and computer < 5) and single_player_weapon==2:
                        #create text,display an image and draw using TextLayout function
                        displayResults("Rock Smashed Scissors, Computer Wins", imgRockW, win)
                        #Add to computer wins
                        computerwins += 1
                    
                    elif single_player_weapon==2 and (computer > 4 and computer < 9):
                        #create text,display an image and draw using TextLayout function
                        displayResults("Scissors Cut Paper, Player Wins", imgScissorsW, win)
                        #Add to player wins
                        singleplayerwins += 1
                        
                    elif (computer > 7 and computer < 13) and single_player_weapon==3:
                        #create text,display an image and draw using TextLayout function
                        displayResults("Scissors Cut Paper, Computer Wins", imgScissorsW, win)
                        #Add to computer wins
                        computerwins += 1
                        

                    elif(computer > 0 and computer < 5) and single_player_weapon ==1:
                        #create text,display an image and draw using TextLayout function
                        displayResults("You both picked Rock results in a Draw", imgDraw, win)
                        #Add to draws
                        draws += 1

                    elif(computer > 4 and computer < 9) and single_player_weapon ==3:
                        #create text,display an image and draw using TextLayout function
                        displayResults("You both picked Paper results in a Draw", imgDraw, win)
                        #Add to draws
                        draws += 1

                    elif(computer > 7 and computer < 13) and single_player_weapon==2:
                        #create text,display an image and draw using TextLayout function
                        displayResults("You both picked Scissors results in a Draw", imgDraw, win)
                        #Add to draws
                        draws += 1


                    #create text, calculate scores, and draw
                    finalString = ("Players Wins: " + str(singleplayerwins) + "\n" + "Players Lose: " + str(computerwins) + "\n" +  "Total Draws: " + str(draws))
                    txtScore = TextLayout(7,3, finalString, "Red", "bold")
                    txtScore.setSize(10)
                    txtScore.draw(win)
                    sleep(2)
                    txtScore.undraw()

                if isOver == True:
                    #close window
                    win.close()

 
                    
        elif p1.getX() >= 4 and p1.getY() >= 1 and p1.getX() <= 5 and p1.getY() <= 2:
            isOver = True
            #close window
            win.close()
            
    
main()
