from sympy.solvers import solve
from scipy.special import comb
from typing import Union
from Constants import *
from Parser import *
import collections
import itertools
import sympy
import math
import sys

sys.setrecursionlimit(10 ** 9)

Abs = abs
Any = any
All = all
Chr = chr
Int = int
Ord = ord
Set = set
Dict = dict
List = list
Divmod = divmod
Enumerate = enumerate
Symbol = sympy.Symbol
DegToRad = math.radians
RadToDeg = math.degrees
Conjugate = complex.conjugate
Sequence = collections.Sequence



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



def ARGV() -> list:
    return sys.argv[1:]


def Base(number: int, base: int) -> list:
    if number == 0:
        return [0]
    result = []
    while number > 0:
        result = [number % base] + result
        number //= base
    return result


def Binomial(a: int, b: int) -> int:
    return comb(a, b, exact=True)


def CompositeQ(integer: int) -> bool:
    return not PrimeQ(integer)


def CharQ(obj: object) -> bool:
    return isinstance(obj, str) and len(obj) == 1


def Ceil(number: float) -> int:
    return int(math.ceil(number))


def Compare(a: object, b: object) -> int:
    return (a > b) - (a < b)


def Differentiate(*objects) -> str:
    return str(sympy.diff(*objects))


def Deltas(collection: collections.Sequence) -> list:
    return [b - a if NumericQ(a) and NumericQ(b) else
            (ord(b) - ord(a) if CharQ(a) and CharQ(b) else None) for a, b in zip(collection, collection[1:])]


def ElasticPotentialEnergy(spring_constant: float, deformation: float) -> float:
    return (spring_constant * (deformation ** 2)) / 2


def Element(collection: collections.Sequence, index: int) -> object:
    return collection[(index - 1) % len(collection)]


def Evaluate(obj: str) -> object:
    try:
        return Parser().unparse_list(obj)
    except:
        return eval(obj)


def Extrema(collection: collections.Iterable) -> list:
    return [Min(collection), Max(collection)]


def ExtremaIndices(collection: collections.Sequence) -> list:
    return [Indices(collection, Min(collection)), Indices(collection, Max(collection))]


def Expression(equation: str) -> str:
    expression = equation
    for pair in ("÷", "/"), ("[", "("), ("]", ")"), ("{", "("), ("}", ")"):
        expression = expression.replace(*pair)
    if "=" in equation:
        parts = equation.split("=")
        expression = parts[0] + f"- ({parts[1]})"
    non_var_names = " +-*/^!()"
    imp_mul_indices = []
    for index, char in enumerate(expression[:-1]):
        if char not in non_var_names and expression[index + 1] not in non_var_names:
            if not (char.isdigit() and expression[index + 1].isdigit()):
                imp_mul_indices.append(index)
    for position, index in enumerate(imp_mul_indices):
        expression = expression[:index + position + 1] + "*" + expression[index + position + 1:]
    return expression


def FrictionForce(friction_coefficient: float, mass: float, angle: float = 0, grav_acc: float = g) -> float:
    return friction_coefficient * mass * Cos(angle) * grav_acc


def FrictionCoefficient(friction_force: float, mass: float, angle: float = 0, grav_acc: float = g) -> float:
    return friction_force / (mass * grav_acc * Cos(angle))


def FullPrimeFac(integer: int) -> list:
    if integer == int(integer):
        return list(map(list, sympy.ntheory.factor_.factorint(int(integer)).objs()))
    else:
        raise TypeError("Unable to factorize the given argument")


def Fst(collection: collections.Sequence) -> object:
    return collection[0]


def FromBase(digital_representation: list, base: int) -> int:
    result = 0
    for digit in digital_representation:
        result = base * result + digit
    return result


def Flatten(collection: list) -> list:
    flat = []
    if isinstance(collection, list):
        for element in collection:
            flat += Flatten(element)
    else:
        flat.append(collection)
    return flat


def Floor(number: float) -> int:
    return int(math.floor(number))


