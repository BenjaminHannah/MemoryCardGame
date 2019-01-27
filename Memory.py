# implementation of card game - Memory

import simplegui
import random

global Turn
Turn = 0

Expose_Card1 = 1
Expose_Card2 = 1
Expose_Card3 = 1
Expose_Card4 = 1
Expose_Card5 = 1
Expose_Card6 = 1
Expose_Card7 = 1
Expose_Card8 = 1
Expose_Card9 = 1
Expose_Card10 = 1
Expose_Card11 = 1
Expose_Card12 = 1
Expose_Card13 = 1
Expose_Card14 = 1
Expose_Card15 = 1
Expose_Card16 = 1

Expose_Guess1 = None

Guess1 = None
Guess2 = None


# helper function to initialize globals
def new_game():
    global state
    state = 0
    
    global Turn
    Turn = 0
    label.set_text("Turns = " + str(Turn))
    
    global Expose_Card1
    global Expose_Card2
    global Expose_Card3
    global Expose_Card4
    global Expose_Card5
    global Expose_Card6
    global Expose_Card7
    global Expose_Card8
    global Expose_Card9
    global Expose_Card10
    global Expose_Card11
    global Expose_Card12
    global Expose_Card13
    global Expose_Card14
    global Expose_Card15
    global Expose_Card16
    
    Expose_Card1 = 1
    Expose_Card2 = 1
    Expose_Card3 = 1
    Expose_Card4 = 1
    Expose_Card5 = 1
    Expose_Card6 = 1
    Expose_Card7 = 1
    Expose_Card8 = 1
    Expose_Card9 = 1
    Expose_Card10 = 1
    Expose_Card11 = 1
    Expose_Card12 = 1
    Expose_Card13 = 1
    Expose_Card14 = 1
    Expose_Card15 = 1
    Expose_Card16 = 1
    
    global listOfCards
    listOfCards=[i for i in range(8)]+[i for i in range(8)]
    random.shuffle(listOfCards)

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state
    global listOfCards
    
    global Expose_Card1
    global Expose_Card2
    global Expose_Card3
    global Expose_Card4
    global Expose_Card5
    global Expose_Card6
    global Expose_Card7
    global Expose_Card8
    global Expose_Card9
    global Expose_Card10
    global Expose_Card11
    global Expose_Card12
    global Expose_Card13
    global Expose_Card14
    global Expose_Card15
    global Expose_Card16
    
    global Turn
    
    global Expose_Guess1
    
    global Guess1
    global Guess2
    
    if state == 0: 
        state = 1
    elif state == 1:
        state = 2
        
    else:
        state = 1
        
        Guess1 = None
        Guess2 = None

        if Expose_Card1 != 3:
            Expose_Card1 = 1
        if Expose_Card2 != 3:    
            Expose_Card2 = 1
        if Expose_Card3 != 3:
            Expose_Card3 = 1
        if Expose_Card4 != 3:    
            Expose_Card4 = 1
        if Expose_Card5 != 3:    
            Expose_Card5 = 1
        if Expose_Card6 != 3:    
            Expose_Card6 = 1
        if Expose_Card7 != 3:    
            Expose_Card7 = 1
        if Expose_Card8 != 3:    
            Expose_Card8 = 1
        if Expose_Card9 != 3:    
            Expose_Card9 = 1
        if Expose_Card10 != 3:    
            Expose_Card10 = 1
        if Expose_Card11 != 3:    
            Expose_Card11 = 1
        if Expose_Card12 != 3:    
            Expose_Card12 = 1
        if Expose_Card13 != 3:    
            Expose_Card13 = 1
        if Expose_Card14 != 3:
            Expose_Card14 = 1
        if Expose_Card15 != 3:
            Expose_Card15 = 1
        if Expose_Card16 != 3:
            Expose_Card16 = 1
            
    print Expose_Card1    
    if pos[0] > 0 and pos[0] < 50 and (Expose_Card1 != 0 and Expose_Card1 != 3):
        
        if Expose_Card1 != 3:
            Expose_Card1 = 0

        if state == 1:
            Guess1 = listOfCards[0]
            Expose_Guess1 = 0
        if state == 2:
            Guess2 = listOfCards[0]
            Turn = Turn + 1
            label.set_text("Turns = " + str(Turn))
        if Guess1 == Guess2:
            Expose_Card1 = 3
            ExposeGuess1()
     
            
    elif pos[0] > 50 and pos[0] < 100 and (Expose_Card2 != 0 and Expose_Card2 != 3):
        if Expose_Card2 != 3:
            Expose_Card2 = 0
        
        if state == 1:
            Guess1 = listOfCards[1]
            Expose_Guess1 = 1
        if state == 2:
            Guess2 = listOfCards[1]
            Turn = Turn + 1
            label.set_text("Turns = " + str(Turn))  #NextTurn
        if Guess1 == Guess2:
            Expose_Card2 = 3
            ExposeGuess1()
        
    elif pos[0] > 100 and pos[0] < 150 and (Expose_Card3 != 0 and Expose_Card3 != 3):
        if Expose_Card3 != 3:
            Expose_Card3 = 0
        
        if state == 1:
            Guess1 = listOfCards[2]
            Expose_Guess1 = 2
        if state == 2:
            Guess2 = listOfCards[2]
            Turn = Turn + 1
            label.set_text("Turns = " + str(Turn))  #NextTurn
        if Guess1 == Guess2:
            Expose_Card3 = 3    
            ExposeGuess1()   
    
    elif pos[0] > 150 and pos[0] < 200 and (Expose_Card4 != 0 and Expose_Card4 != 3):
        if Expose_Card4 != 3:
            Expose_Card4 = 0
        
        if state == 1:
            Guess1 = listOfCards[3]
            Expose_Guess1 = 3
        if state == 2:
            Guess2 = listOfCards[3]
            Turn = Turn + 1
            label.set_text("Turns = " + str(Turn))  #NextTurn
        if Guess1 == Guess2:
            Expose_Card4 = 3
            ExposeGuess1()
        
    elif pos[0] > 200 and pos[0] < 250 and (Expose_Card5 != 0 and Expose_Card5 != 3):
        if Expose_Card5 != 3:
            Expose_Card5 = 0
        
        if state == 1:
            Guess1 = listOfCards[4]
            Expose_Guess1 = 4
        if state == 2:
            Guess2 = listOfCards[4]
            Turn = Turn + 1
            label.set_text("Turns = " + str(Turn))  #NextTurn
        if Guess1 == Guess2:
            Expose_Card5 = 3
            ExposeGuess1()
            
    elif pos[0] > 250 and pos[0] < 300 and (Expose_Card6 != 0 and Expose_Card6 != 3):
        if Expose_Card6 != 3:
            Expose_Card6 = 0
        
        if state == 1:
            Guess1 = listOfCards[5]
            Expose_Guess1 = 5
        if state == 2:
            Guess2 = listOfCards[5]
            Turn = Turn + 1
            label.set_text("Turns = " + str(Turn))  #NextTurn
        if Guess1 == Guess2:
            Expose_Card6 = 3
            ExposeGuess1()
            
    elif pos[0] > 300 and pos[0] < 350 and (Expose_Card7 != 0 and Expose_Card7 != 3):
        if Expose_Card7 != 3:
            Expose_Card7 = 0
        
        if state == 1:
            Guess1 = listOfCards[6]
            Expose_Guess1 = 6
        if state == 2:
            Guess2 = listOfCards[6]
            Turn = Turn + 1
            label.set_text("Turns = " + str(Turn))  #NextTurn
        if Guess1 == Guess2:
            Expose_Card7 = 3
            ExposeGuess1()
            
    elif pos[0] > 350 and pos[0] < 400 and (Expose_Card8 != 0 and Expose_Card8 != 3):
        if Expose_Card8 != 3:
            Expose_Card8 = 0
        
        if state == 1:
            Guess1 = listOfCards[7]
            Expose_Guess1 = 7
        if state == 2:
            Guess2 = listOfCards[7]
            Turn = Turn + 1
            label.set_text("Turns = " + str(Turn))  #NextTurn
        if Guess1 == Guess2:
            Expose_Card8 = 3
            ExposeGuess1()
            
    elif pos[0] > 400 and pos[0] < 450 and (Expose_Card9 != 0 and Expose_Card9 != 3):
        if Expose_Card9 != 3:
            Expose_Card9 = 0
        
        if state == 1:
            Guess1 = listOfCards[8]
            Expose_Guess1 = 8
        if state == 2:
            Guess2 = listOfCards[8]
            Turn = Turn + 1
            label.set_text("Turns = " + str(Turn))  #NextTurn
        if Guess1 == Guess2:
            Expose_Card9 = 3
            ExposeGuess1()
            
    elif pos[0] > 450 and pos[0] < 500 and (Expose_Card10 != 0 and Expose_Card10 != 3):
        if Expose_Card10 != 3:
            Expose_Card10 = 0
        
        if state == 1:
            Guess1 = listOfCards[9]
            Expose_Guess1 = 9
        if state == 2:
            Guess2 = listOfCards[9]
            Turn = Turn + 1
            label.set_text("Turns = " + str(Turn))  #NextTurn
        if Guess1 == Guess2:
            Expose_Card10 = 3    
            ExposeGuess1()
            
    elif pos[0] > 500 and pos[0] < 550 and (Expose_Card11 != 0 and Expose_Card11 != 3):
        if Expose_Card11 != 3:
            Expose_Card11= 0
        
        if state == 1:
            Guess1 = listOfCards[10]
            Expose_Guess1 = 10
        if state == 2:
            Guess2 = listOfCards[10]
            Turn = Turn + 1
            label.set_text("Turns = " + str(Turn))  #NextTurn
        if Guess1 == Guess2:
            Expose_Card11 = 3   
            ExposeGuess1()
            
    elif pos[0] > 550 and pos[0] < 600 and (Expose_Card12 != 0 and Expose_Card12 != 3):
        if Expose_Card12 != 3:	
            Expose_Card12 = 0
            
        if state == 1:
            Guess1 = listOfCards[11]
            Expose_Guess1 = 11
        if state == 2:
            Guess2 = listOfCards[11]
            Turn = Turn + 1
            label.set_text("Turns = " + str(Turn))  #NextTurn
        if Guess1 == Guess2:
            Expose_Card12 = 3
            ExposeGuess1()
            
    elif pos[0] > 600 and pos[0] < 650 and (Expose_Card13 != 0 and Expose_Card13 != 3):
        if Expose_Card13 != 3:	
            Expose_Card13 = 0
        
        if state == 1:
            Guess1 = listOfCards[12]
            Expose_Guess1 = 12
        if state == 2:
            Guess2 = listOfCards[12]
            Turn = Turn + 1
            label.set_text("Turns = " + str(Turn))  #NextTurn
        if Guess1 == Guess2:
            Expose_Card13 = 3
            ExposeGuess1()
            
    elif pos[0] > 650 and pos[0] < 700 and (Expose_Card14 != 0 and Expose_Card14 != 3):
        if Expose_Card14 != 3:
            Expose_Card14 = 0
        
        if state == 1:
            Guess1 = listOfCards[13]
            Expose_Guess1 = 13
        if state == 2:
            Guess2 = listOfCards[13]
            Turn = Turn + 1
            label.set_text("Turns = " + str(Turn))  #NextTurn
        if Guess1 == Guess2:
            Expose_Card14 = 3
            ExposeGuess1()
            
            
    elif pos[0] > 700 and pos[0] < 750 and (Expose_Card15 != 0 and Expose_Card15 != 3):
        if Expose_Card15 != 3:
            Expose_Card15 = 0
        
        if state == 1:
            Guess1 = listOfCards[14]
            Expose_Guess1 = 14
        if state == 2:
            Guess2 = listOfCards[14]
            Turn = Turn + 1
            label.set_text("Turns = " + str(Turn))  #NextTurn
        if Guess1 == Guess2:
            Expose_Card15 = 3
            ExposeGuess1()
            
    elif pos[0] > 750 and pos[0] < 800 and (Expose_Card16 != 0 and Expose_Card16 != 3):
        if Expose_Card16 != 3:
            Expose_Card16 = 0   
        
        if state == 1:
            Guess1 = listOfCards[15]
            Expose_Guess1 = 15
        if state == 2:
            Guess2 = listOfCards[15]
            Turn = Turn + 1
            label.set_text("Turns = " + str(Turn))  #NextTurn
        if Guess1 == Guess2:
            Expose_Card16 = 3    
            ExposeGuess1()
            
    else: state = 1
    
    print "Guess 1 = ",Guess1
    print "Guess 2 = ",Guess2          
                        
