from vpython import *
from random import uniform


class Planet:
    content = []
    gravity_constant = 0.03

    @classmethod
    def update(cls):
        for i in range(len(Planet.content)):
            Planet.content[i].update_pos()
            for j in range(len(Planet.content)):
                if j != i:
                    Planet.content[i].update_speed(Planet.content[j])

    def __init__(self, radius: float, mass: float, pos: vector, speed: vector, col=color.gray(128)):
        self.ball = sphere(pos=pos, radius=radius, color=col)
        self.arrow = arrow(pos=pos, axis=norm(speed))
        self.arrow.opacity = 0.3
        self.mass = mass
        self.speed = speed
        Planet.content.append(self)

    def update_pos(self):
        self.ball.pos += self.speed
        self.arrow.pos += self.speed

    def update_speed(self, other):
        direction = other.ball.pos - self.ball.pos
        n = mag(direction)
        if n != 0:
            self.speed += (Planet.gravity_constant * other.mass / n ** 3) * direction
            self.arrow.axis = norm(self.speed)
            self.arrow.length = 10 * mag(self.speed)

    def __del__(self):
        del self.ball
        del self.arrow
        del self.mass
        del self.speed

scene.width = 2400
scene.height = 1300

sun = Planet(radius=10, mass=1000, pos=vector(0, 0, 0), speed=vector(0, 0, 0), col=color.yellow)


moon = Planet(radius=1, mass=1, pos=vector(140,0 , 0), speed=vector(0, .9,0),col = color.white)
earth= Planet(radius=4, mass=64, pos=vector(130,0 , 0), speed=vector(0,.4,0 ),col = color.blue)
scene.camera.follow(sun.ball)

while True:
    rate(60)
    Planet.update()

