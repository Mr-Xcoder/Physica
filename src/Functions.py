from Constants import *
from Transpiler import *
import math
import collections
import sympy
import itertools
import sys

sys.setrecursionlimit(10 ** 9)

DegToRad = math.radians
RadToDeg = math.degrees
Ord = ord
Chr = chr
Any = any
All = all
Sum = sum


def Sin(deg: float) -> float:
    return math.sin(DegToRad(deg))


def Cos(deg: float) -> float:
    return math.cos(DegToRad(deg))


def Tan(deg: float) -> float:
    return math.tan(DegToRad(deg))


def Cot(deg: float) -> float:
    return 1 / Tan(deg)


def Sec(deg: float) -> float:
    return 1 / Cos(deg)


def Csc(deg: float) -> float:
    return 1 / Sin(deg)


def Sinh(deg: float) -> float:
    return math.sinh(DegToRad(deg))


def Cosh(deg: float) -> float:
    return math.cosh(DegToRad(deg))


def Tanh(deg: float) -> float:
    return math.tanh(DegToRad(deg))


def Coth(deg: float) -> float:
    return 1 / Tanh(deg)


def Sech(deg: float) -> float:
    return 1 / Cosh(deg)


def Csch(deg: float) -> float:
    return 1 / Sinh(deg)


def Arcsin(sine: float) -> float:
    return RadToDeg(math.asin(sine))


def Arccos(cosine: float) -> float:
    return RadToDeg(math.acos(cosine))


def Arctan(tangent: float) -> float:
    return RadToDeg(math.atan(tangent))


def Arccot(cotangent: float) -> float:
    return RadToDeg(math.atan(1 / cotangent))


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


def Permutations(item: collections.Iterable) -> list:
    perms = list(itertools.permutations(item))
    if isinstance(item, str):
        return list(map("".join, perms))
    return list(map(list, perms))


def Join(item: collections.Iterable, separator: object) -> collections.Iterable:
    if isinstance(separator, str) and all(isinstance(element, str) for element in item):
        return separator.join(map(str, item))
    result = []
    for index, element in enumerate(item):
        result.append(element)
        if index != len(item) - 1:
            result.append(separator)
    return result


def Slice(iterable: collections.Sequence, start: int = 0, end: int = 0, step: int = 1) -> collections.Sequence:
    return iterable[start:end or len(iterable):step]


def Range(lower_bound: int, upper_bound: int, step: int = 1) -> list:
    if isinstance(lower_bound, int) and isinstance(upper_bound, int) and isinstance(step, int):
        if lower_bound <= upper_bound:
            return list(range(lower_bound, upper_bound + 1, step))
        return []
    else:
        raise TypeError("Range arguments must all be integers")


def Input() -> object:
    inp = input()
    try:
        return eval(inp)
    except (NameError, SyntaxError):
        try:
            return Transpiler().unformat_list(inp)
        except:
            return inp


def STDIN() -> list:
    return sys.stdin.read().split("\n")


def ARGV() -> list:
    return sys.argv[1:]


def String(item: object) -> str:
    return str(item)


def Element(item: collections.Sequence, index: int) -> object:
    return item[(index - 1) % len(item)]


def Print(*objects, Sep: str = " ", End: str = "\n"):
    result = []
    for element in objects:
        if isinstance(element, list):
            result.append(Transpiler().format_list(element))
        else:
            result.append(element)
    print(*result, sep=Sep, end=End)


def Evaluate(item: str) -> object:
    try:
        return Transpiler().unformat_list(item)
    except:
        return eval(item)


def Length(item: object) -> object:
    if isinstance(item, int):
        return len(str(abs(item)))
    elif isinstance(item, collections.Sequence):
        return len(item)
    else:
        raise TypeError("The given arguments do not match any overloads for 'Length'")


def Round(number: float, number_of_decimals: int = 0) -> float:
    return round(number, number_of_decimals)


def Max(item: collections.Iterable) -> object:
    return max(item)


def Min(item: collections.Iterable) -> object:
    return min(item)


def Zip(object: list, filler: object = None) -> list:
    import itertools
    return list(map(list, itertools.zip_longest(*object, fillvalue=filler)))


def Gamma(number: float) -> float:
    return math.gamma(number)


def Abs(number: float) -> float:
    return abs(number)


def FromBase(digital_representation: list, base: int) -> int:
    result = 0
    for digit in digital_representation:
        result = base * result + digit
    return result


def Base(number: int, base: int) -> list:
    if number == 0:
        return [0]
    result = []
    while number > 0:
        result = [number % base] + result
        number //= base
    return result


def Flatten(item: list) -> list:
    flat = []
    if isinstance(item, list):
        for element in item:
            flat += Flatten(element)
    else:
        flat.append(item)
    return flat


def NumericQ(item: object) -> bool:
    return isinstance(item, int) or isinstance(item, float)


def CharQ(item: object) -> bool:
    return isinstance(item, str) and len(item) == 1


def Deltas(item: collections.Sequence) -> list:
    return [y - x if NumericQ(x) and NumericQ(y) else (ord(y) - ord(x) if CharQ(x) and CharQ(y) else None) for x, y in zip(item, item[1:])]


def Sort(func: callable, item: collections.Sequence, *, Descending: bool = False) -> collections.Sequence:
    return sorted(item, key=func, reverse=Descending)


def Map(func: callable, item: collections.Iterable) -> list:
    return list(map(func, item))


def Filter(func: callable, item: collections.Iterable, *, Negated: bool = False) -> list:
    return list(filter((lambda x: not func(x) if Negated else func(x)), item))
