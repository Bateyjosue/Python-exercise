from math import pi

def radian_to_degrees(radian):
    deg = radian * (180 / pi)
    return deg

def degree_to_radian(degree):
    rad = degree * (pi / 180)
    return rad

def Main():
    print(f'1 [deg] is {round(degree_to_radian(1), 3)}[rad]')
    print(f'30 [rad] is {round(radian_to_degrees(30), 2)}[deg]')

if __name__ == '__main__':
    Main()
