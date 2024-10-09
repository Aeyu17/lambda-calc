IDENTITY = lambda a: a

TRUE = lambda x: lambda y: x
FALSE = lambda x: lambda y: y

IFTHEN = lambda b: lambda x: lambda y: b(x)(y)

AND = lambda p: lambda q: p(q)(p)
OR = lambda p: lambda q: p(p)(q)
NOT = lambda p: p(FALSE)(TRUE)

