from Constants import *
import math

DegToRad = math.radians
RadToDeg = math.degrees


def Sin(deg: float) -> float:
    return math.sin(DegToRad(deg))


def Cos(deg: float) -> float:
    return math.cos(DegToRad(deg))


def Tan(deg: float) -> float:
    return math.tan(DegToRad(deg))


def Cot(deg: float) -> float:
    return 1 / math.tan(DegToRad(deg))


def SchwarzschildRadius(mass: float) -> float:
    return (2 * mass * G) / (c ** 2)


def KineticEnergy(mass: float, velocity: float) -> float:
    return (mass * (velocity ** 2)) / 2

def Print(*objects, Sep = " ", End = "\n"):
    print(*objects, sep = Sep, end = End)
