# create your solar system animation here!

import turtle
import math


class SolarSystem:
    def __init__(self, height, width):
        self.sun = None
        self.planets = []
        self.window = turtle.Screen()
        self.window.tracer(0)
        self.window.setup(900, 900)
        self.window.bgcolor("black")
        self.sst = turtle.Turtle()
        self.sst.hideturtle()
        self.window.setworldcoordinates(
            -width / 2.0, -height / 2.0, width / 2.0, height / 2.0
        )

    def add_planet(self, planet):
        self.planets.append(planet)

    def add_sun(self, sun):
        self.sun = sun

    def show_planets(self):
        for planet in self.planets:
            print(planet.name)

    def freeze(self):
        self.sst.exitOnClick()

    def move_planets(self):
        G = 0.1
        dt = 0.0005

        for p in self.planets:
            p.move_to(p.x + dt * p.x_vel, p.y + dt * p.y_vel)

            rx = self.sun.x - p.x
            ry = self.sun.y - p.y
            r = math.sqrt(rx ** 2 + ry ** 2)

            x_accel = G * self.sun.mass * rx / r ** 3
            y_accel = G * self.sun.mass * ry / r ** 3

            p.x_vel += dt * x_accel
            p.y_vel += dt * y_accel


class Sun:
    def __init__(self, name, radius, mass, temp):
        self.name = name
        self.radius = radius
        self.mass = mass
        self.temp = temp
        self.x = 0
        self.y = 0

        self.st = turtle.Turtle()
        self.st.up()
        self.st.goto(self.x, self.y)
        self.st.down()
        self.st.color("yellow")
        self.st.begin_fill()
        self.st.shape("circle")
        self.st.shapesize(radius, radius, 1)
        # self.st.circle(radius)
        self.st.end_fill()


class Planet:
    def __init__(self, name, radius, mass, distance, x_vel, y_vel, color):
        self.name = name
        self.radius = radius
        self.mass = mass
        self.distance = distance
        self.x = distance
        self.y = 0
        self.color = color

        self.x_vel = x_vel
        self.y_vel = y_vel

        self.t = turtle.Turtle()
        self.t.up()
        self.t.goto(self.x, self.y)
        self.t.down()
        self.t.color(color)
        self.t.begin_fill()
        self.t.shape("circle")
        self.t.shapesize(radius, radius, 1)
        # self.t.circle(radius)
        self.t.end_fill()

    def move_to(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        self.t.up()
        self.t.goto(self.x, self.y)
        self.t.down()


def create_animate():
    ss = SolarSystem(2, 2)

    sun = Sun("SUN", 1, 25, 5800)
    ss.add_sun(sun)

    planet = Planet("MERCURY", 2, 1000, 0.7, -0.5, 0.5, "blue")
    ss.add_planet(planet)

    planet_2 = Planet("EARTH", 4, 5000, 0.8, -0.5, 0.6, "green")
    ss.add_planet(planet_2)

    planet_3 = Planet("JUPITER", 8, 8000, 1, -0.5, 0.8, "brown")
    ss.add_planet(planet_3)

    while True:
        ss.move_planets()
        ss.window.update()


# i couldn't get ontimer to work for the life of me :(


#    ss.move_planets()
#    ss.window.ontimer(create_animate, 500)
#    ss.window.update()
#    ss.window.exitonclick()


# ss.window.mainloop()

create_animate()
