from Constants import *
from Transpiler import *
import math
import collections
import sympy
import itertools

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


def PotentialEnergy(mass: float, height: float, gravitational_acceleration: float = g) -> float:
    return mass * height * gravitational_acceleration


def ElasticPotentialEnergy(spring_constant: float, deformation: float) -> float:
    return (spring_constant * (deformation ** 2)) / 2


def TangentialComponent(force: float, angle: float) -> float:
    return force * Sin(angle)


def NormalComponent(force: float, angle: float) -> float:
    return force * Cos(angle)


def FrictionForce(friction_coefficient: float, mass: float, angle: float = 0, gravitational_acceleration: float = g) -> float:
    return friction_coefficient * mass * Cos(angle) * gravitational_acceleration


def FrictionCoefficient(friction_force: float, mass: float, angle: float = 0, gravitational_acceleration: float = g) -> float:
    return friction_force / (mass * gravitational_acceleration * Cos(angle))


def Integrate(*objects) -> str:
    return str(sympy.integrate(*objects))


def Differentiate(*objects) -> str:
    return str(sympy.diff(*objects))


def Sqrt(number: float) -> float:
    return number ** 0.5


def PrimeQ(integer: int) -> bool:
    if integer == int(integer):
        return sympy.primetest.isprime(int(integer))
    else:
        raise TypeError("Unable to run a primality test on the given argument")


def CompositeQ(integer: int) -> bool:
    return not PrimeQ(integer)


def PrimePi(number: float) -> int:
    return sympy.ntheory.generate.primepi(number)


def PrimeFac(integer: int) -> list:
    if integer == int(integer):
        result = []
        for factor, exponent in sympy.ntheory.factor_.factorint(int(integer)).items():
            result.extend([factor] * exponent)
        return result
    else:
        raise TypeError("Unable to factorize the given argument")


def FullPrimeFac(integer: int) -> list:
    if integer == int(integer):
        return list(map(list, sympy.ntheory.factor_.factorint(int(integer)).items()))
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


def Filter(*objects) -> list:
    return list(filter(*objects))


def Permutations(item: collections.Sequence) -> list:
    perms = list(itertools.permutations(item))
    if isinstance(item, str):
        return list(map("".join, perms))
    return list(map(list, perms))


def Slice(iterable: collections.Sequence, start: int = 0, end: int = 0, step: int = 1) -> collections.Sequence:
    return iterable[start:end or len(iterable):step]


def Range(lower_bound: int, upper_bound: int, step: int = 1) -> list:
    if isinstance(lower_bound, int) and isinstance(upper_bound, int) and isinstance(step, int):
        if lower_bound <= upper_bound:
            return list(range(lower_bound, upper_bound + 1, step))
        else:
            return list(range(upper_bound, lower_bound + 1)[::-1][::step])
    else:
        raise TypeError("Range arguments must all be integers")


def Input() -> object:
    return eval(input())


def Print(*objects, Sep: str = " ", End: str = "\n"):
    result = []
    for element in objects:
        if isinstance(element, list):
            result.append(Transpiler().format_list(element))
        else:
            result.append(element)
    print(*result, sep=Sep, end=End)
