from appJar import gui
from random import *

app=gui()
app.addLabel("title", "Generar contraseña aleatoria")
app.addLabelEntry("Palabra")
app.addLabel("passw", "")

def rand():
    p=app.getEntry("Palabra")
    p=p.replace(" ", "")
    if len(p)>4:
        t=sample(p, 4)
        q=""
        for i in t:
            q=q+i
    else: q=p
    app.setLabel("passw",q+str(randint(1000, 9999)))
    
app.addButton("GetPass", rand)
app.go()
