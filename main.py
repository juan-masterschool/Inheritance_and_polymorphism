from Universe import *


def main():
    earth = Planet("earth", 6.371e6, 5.972e24, 15, 4.54e9, True)

    moon = Moon("moon", 1.7371e6, 7.342e22, -20, 4.53e9, earth)

    print(moon)
    print(earth)


if __name__ == '__main__':
    main()
