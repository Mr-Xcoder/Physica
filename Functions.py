from Constants import *
import math
import collections


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


def Sec(deg: float) -> float:
    return 1 / Cos(deg)


def Csc(deg: float) -> float:
    return 1 / Sin(deg)


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


def FrictionCoefficient(frictionForce: float, mass: float, angle: float = 0, gravitationAcceleration: float = g) -> float:
    return frictionForce / (mass * gravitationAcceleration * Cos(angle))


def Integrate(*objects) -> str:
    return str(__import__("sympy").integrate(*objects))


def Differentiate(*objects) -> str:
    return str(__import__("sympy").diff(*objects))


def Sqrt(number: float) -> float:
    return number ** 0.5


def PrimeQ(integer: int) -> bool:
    if integer == int(integer):
        return __import__("sympy").primetest.isprime(int(integer))
    else:
        raise TypeError("Unable to run a primality test on the given argument")


def CompositeQ(integer: int) -> bool:
    return not PrimeQ(integer)


def PrimePi(number: float) -> int:
    return  __import__("sympy").ntheory.generate.primepi(number)


def PrimeFac(integer: int) -> list:
    if integer == int(integer):
        result = []
        for factor, exponent in __import__("sympy").ntheory.factor_.factorint(int(integer)).items():
            result.extend([factor] * exponent)
        return result
    else:
        raise TypeError("Unable to factorize the given argument")


def FullPrimeFac(integer: int) -> list:
    if integer == int(integer):
        return list(map(list,__import__("sympy").ntheory.factor_.factorint(int(integer)).items()))
    else:
        raise TypeError("Unable to factorize the given argument")


def SquareQ(number: float) -> bool:
    if number == int(number):
        return Sqrt(number) == int(Sqrt(number))
    else:
        return False


def Root(base: float, root: float = 2) -> float:
    return base ** (1 / root)


def Map(*objects) -> list:
    return list(map(*objects))


def Slice(iterable: collections.Sized, start: int = 0, end: int = 0, step: int = 1) -> collections.Sized:
    return iterable[start : end or len(iterable) : step]


def Range(lowerBound: int, upperBound: int, step: int = 1):
    if isinstance(lowerBound, int) and isinstance(upperBound, int) and isinstance(step, int):
        if lowerBound <= upperBound:
            return list(range(lowerBound, upperBound + 1, step))
        else:
            return list(range(upperBound, lowerBound + 1)[::-1][::step])
    else:
        raise TypeError("Range arguments must all be integers")


def Print(*objects, Sep : str = " ", End : str = "\n"):
    print(*objects, sep = Sep, end = End)