# cards are logically 50x100 pixels in size    
def ExposeGuess1():
    
    print "ExposeGuess1"
    print "Guessing 1 =", Guess1
    print "Guessing 2 =", Guess2
    
    global Expose_Card1
    global Expose_Card2
    global Expose_Card3
    global Expose_Card4
    global Expose_Card5
    global Expose_Card6
    global Expose_Card7
    global Expose_Card8
    global Expose_Card9
    global Expose_Card10
    global Expose_Card11
    global Expose_Card12
    global Expose_Card13
    global Expose_Card14
    global Expose_Card15
    global Expose_Card16
    
    
    global Expose_Guess1
    
    if Expose_Guess1 == 0:
        Expose_Card1 = 3
        print "Expose_Card1"
    if Expose_Guess1 == 1:
        Expose_Card2 = 3
        print "Expose_Card2"
    if Expose_Guess1 == 2:
        Expose_Card3 = 3
        print "Expose_Card3"
    if Expose_Guess1 == 3:
        Expose_Card4 = 3
        print "Expose_Card4"
    if Expose_Guess1 == 4:
        Expose_Card5 = 3
        print "Expose_Card5"
    if Expose_Guess1 == 5:
        Expose_Card6 = 3
        print "Expose_Card6"
    if Expose_Guess1 == 6:
        Expose_Card7 = 3
        print "Expose_Card7"
    if Expose_Guess1 == 7:
        Expose_Card8 = 3
        print "Expose_Card8"
    if Expose_Guess1 == 8:
        Expose_Card9 = 3
        print "Expose_Card9"
    if Expose_Guess1 == 9:
        Expose_Card10 = 3
        print "Expose_Card10"
    if Expose_Guess1 == 10:
        Expose_Card11 = 3
        print "Expose_Card11"
    if Expose_Guess1 == 11:
        Expose_Card12 = 3
        print "Expose_Card12"
    if Expose_Guess1 == 12:
        Expose_Card13 = 3
        print "Expose_Card13"
    if Expose_Guess1 == 13:
        Expose_Card14 = 3
        print "Expose_Card14"
    if Expose_Guess1 == 14:
        Expose_Card15 = 3
        print "Expose_Card15"
    if Expose_Guess1 == 15:
        Expose_Card16 = 3
        print "Expose_Card16"

