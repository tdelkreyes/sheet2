from gasp import *
def draw():
    begin_graphics()
    Circle((300, 200), 100)
    Circle((265, 220), 15)
    Circle((335, 220), 15)
    Arc((300, 200), 60, 225, 315)
    Line((300, 220), (280, 180))
    Line((280, 180), (320, 180))
draw()
update_when('key_pressed')
end_graphics()