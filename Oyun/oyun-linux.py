import turtle
import random
import math
import os

#sounds settings
sekme= "aplay sekme.wav&"
yemarti = "aplay yemarti.wav&"
yemeksi = "aplay yemeksi.wav&"
buffyem = "aplay buffyem.wav&"
debuffyem= "aplay debuffyem.wav&"
pikseleksi = "aplay pikseleksi.wav&"
pikselarti = "aplay pikselarti.wav&"
bitis = "aplay bitis.wav&"
hızlanma= "aplay hızlanma.wav&"
yavaslama= "aplay yavaslama.wav&"


#create the ints.
speedp1=7
speedp2=7
boyut1=1
boyut2=1

print("Competetive mode: White point +1 score, yellow buff %30 chance to +2 score,%30 chance to -2 score,%20 chance to increase your speed, %20 chance to reduce your speed\n")
print("Chaos mode:White point +1 score, yellow buff %30 chance to grow up, %30 chance to become smaller, %20 chance to extremely increase the speed of your rival, %20 chance to extremely reduce the speed of your rival\n")    
secenek=int(input("For the competetive mode press 1. For the chaos mode press 2\n:"))

#create screen
ekran=turtle.Screen()
ekran.bgcolor("black")
ekran.title("TURTLE WARS")

#create border
sınırcı=turtle.Turtle()
sınırcı.penup()
sınırcı.setposition(-350,-350)
sınırcı.pendown()
sınırcı.pensize(2)
sınırcı.pencolor("white")
for sınır in range(4):
    sınırcı.speed(700)
    sınırcı.forward(700)
    sınırcı.left(90)
sınırcı.hideturtle()  
#create player 1
player1=turtle.Turtle()                   
player1.turtlesize(1)
player1.color("blue")
player1.shape("turtle")
player1.penup()
player1.speed(0)
score_player1=0

#create player 2
player2=turtle.Turtle()
player2.turtlesize(1)
player2.color("light green")
player2.shape("turtle")
player2.penup()
player2.speed(0)
score_player2=0

scoreboardfinish=turtle.Turtle()
scoreboardfinish.setposition(-85,355)
scoreboardfinish.pencolor("white")
scoreboardfinish.hideturtle()

scoreboardp1=turtle.Turtle()
scoreboardp1.setposition(-420,0)
scoreboardp1.pencolor("white")
scoreboardp1.hideturtle()

scoreboardp2=turtle.Turtle()
scoreboardp2.setposition(400,0)
scoreboardp2.pencolor("white")
scoreboardp2.hideturtle()

#create goal
yem=turtle.Turtle()
yem.turtlesize(0.5)
yem.color("white")
yem.shape("circle")
yem.penup()
yem.speed(0)
yem.setposition(random.randint(-345,345),random.randint(-345,345))

#create buff
buff=turtle.Turtle()
buff.turtlesize(0.5)
buff.color("yellow")
buff.shape("circle")
buff.penup()
buff.speed(0)
buff.setposition(random.randint(-345,345),random.randint(-345,345))

#mouvment functions
def sagp1():
    player1.right(30)
def sagp2():
    player2.right(30)
def solp1():
    player1.left(30)
def solp2():
    player2.left(30)

#key-function configrations
turtle.listen()
turtle.onkey(sagp1,"Right")
turtle.onkey(sagp2,"d")
turtle.onkey(solp1,"Left")
turtle.onkey(solp2,"a")
turtle.onkey(solp2,"A")
turtle.onkey(sagp2,"D")

FONTSIZE =10

