from boolean import *

SUCC = lambda n: lambda f: lambda x: f(n(f)(x))
PLUS = lambda m: lambda n: m(SUCC)(n)
MULT = lambda m: lambda n: m(PLUS(n))(ZERO)
EXP = lambda b: lambda e: e(b)

PRED = lambda n: lambda f: lambda x: n(lambda g: lambda h: h(g(f)))(lambda u: x)(IDENTITY) # returns 0 if the argument is 0
SUB = lambda m: lambda n: n(PRED)(m) # returns m - n when m > n, 0 otherwise

ZERO = FALSE
ONE = lambda f: lambda x: f(x)
TWO = lambda f: lambda x: f(f(x))
THREE = SUCC(TWO)
FOUR = SUCC(THREE)
FIVE = SUCC(FOUR)
SIX = SUCC(FIVE)
SEVEN = SUCC(SIX)
EIGHT = SUCC(SEVEN)
NINE = SUCC(EIGHT)
TEN = SUCC(NINE)

ISZERO = lambda n: n(lambda x: FALSE)(TRUE)
LEQ = lambda m: lambda n: ISZERO(SUB(m)(n))
GEQ = lambda m: lambda n: ISZERO(SUB(n)(m))
EQ = lambda m: lambda n: AND(LEQ(m)(n))(GEQ(m)(n))
LESS = lambda m: lambda n: ISZERO(SUB(SUCC(m))(n))
GREATER = lambda m: lambda n: ISZERO(SUB(SUCC(n))(m))

MIN = lambda m: lambda n: LEQ(m)(n)(m)(n)
MAX = lambda m: lambda n: GEQ(m)(n)(m)(n)