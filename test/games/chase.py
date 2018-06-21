from pyleap import *
import random


def chase(self, hero):
    r = ((hero.x - self.x)**2 + (hero.y-self.y)**2)**0.5
    self.x += self.speed * (hero.x - self.x) / r
    self.y += self.speed * (hero.y - self.y) / r


Sprite.chase = chase

class Monster(Sprite):

    def __init__(self, x=0, y=0):
        src = "https://rss.leaplearner.com/Image/Role/CircleFace.png"
        super().__init__(src, x, y)
        self.scale = 0.15
        self.speed = 0.5 + random.random() * 0.5


monsters = []

bg = Sprite("https://rss.leaplearner.com/Image/Bgs/BG.png")
hero = Sprite("https://rss.leaplearner.com/Image/Role/Alien2.png")
hero.scale = 0.3
hero.speed = 5

t = Text("RETRY!", font_size=30)

def add_monster(dt):
    m = Monster()
    monsters.append(m)

def game(dt):
    window.clear()
    hero.chase(mouse)

    bg.draw()
    hero.draw()

    for m in monsters:
        m.chase(hero)
        m.draw()

    for m in monsters:
        if(m.collide(hero)):
            t.draw()
            unschedule(game)
            break

def retry():
    global monsters
    monsters = []
    schedule_interval(game)
    
t.on_press(retry)

schedule_interval(game)
schedule_interval(add_monster, 1)
run()