def draw(canvas):
    global Expose_Card1
    
    for i in range(16):
            canvas.draw_text(str(listOfCards[i]), [15+50*i,70], 40, "lime")

    if Expose_Card1 == 1:
        canvas.draw_line([25, 0], [25, 100], 50, 'Green')
    if Expose_Card2 == 1:    
        canvas.draw_line([75, 0], [75, 100], 50, 'Green')
    if Expose_Card3 == 1:
        canvas.draw_line([125, 0], [125, 100], 50, 'Green')
    if Expose_Card4 == 1:
        canvas.draw_line([175, 0], [175, 100], 50, 'Green')
    if Expose_Card5 == 1:
        canvas.draw_line([225, 0], [225, 100], 50, 'Green')
    if Expose_Card6 == 1:
        canvas.draw_line([275, 0], [275, 100], 50, 'Green')
    if Expose_Card7 == 1:
        canvas.draw_line([325, 0], [325, 100], 50, 'Green')
    if Expose_Card8 == 1:
        canvas.draw_line([375, 0], [375, 100], 50, 'Green')
    if Expose_Card9 == 1:
        canvas.draw_line([425, 0], [425, 100], 50, 'Green')
    if Expose_Card10 == 1:
        canvas.draw_line([475, 0], [475, 100], 50, 'Green')
    if Expose_Card11 == 1:
        canvas.draw_line([525, 0], [525, 100], 50, 'Green')
    if Expose_Card12 == 1:
        canvas.draw_line([575, 0], [575, 100], 50, 'Green')
    if Expose_Card13 == 1:
        canvas.draw_line([625, 0], [625, 100], 50, 'Green')
    if Expose_Card14 == 1:
        canvas.draw_line([675, 0], [675, 100], 50, 'Green')
    if Expose_Card15 == 1:
        canvas.draw_line([725, 0], [725, 100], 50, 'Green')
    if Expose_Card16 == 1:
        canvas.draw_line([775, 0], [775, 100], 50, 'Green')
    
    for i in range(16):
            canvas.draw_line([50*(i%15+1),0], [50*(i%15+1),100], 2, "lime")
    
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = " + str(Turn))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

# Always remember to review the grading rubric
