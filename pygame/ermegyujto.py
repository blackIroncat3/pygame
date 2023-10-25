
from random import randint
TITLE = "Érmegyűjtő"
HEIGHT = 400
WIDTH = 400
erme = Actor("erme")
roka = Actor("roka")
kezdes = True
szam = 0
lejart = False
limit = 10
next_ = False
ended = False
s = 5
def draw():
    global szam
    if lejart == False:
        screen.fill((40, 150, 40))
        roka.draw()
        erme.draw()
        screen.draw.text(str(limit), center=(30, 30), fontsize = 40, color="#C95C43")
        screen.draw.text(str(szam), center=(200, 380), fontsize = 60, color="#ff0000")
def update():
    global szam
    global kezdes
    roka.pos = roka.x, roka.y
    global lejart
    global s
    global ended
    global limit
    if ended == True and lejart == True and keyboard.f5:
        lejart = False
        ended = False
        szam = 0
        roka.pos = 200, 200
        starter()
        limit = 10
    if lejart == True:
        screen.clear()
        screen.draw.text(f"Ennyi érmét gyűjtöttél: {szam}", center=(200, 200), fontsize=30, color="#72CDCC")
        ended = True
    else:
        if kezdes:
            roka.pos = 200, 200
            kezdes = False
        if keyboard.left and roka.x > 31:
            roka.x -= s
        if keyboard.right and roka.x < (WIDTH - 31):
            roka.x += s
        if keyboard.up and roka.y > 42:
            roka.y -= s
        if keyboard.down and roka.y < (HEIGHT - 42):
            roka.y += s
        if roka.colliderect(erme):
            erme.pos = randint(20, (WIDTH - 20)), randint(20, (HEIGHT - 20))
            szam += 1
def timer():
    global lejart
    lejart = True
    clock.unschedule(timer2)
def timer2():
    global limit
    limit -=1
def starter():
    clock.schedule(timer, 10)
    clock.schedule_interval(timer2, 1)
starter()