FONT = ('Arial', FONTSIZE, 'normal')
scoreboardp1.write("Player 1\nScore: {} \nSpeed: {}".format(score_player1,speedp1),font=FONT)
scoreboardp2.write("Player 2\nScore: {} \nSpeed: {}".format(score_player2,speedp2),font=FONT)
while (secenek==1):
    player1.forward(speedp1)
    player2.forward(speedp2)
    if player1.xcor()>345 or player1.xcor()<-345:
        player1.right(179)
        os.system(sekme)
    if player2.xcor()>345 or player2.xcor()<-345:
        player2.right(179)
        os.system(sekme)
    if player1.xcor()>349 and player1.xcor()<-349:
        player1.right(179)
        os.system(sekme)
    if player2.xcor()>349 and player2.xcor()<-349:
        player2.right(179)
        os.system(sekme)
    if player1.ycor()>345 or player1.ycor()<-345:
        player1.right(179)
        os.system(sekme)
    if player2.ycor()>345 or player2.ycor()<-345:
        player2.right(179)
        os.system(sekme)
    if player1.ycor()>349 and player1.ycor()<-349:
        player1.right(179)
        os.system(sekme)
    if player2.ycor()>349 and player2.ycor()<-349:
        player2.right(179)
        os.system(sekme)
        
    #yeme göre pozisyon
    uzaklık1= math.hypot(player1.xcor()-yem.xcor() ,player1.ycor()-yem.ycor() )
    if uzaklık1<20:
             
            score_player1+=1
            os.system(yemarti)    
            yem.setposition(random.randint(-345,345),random.randint(-345,345))
            scoreboardp1.clear()
            scoreboardp1.write("Player 1\nScore: {} \nSpeed: {}".format(score_player1,speedp1),font=FONT)
            
   
    uzaklık2= math.hypot(player2.xcor()-yem.xcor() ,player2.ycor()-yem.ycor() )
    if uzaklık2<20:
            score_player2+=1
            os.system(yemarti)     
            yem.setposition(random.randint(-345,345),random.randint(-345,345))
            scoreboardp2.clear()
            scoreboardp2.write("Player 2\nScore: {} \nSpeed: {}".format(score_player2,speedp2),font=FONT)
    #buffa göre pozisyon
    uzaklık3= math.hypot(player1.xcor()-buff.xcor() ,player1.ycor()-buff.ycor() )
    if uzaklık3<20:
            b=random.randint(0,6)
            if(b<=1):
                speedp1+=0.50
                os.system(hızlanma) 
            if(b>=5):
                speedp1-=0.30
                os.system(yavaslama) 
            if(b>1 and b<=3):
                score_player1+=2
                os.system(buffyem) 
            if(b>3 and b<5):
                score_player1-=2
                os.system(debuffyem) 
            scoreboardp1.clear()
            scoreboardp1.write("Player 1\nScore: {} \nSpeed: {}".format(score_player1,speedp1),font=FONT)
            buff.setposition(random.randint(-345,345),random.randint(-345,345))
            
    uzaklık4= math.hypot(player2.xcor()-buff.xcor() ,player2.ycor()-buff.ycor() )
    if uzaklık4<20:
            b=random.randint(0,6)
            if(b<=1):
                speedp2+=0.50
                os.system(hızlanma) 
            if(b>=5):
                speedp2-=0.25                   
                os.system(yavaslama) 
            if(b>1 and b<=3):
                score_player2+=2
                os.system(buffyem) 
            if(b>3 and b<5):
                score_player2-=2
                os.system(debuffyem) 
            scoreboardp2.clear()
            scoreboardp2.write("Player 2\nScore: {} \nSpeed: {}".format(score_player2,speedp2),font=FONT)       
            buff.setposition(random.randint(-345,345),random.randint(-345,345))                
            
            
    if(score_player1>=20):
        os.system(bitis) 
        scoreboardfinish.reset()
        scoreboardfinish.setposition(-85,0)
        scoreboardfinish.pencolor("white")
        scoreboardfinish.write("PLAYER 1: {}    PLAYER2: {} \n  PLAYER 1 WON!".format(score_player1,score_player2))
        scoreboardfinish.hideturtle()
        
        break;
    if(score_player2>=20):
        os.system(bitis) 
        scoreboardfinish.reset()
        scoreboardfinish.setposition(-85,0)
        scoreboardfinish.pencolor("white")
        scoreboardfinish.write("PLAYER 1: {}    PLAYER2: {} \n  PLAYER 2 WON!".format(score_player1,score_player2))
        scoreboardfinish.hideturtle()
        break;
    
