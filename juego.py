import turtle
import time
from turtle import *
import random
turtle.bye()
posponer = 0.1


  

class ventana():
    global imaBobEsp, imaMedusa
    imaBobEsp = "bob esponja.gif" 
    imaMedusa = "medusa.gif"
    
     
    def __init__(self, width, height, title, NivelJuego1):
         
        self.NivelJuego = NivelJuego1
        self.width = width
        self.height = height
        self.title = title
        self.ventana = turtle.Screen()
        self.ventana.title(title)
        self.ventana.setup(width=self.width, height=self.height)
        if self.NivelJuego == 1:
            self.ventana.bgpic("FONDO DE BIKINI.gif")
        elif self.NivelJuego == 2:
            self.ventana.bgpic("fondo_N2.gif")
        self.ventana.addshape(imaBobEsp)
        self.ventana.addshape(imaMedusa)
             

class jugador():
     
    
    def __init__(self, xcor, ycor, width=20, height=20):
    
        
        self.xcor = xcor
        self.ycor = ycor
        self.width = width
        self.height = height
        self.jugador = turtle.Turtle()       
        self.jugador.speed(0)
        self.jugador.shape(imaBobEsp)
        self.jugador.penup()
        self.jugador.goto(self.xcor, self.ycor)
        self.jugador.direction = "stop"
       
        
        
#FUNCIONES

    def jugador_arriba(self):
         
        y = self.jugador.ycor()
        y += 50
        self.jugador.sety(y)
        
    def jugador_abajo(self):
         
        y = self.jugador.ycor()
        y -= 50
        self.jugador.sety(y)
        
    def jugador_izquierda(self):
         
        x = self.jugador.xcor()
        x  -= 50
        self.jugador.setx(x)
    

    def jugador_derecha(self):
         
        x = self.jugador.xcor()
        x  += 50
        self.jugador.setx(x)     

class medusa:
     
    def __init__(self,  vy=10, xcor=0, ycor=0):
         
        
        self.vy = vy
        self.xcor = xcor
        self.ycor = ycor
         
        self.medusa = turtle.Turtle()
        self.medusa.speed(0)
        self.medusa.shape(imaMedusa)
        self.medusa.penup()
        self.medusa.goto(self.xcor, self.ycor)

class puntaje:
         
    score = 0
    high_score = 0
     
    def __init__(self, color, xcor, ycor):
        self.color = color
        self.xcor = xcor
        self.ycor = ycor
        
        self.puntaje = turtle.Turtle()
        self.puntaje.speed(0)
        self.puntaje.color(self.color)
        self.puntaje.penup()
        self.puntaje.goto(self.xcor, self.ycor)
        self.puntaje.hideturtle()
        self.puntaje.write("Level: 1      Score : 0      High Score: 0", align="center", font=("Arial", 20, "normal"))    



vent = ventana(600, 600, "Atrapa Medusas",1)
jug = jugador( 0, -260)
med = medusa(vy=10)
s =  puntaje("black", 0, 260)

    
# TECLADO
vent.ventana.listen()
vent.ventana.onkeypress(jug.jugador_arriba,"Up")
vent.ventana.onkeypress(jug.jugador_abajo,"Down")
vent.ventana.onkeypress(jug.jugador_izquierda,"Left")
vent.ventana.onkeypress(jug.jugador_derecha,"Right")

SiNivel2 =0 
NivelScore=0       
# TODO LO DEL JUEGO SUCEDE EN EL BUCLE 

#NIVEL 1

