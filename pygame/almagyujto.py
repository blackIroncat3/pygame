from random import randint

alma = Actor("alma")
pont = 0

def draw():
    screen.clear()
    alma.x = randint(0, 801)
    alma.y = randint(0, 601)
    alma.draw()
    screen.draw.text(str(pont), (10, 10))
    
def on_mouse_down(pos):
    global pont
    if alma.collidepoint(pos):
        print("Szép lövés!", pos)
        pont += 1
    else:
        print("Elhibáztad!")
        print("Pont:", pont)
        quit()

def jatekvege():
    print("Lejárt az időd!")
    print("Pont:", pont)
    quit()

clock.schedule(jatekvege, 10)