def Filter(func: callable, collection: collections.Iterable, *, Negated: bool = False) -> list:
    return list(filter((lambda elem: not func(elem) if Negated else func(elem)), collection))


def Group(collection: collections.Sequence) -> list:
    return [Indices(collection, element) for element in Unique(collection)]


def Gamma(number: float) -> float:
    return math.gamma(number)


def Integrate(*objects) -> str:
    return str(sympy.integrate(*objects))


def Input() -> object:
    inp = input()
    try:
        return eval(inp)
    except (NameError, SyntaxError):
        try:
            return Parser().unparse_list(inp)
        except:
            return inp


def Indices(collection: collections.Sequence, element: object) -> list:
    indices = []
    for index, elem in enumerate(collection):
        if elem == element:
            indices.append(index + 1)
    return indices


def Intersection(a: collections.Sequence, b: collections.Sequence) -> collections.Sequence:
    intersection = [z for z in a if z in b]
    return "".join(intersection) if isinstance(a, str) else intersection


def Join(collection: collections.Iterable, separator: object = None) -> collections.Iterable:
    if separator == None:
            if isinstance(collection, list):
                separator = ""
            else:
                separator = " "
    if isinstance(separator, str) and all(isinstance(element, str) for element in collection):
        return separator.join(map(str, collection))
    result = []
    for index, element in enumerate(collection):
        result.append(element)
        if index != len(collection) - 1:
            result.append(separator)
    return result


def KineticEnergy(mass: float, velocity: float) -> float:
    return (mass * (velocity ** 2)) / 2


def Len(obj: object) -> int:
    if isinstance(obj, int):
        return len(str(abs(obj)))
    elif isinstance(obj, collections.Sequence):
        return len(obj)
    else:
        raise TypeError("The given arguments do not match any overloads for 'Len'")


def Lst(collection: collections.Sequence) -> object:
    return collection[-1]


def Max(collection: collections.Iterable) -> object:
    return max(collection)


def Min(collection: collections.Iterable) -> object:
    return min(collection)


def Map(func: callable, collection: collections.Iterable) -> list:
    return list(map(func, collection))


def NormalComponent(force: float, angle: float) -> float:
    return force * Cos(angle)


def NumericQ(obj: object) -> bool:
    return isinstance(obj, int) or isinstance(obj, float)


def Optimize(equation: str, variable: Union[Symbol, str] = x) -> list:
    derivative = Differentiate(Expression(equation), variable)
    return [str(solution) for solution in Solve(derivative, variable)]


def PotentialEnergy(mass: float, height: float, grav_acc: float = g) -> float:
    return mass * height * grav_acc


def PrimeQ(integer: int) -> bool:
    if integer == int(integer):
        return sympy.primetest.isprime(int(integer))
    else:
        raise TypeError("Unable to run a primality test on the given argument")


def PrimePi(number: float) -> int:
    return sympy.ntheory.generate.primepi(number)


def PrimeFac(integer: int) -> list:
    if integer == int(integer):
        result = []
        for factor, exponent in sympy.ntheory.factor_.factorint(int(integer)).objs():
            result.extend([factor] * exponent)
        return result
    else:
        raise TypeError("Unable to factorize the given argument")


def Permutations(collection: collections.Iterable) -> list:
    perms = list(itertools.permutations(collection))
    if isinstance(collection, str):
        return list(map("".join, perms))
    return list(map(list, perms))


def Calculate(equation: Union[list, str], replacement: list) -> Union[list, float]:
    replacements = dict(replacement)
    if isinstance(equation, str):
        expression = Expression(equation)
        for variable in replacements:
            expression = expression.replace(variable, str(replacements.get(variable)))
        return eval(expression)
    results = []
    for expression in map(Expression, equation):
        for replacement in replacements:
            expression = expression.replace(replacement, str(replacements.get(replacement)))
        results.append(eval(expression))
    return results


