from winsound import Beep
from time import sleep

def b4(duration):
    Beep(494, duration)

def asharp4(duration):
    Beep(466, duration)

def a4(duration):
    Beep(440, duration)

def gsharp4(duration):
    Beep(415, duration)

def g4(duration):
    Beep(392, duration)

def fsharp4(duration):
    Beep(370, duration)

def f4(duration):
    Beep(349, duration)

def dsharp4(duration):
    Beep(311, duration)

def asharp3(duration):
    Beep(233, duration)

def pause(duration):
    sleep(0.001*duration)

def everything_is_awesome():
    gsharp4(300)
    gsharp4(300)
    gsharp4(300)
    gsharp4(300)
    gsharp4(300)
    g4(800)
    pause(400)
    gsharp4(300)
    gsharp4(300)
    gsharp4(300)
    gsharp4(300)
    gsharp4(600)
    g4(400)
    f4(400)
    dsharp4(400)
    f4(400)
    g4(400)
    f4(800)
    gsharp4(600)
    gsharp4(300)
    gsharp4(300)
    gsharp4(300)
    gsharp4(300)
    asharp4(800)
    pause(400)
    asharp3(300)
    asharp3(300)
    g4(600)
    f4(400)
    f4(400)
    dsharp4(400)
    dsharp4(800)
    
everything_is_awesome()
