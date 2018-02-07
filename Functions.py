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


def PotentialEnergy(mass: float, height: float, gravitationAcceleration: float = g) -> float:
    return mass * height * gravitationAcceleration


def ElasticPotentialEnergy(springConstant: float, deformation: float) -> float:
    return (springConstant * (deformation ** 2)) / 2


def TangentialComponent(force: float, angle: float) -> float:
    return force * Sin(angle)


def NormalComponent(force: float, angle: float) -> float:
        return force * Cos(angle)


def FrictionForce(frictionCoefficient: float, mass: float, angle : float = 0, gravitationAcceleration: float = g) -> float:
    return frictionCoefficient * mass * Cos(angle) * gravitationAcceleration


def Print(*objects, Sep : str = " ", End : str = "\n"):
    print(*objects, sep = Sep, end = End)