def Print(*objects, Sep: str = " ", End: str = "\n"):
    result = []
    for element in objects:
        if isinstance(element, list):
            result.append(Parser().parse_list(element))
        else:
            result.append(element)
    print(*result, sep=Sep, end=End)


def Powerset(collection: collections.Iterable) -> list:
    lst = list(collection)
    return [list(z) for z in itertools.chain.from_iterable(itertools.combinations(lst, r + 1) for r in range(len(lst)))]


def Root(base: float, root: float = 2) -> float:
    return base ** (1 / root)


def Range(*arguments: float) -> Union[list, None]:
    step = 1
    if len(arguments) == 3:
        step = arguments[-1]
    if len(arguments) >= 2:
        lower_bound = arguments[0]
        upper_bound = arguments[1]
    else:
        lower_bound = 1
        upper_bound = arguments[0]
    if NumericQ(lower_bound) and NumericQ(upper_bound) and NumericQ(step):
        step_sgn = 1 if lower_bound <= upper_bound else -1
        step *= step_sgn
        if step == 0:
            return None
        if step % 1 == 0:
            return list(range(Floor(lower_bound), Floor(upper_bound) + step_sgn, step))
        return [list(range(Floor(lower_bound), Floor(upper_bound) + step_sgn, s)) for s in [Floor(step), Ceil(step)]]
    else:
        raise TypeError("The arguments to 'Range' must all be integers.")


def Round(number: float, number_of_decimals: int = 0) -> float:
    return round(number, number_of_decimals)


def RunLengthEncode(collection: collections.Iterable) -> collections.Iterable:
    return [(len(list(b)), a) for a, b in itertools.groupby(collection)]


def RunLengthDecode(encoded: list) -> collections.Iterable:
    result = []
    for pair in encoded:
        result.extend(pair[0] * [pair[1]])
    return result


def Reshape(collection: list, shape: collections.Iterable) -> object:
    import numpy
    return [list(z) for z in numpy.reshape(collection, shape)]


def Reverse(collection: collections.Sequence) -> collections.Sequence:
    return collection[::-1]


def ReIm(number: complex) -> tuple:
    return number.real, number.imag


def Reduce(func: callable, collection: collections.Iterable) -> collections.Iterable:
    from functools import reduce
    return reduce(func, collection)


def SchwarzschildRadius(mass: float) -> float:
    return (2 * mass * G) / (c ** 2)


def SquareQ(number: float) -> bool:
    if number == int(number):
        return Root(number) == int(Root(number))
    else:
        return False


def Slice(iterable: collections.Sequence, start: int = 0, end: int = 0, step: int = 1) -> collections.Sequence:
    return iterable[start:end or len(iterable):step]


def Sum(obj: list) -> Union[list, float]:
    if all(map(NumericQ, obj)):
        return sum(obj)
    return [sum(obj) if isinstance(obj, list) and all(map(NumericQ, obj)) else obj for obj in obj]


def STDIN() -> list:
    return sys.stdin.read().split("\n")


def String(obj: object) -> str:
    return str(obj)


def Str(obj: object) -> str:
    if isinstance(obj, list):
        return Parser.parse_list(obj)
    return str(obj)


def Split(collection: collections.Sequence, element: object) -> list:
    result = [[]]
    for elem in collection:
        if elem == element:
            result.append([])
        else:
            result[-1].append(elem)
    return result


def Solve(equation: str, variable: Union[Symbol, str] = x) -> list:
    return [str(solution) for solution in solve(Expression(equation), variable)]


def Sort(func: callable, collection: collections.Sequence, *, Descending: bool = False) -> collections.Sequence:
    return sorted(collection, key=func, reverse=Descending)


def TangentialComponent(force: float, angle: float) -> float:
    return force * Sin(angle)


def Unique(collection: collections.Sequence) -> collections.Sequence:
    result = []
    for element in collection:
        if element not in result:
            result.append(element)
    return "".join(result) if isinstance(collection, str) else result


def Zip(obj: list, filler: object = None) -> list:
    return list(map(list, itertools.zip_longest(*obj, fillvalue=filler)))