while True:
    
    vent.ventana.update()
    med.medusa.sety(med.medusa.ycor() - med.vy)
    
    if SiNivel2 == 2 and NivelScore >= 30:
        vent = ventana(600, 600,"Pong",1)
        SiNivel2 == 3
        NivelScore = 0
        
        
    elif SiNivel2 == 2 and NivelScore < 30:
        SiNivel2 = 0
        vent = ventana(600, 600,"Pong",1)
        med.medusa.showturtle()
    
    
    
    #COLISIONES DE LOS BORDE
    if jug.jugador.xcor() > 280 or jug.jugador.xcor() < -280 or jug.jugador.ycor() > 280 or jug.jugador.ycor()<-280:
        time.sleep(1)
        jug.jugador.goto(0,-260)
        jug.jugador.direction = "stop"
        
        # RESETEAR MARCADOR
        s.score = 0
        s.puntaje.clear()
        s.puntaje.write("Level:1      Score: {}      High Score: {}".format(s.score, s.high_score) ,
                    align = "center" , font = ("Arial", 24 ,"normal"))
        

    # COLISIONES DE COMIDA
    if jug.jugador.distance(med.medusa) < 50:
        x =random.randint(-260, 260)
        y =random.randint(0, 260)
        med.medusa.goto(x,y)   #PARA ACTUALIZAR LA POSISCION 
       
        # AUMENTAR MARCADOR
        
        s.score += 10
        NivelScore = s.score
        if s.score > s.high_score:
            s.high_score = s.score
            
        
        s.puntaje.clear()
        s.puntaje.write("Level:1      Score: {}      High Score: {}".format(s.score, s.high_score) ,
                    align = "center" , font = ("Arial", 24 ,"normal"))
 

    if med.medusa.ycor() < -280:
        time.sleep(0.35)
        med.medusa.goto(0,260)
        med.medusa.direction = "stop"
        
        NivelScore = 0
        if SiNivel2 == 1:
            med_1.medusa.hideturtle()
        med.medusa.hideturtle()
        SiNivel2 = 2

    # RESETEAR MARCADOR
        s.score = 0
        s.puntaje.clear()
        s.puntaje.write("Level:1      Score: {}      High Score: {}".format(s.score, s.high_score) ,
                    align = "center" , font = ("Arial", 24 ,"normal"))

#MEDUSA DEL SEGUNDO NIVEL    
        
    if (NivelScore >= 30):
        
        
        if SiNivel2 == 0:
            vent = ventana(600, 600,"Pong",2)
            med_1 = medusa(vy=10)
            
            SiNivel2 = 1
        
        if SiNivel2 == 3:
            vent = ventana(600, 600,"Pong",2)
            SiNivel2 = 1
            
        if SiNivel2 == 1:
            med_1.medusa.sety(med_1.medusa.ycor() - med_1.vy)
            
        if jug.jugador.distance(med_1.medusa) < 50:
            x =random.randint(-260, 260)
            y =random.randint(0, 260)
            med_1.medusa.goto(x,y)
            
            s.score += 10
            NivelScore = s.score
            
            if s.score > s.high_score:
                s.high_score = s.score
               
            s.puntaje.clear()
            s.puntaje.write("Level:2      Score: {}      High Score: {}".format(s.score, s.high_score),
                                align = "center" , font = ("Arial", 24 ,"normal")) 

        
        if med_1.medusa.ycor() < -280:
            time.sleep(0.35)
            med_1.medusa.goto(0,260)
            med_1.medusa.direction = "stop"
            SiNivel2 = 2
            NivelScore = 0
            med_1.medusa.hideturtle()
            med.medusa.hideturtle()
            
    
        # RESETEAR MARCADOR
            s.score = 0
            s.puntaje.clear()
            s.puntaje.write("Level:2      Score: {}      High Score: {}".format(s.score, s.high_score) ,
                        align = "center" , font = ("Arial", 24 ,"normal")) 
        
    time.sleep(posponer)
    
    if NivelScore >=80:
        s.puntaje.clear()
        s.puntaje.write("HAS GANADO... FELICITACIONES",
                        align = "center" , font = ("Arial", 20 ,"normal"))
        med_1.medusa.hideturtle()
        med.medusa.hideturtle()
        break

turtle.exitonclick()

turtle.bye() 