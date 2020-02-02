# PARTE 1: Importazione delle librerie

from tkinter import *
import math
import pygame
import random
import time
import numpy as np

g = 9.81
zoom=100

WIDTH, HEIGHT=800, 600
global maxRadius

maxRadius=HEIGHT/20
startingTime=time.time()

def calculate():
    global maxRadius
    pygame.init()
    win=pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Double pendulum')
    
    alpha=float(alphaIn.get())
    beta=float(betaIn.get())
    high=float(highIn.get())
    low=float(lowIn.get())
    massup=float(massupIn.get())
    MasInf=float(MasInfIn.get())
    Prec=time.time()-startingTime
    
    dbeta=beta/Prec
    dalpha=alpha/Prec
    Vecchio=time.time()
    zoom=0.9*(HEIGHT/2)/(high+low)
    execution=True
    while execution:
        if (alpha>=0):
            alpha=alpha-2*math.ceil(alpha/(2*np.pi))*np.pi
        if(beta>=0):
            beta=beta-2*math.ceil(beta/(2*np.pi))*np.pi
        if (alpha<0):
            alpha=alpha+-2*int(alpha/(2*np.pi))*np.pi
        if(beta<0):
            beta=beta-2*int(beta/(2*np.pi))*np.pi

        Prec=time.time()-Vecchio
        Vecchio=time.time()
        mu = 1+massup/MasInf

        d2alpha=(g*(np.sin(beta)*np.cos(alpha-beta)-mu*np.sin(alpha))-(low*dbeta*dbeta+high*dalpha*dalpha*np.cos(alpha-beta))*np.sin(alpha-beta))/(high*(mu-np.cos(alpha-beta)*np.cos(alpha-beta)))
        d2beta=(mu*g*(np.sin(alpha)*np.cos(alpha-beta)-np.sin(beta))+(mu*high*dalpha*dalpha+low*dbeta*dbeta*np.cos(alpha-beta))*np.sin(alpha-beta))/(low*(mu-np.cos(alpha-beta)*np.cos(alpha-beta)))

        dalpha=dalpha+d2alpha*Prec
        dbeta=dbeta+d2beta*Prec
        alpha=alpha+dalpha*Prec
        beta=beta+dbeta*Prec

        if (alpha>=0):
            alpha=alpha-2*math.ceil(alpha/(2*np.pi))*np.pi
        if(beta>=0):
            beta=beta-2*math.ceil(beta/(2*np.pi))*np.pi
        if (alpha<0):
            alpha=alpha-2*int(alpha/(2*np.pi))*np.pi
        if(beta<0):
            beta=beta-2*int(beta/(2*np.pi))*np.pi
            
        l1=high*zoom
        l2=low*zoom
        alphaX=l1*np.sin(alpha)+abs(WIDTH/2)
        alphaY=l1*np.cos(alpha)+abs(HEIGHT/2)
        betaX=alphaX+l2*np.sin(beta)
        betaY=alphaY+l2*np.cos(beta)
        
        win.fill((0,0,0))
        
        radius1=3*massup/(4*math.pi)
        radius2=3*MasInf/(4*math.pi)
        
        radiushigh=max(radius1, radius2)
        
        zoomP=radiushigh/maxRadius
        
        radius1=radius1/zoomP
        radius2=radius2/zoomP
        
        pygame.draw.line(win, (255, 255, 255), (0, HEIGHT/2),(WIDTH/2, HEIGHT/2), 1)
        pygame.draw.line(win, (255, 0, 0),(WIDTH/2, HEIGHT/2),(alphaX, alphaY), 1)
        pygame.draw.line(win, (255, 255, 255),(alphaX,alphaY),(betaX, betaY), 1)
        pygame.draw.circle(win, (255,0,0),(int(alphaX), int(alphaY)),int(radius1), 0)
        pygame.draw.circle(win, (255,255,255),(int(betaX), int(betaY)),int(radius2), 0)
        pygame.display.flip()
        
        # Chiusura del programma
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                execution=False
                pygame.quit()

# PARTE 2: Input

data = Tk()
data.title("Settings")
data.minsize(height=295, width=400)
data.maxsize(height=295, width=400)

alphaEt=Label(data, text="\nAngle 1:").pack()
alphaIn=Entry(data)
alphaIn.pack()

betaEt=Label(data, text="Angle 2:").pack()
betaIn=Entry(data)
betaIn.pack()

highEt=Label(data, text="First pendulum length:").pack()
highIn=Entry(data)
highIn.pack()

lowEt=Label(data, text="Second pendulum length:").pack()
lowIn=Entry(data)
lowIn.pack()

massupEt=Label(data, text="First mass:").pack()
massupIn=Entry(data)
massupIn.pack()

MasInfEt=Label(data, text="Second mass:").pack()
MasInfIn=Entry(data)
MasInfIn.pack()

button=Button(data, text="Calculate", command=calculate)
button.pack(pady=10)

data.mainloop()