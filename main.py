from Universe import *


def main():

    sun = Star("Sun", 6.9634e8, 1.989e30, 5505, 4.6e9)
    earth = Planet("Earth", 6.371e6, 5.972e24, 15, 4.54e9, True, sun)
    moon = Moon("Moon", 1.7371e6, 7.342e22, -20, 4.53e9, earth)

    print(f"{earth.name} class: {earth}")
    print(f"{earth.name} host: {earth.get_host()}\n")

    print(f"{moon.name} class: {moon}")
    print(f"{moon.name} host: {moon.get_host()}\n")

    print(f"{sun.name} class: {sun}")
    print(f"{sun.name} host: {sun.get_host()}\n")


if __name__ == '__main__':
    main()
