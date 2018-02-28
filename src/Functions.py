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
Set = set
Int = int
List = list
String = str
Conjugate = complex.conjugate
Sequence = collections.Sequence
Enumerate = enumerate


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
        return Root(number) == int(Root(number))
    else:
        return False


def Root(base: float, root: float = 2) -> float:
    return base ** (1 / root)


def Permutations(collection: collections.Iterable) -> list:
    perms = list(itertools.permutations(collection))
    if isinstance(collection, str):
        return list(map("".join, perms))
    return list(map(list, perms))


def Join(collection: collections.Iterable, separator: object) -> collections.Iterable:
    if isinstance(separator, str) and all(isinstance(element, str) for element in collection):
        return separator.join(map(str, collection))
    result = []
    for index, element in enumerate(collection):
        result.append(element)
        if index != len(collection) - 1:
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


def Element(collection: collections.Sequence, index: int) -> object:
    return collection[(index - 1) % len(collection)]


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


def Max(collection: collections.Iterable) -> object:
    return max(collection)


def Min(collection: collections.Iterable) -> object:
    return min(collection)


def Fst(collection: collections.Sequence) -> object:
    return collection[0]


def Lst(collection: collections.Sequence) -> object:
    return collection[-1]


def RunLengthEncode(collection: collections.Iterable) -> collections.Iterable:
    return [(len(list(y)), x) for x, y in itertools.groupby(collection)]


def RunLengthDecode(encoded: list) -> collections.Iterable:
    result = []
    for pair in encoded:
        result.extend(pair[0] * [pair[1]])
    return result


def Group(collection: collections.Sequence) -> list:
    return [Indices(collection, element) for element in Deduplicate(collection)]


def Zip(object: list, filler: object = None) -> list:
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


def Flatten(collection: list) -> list:
    flat = []
    if isinstance(collection, list):
        for element in collection:
            flat += Flatten(element)
    else:
        flat.append(collection)
    return flat


def NumericQ(item: object) -> bool:
    return isinstance(item, int) or isinstance(item, float)


def CharQ(item: object) -> bool:
    return isinstance(item, str) and len(item) == 1


def Deltas(collection: collections.Sequence) -> list:
    return [y - x if NumericQ(x) and NumericQ(y) else (ord(y) - ord(x) if CharQ(x) and CharQ(y) else None) for x, y in zip(collection, collection[1:])]


def Deduplicate(collection: collections.Sequence) -> collections.Sequence:
    result = []
    for element in collection:
        if element not in result:
                result.append(element)
    return "".join(result) if isinstance(collection, str) else result


def Indices(collection: collections.Sequence, element: object) -> list:
    indices = []
    for index, elem in enumerate(collection):
        if elem == element:
            indices.append(index + 1)
    return indices


def Reshape(collection: list, shape: collections.Iterable) -> object:
    import numpy
    return list(map(list, numpy.reshape(collection, shape)))


def Powerset(collection: collections.Iterable) -> list:
    listify = list(collection)
    return list(map(list,itertools.chain.from_iterable(itertools.combinations(listify, r) for r in range(1, len(listify)+1))))


def Split(collection: collections.Sequence, element: object) -> list:
    result = [[]]
    for elem in collection:
        if elem == element:
            result.append([])
        else:
            result[-1].append(elem)
    return result


def Reverse(collection: collections.Sequence) -> collections.Sequence:
    return collection[::-1]


def Floor(number: float) -> int:
    return int(math.floor(number))


def Ceil(number: float) -> int:
    return int(math.ceil(number))


def ReIm(number: complex) -> tuple:
    return number.real, number.imag


def Sort(func: callable, collection: collections.Sequence, *, Descending: bool = False) -> collections.Sequence:
    return sorted(collection, key=func, reverse=Descending)


def Map(func: callable, collection: collections.Iterable) -> list:
    return list(map(func, collection))


def Filter(func: callable, collection: collections.Iterable, *, Negated: bool = False) -> list:
    return list(filter((lambda x: not func(x) if Negated else func(x)), collection))


def Reduce(func: callable, collection: collections.Iterable) -> collections.Iterable:
    from functools import reduce
    return reduce(func, collection)