while (secenek==2):  
    player1.forward(speedp1)
    player2.forward(speedp2)
    if player1.xcor()>345 or player1.xcor()<-345:
        player1.right(179)
        os.system(sekme)
    if player2.xcor()>345 or player2.xcor()<-345:
        player2.right(179)
        os.system(sekme)
    if player1.xcor()>349 and player1.xcor()<-349:
        player1.right(179)
        os.system(sekme)
    if player2.xcor()>349 and player2.xcor()<-349:
        player2.right(179)
        os.system(sekme)
    if player1.ycor()>345 or player1.ycor()<-345:
        player1.right(179)
        os.system(sekme)
    if player2.ycor()>345 or player2.ycor()<-345:
        player2.right(179)
        os.system(sekme)
    if player1.ycor()>349 and player1.ycor()<-349:
        player1.right(179)
        os.system(sekme)
    if player2.ycor()>349 and player2.ycor()<-349:
        player2.right(179)
        os.system(sekme)
    #yeme göre pozisyon
    uzaklık1= math.hypot(player1.xcor()-yem.xcor() ,player1.ycor()-yem.ycor() )
    if uzaklık1<20:
            
            score_player1+=1
            os.system(yemarti)     
            yem.setposition(random.randint(-345,345),random.randint(-345,345))
            scoreboardp1.clear()
            scoreboardp1.write("Player 1\nScore: {} \nSpeed: {}".format(score_player1,speedp1),font=FONT)
            
   
    uzaklık2= math.hypot(player2.xcor()-yem.xcor() ,player2.ycor()-yem.ycor() )
    if uzaklık2<20:
            score_player2+=1
            os.system(yemarti) 
                
            yem.setposition(random.randint(-345,345),random.randint(-345,345))
            scoreboardp2.clear()
            scoreboardp2.write("Player 2\nScore: {} \nSpeed: {}".format(score_player2,speedp2),font=FONT)
    #buffa göre pozisyon
    uzaklık3= math.hypot(player1.xcor()-buff.xcor() ,player1.ycor()-buff.ycor() )
    if uzaklık3<20:
            b=random.randint(0,6)
            if(b<=1):
                speedp2+=1.5
                os.system(hızlanma) 
            if(b>=5):
                speedp2-=1
                os.system(yavaslama)
                 
            if(b>1 and b<=3):
                if(boyut1<5):
                    boyut1+=0.50
                    os.system(pikselarti)
                    player1.turtlesize(boyut1)
            if(b>3 and b<5):
                if(boyut1>0.50):
                    boyut1-=0.25
                    os.system(piksel-)
                    player1.turtlesize(boyut1)
            
            scoreboardp2.clear()
            scoreboardp2.write("Player 2\nScore: {} \nSpeed: {}".format(score_player2,speedp2),font=FONT)
            buff.setposition(random.randint(-345,345),random.randint(-345,345))
            
    uzaklık4= math.hypot(player2.xcor()-buff.xcor() ,player2.ycor()-buff.ycor() )
    if uzaklık4<20:
            b=random.randint(0,6)
            if(b<=1):
                speedp1+=1.5
                os.system(hızlanma)
            if(b>=5):
                speedp1-=1
                os.system(yavaslama)
            if(b>1 and b<=3):
                if(boyut2<5):
                    boyut2+=0.50
                    os.system(pikselarti)
                    player2.turtlesize(boyut2)
                
            if(b>3 and b<5):
                if(boyut2>0.50):
                    boyut2-=0.25
                    os.system(pikseleksi)
                    player2.turtlesize(boyut2)
                    
            scoreboardp1.clear()
            scoreboardp1.write("Player 1\nScore: {} \nSpeed: {}".format(score_player1,speedp1),font=FONT)        
            buff.setposition(random.randint(-345,345),random.randint(-345,345))                
            
            
    if(score_player1>=20):
        os.system(bitis)
        scoreboardfinish.reset()
        scoreboardfinish.setposition(-85,0)
        scoreboardfinish.pencolor("white")
        scoreboardfinish.write("PLAYER 1: {}    PLAYER2: {} \n  PLAYER 1 WON!".format(score_player1,score_player2))
        scoreboardfinish.hideturtle()
        
        break;
    if(score_player2>=20):
        os.system(bitis)
        scoreboardfinish.reset()
        scoreboardfinish.setposition(-85,0)
        scoreboardfinish.pencolor("white")
        scoreboardfinish.write("PLAYER 1: {}    PLAYER2: {} \n  PLAYER 2 WON!".format(score_player1,score_player2))
        scoreboardfinish.hideturtle()
        break;
   

    

    
    
    
    



