from gasp import *
begin_graphics()
Circle((300, 200), 150, color="blue", filled=False, thickness=10)
Circle((265, 220), 35)
Circle((335, 220), 35)
Arc((300, 200), 60, 225, 315)
Line((300, 220), (280, 180))
Line((280, 180), (320, 180))
Circle((265, 220), 10, color="green", filled=True)
Circle((335, 220), 10, color="green", filled=True)

def moan():
    print('Python is useless!')
    print('And so are these worksheets.')

def twice(x):
    print(x, '*', x, 'is', x * x)

def draw_face(x, y):
    Circle((300, 200), 150)
    Circle((265, 220), 15)
    Circle((335, 220), 15)
    Arc((300, 200), 60, 225, 315)
    Line((300, 220), (280, 180))
    Line((280, 180), (320, 180))
    Circle((265, 220), 10)
    Circle((335, 220), 10) 

update_when('key_pressed')
end_graphics()