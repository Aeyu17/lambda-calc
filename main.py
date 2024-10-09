from boolean import *
from counting import *

def decode_bool(func):
    return IFTHEN(func)(True)(False)

def decode_number(func):
    incr = lambda x: x + 1
    return func(incr)(0)

if __name__ == '__main__':
    a = TRUE
    b = FALSE

    print(decode_bool(AND(a)(b)))
    print(decode_bool(OR(a)(b)))
    print(decode_bool(NOT(a)))

    print(decode_number(ZERO))
    print(decode_number(SUCC(ONE)))
    print(decode_number(PLUS(TWO)(THREE)))
    print(decode_number(MULT(TWO)(THREE)))
    print(decode_number(EXP(TWO)(THREE)))

    print(decode_number(PRED(ONE)))
    print(decode_number(PRED(ZERO))) # should print 0
    print(decode_number(SUB(TEN)(FOUR)))
    print(decode_number(SUB(FOUR)(TEN)))

    print(decode_bool(ISZERO(ZERO)))
    print(decode_bool(ISZERO(ONE)))

    print(decode_bool(LEQ(FOUR)(THREE)))
    print(decode_bool(GEQ(FOUR)(THREE)))
    print(decode_bool(EQ(FOUR)(THREE)))
    print(decode_bool(LESS(FOUR)(THREE)))
    print(decode_bool(GREATER(FOUR)(THREE)))

    print(decode_number(MAX(FOUR)(THREE)))