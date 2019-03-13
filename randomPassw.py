from appJar import gui
from random import *
import pyperclip

app=gui()
app.addLabel("title", "Generar contraseña aleatoria")
app.addLabelEntry("Palabra")
app.addLabel("passw", "")

def rand():
    p=app.getEntry("Palabra")
    p=p.replace(" ", "")
    q=""
    if len(p)>4:
        t=sample(p, 4)
        for i in t:
            q=q+i
    else: q=p
    s=randint(0,1)
    if s==0:    
        q=q+str(randint(1000, 9999))
    elif s==1:
        q=str(randint(1000, 9999))+q

    app.setLabel("passw",q)
    pyperclip.copy(q)
    
    
app.addButton("GetPass", rand)
app.go()
