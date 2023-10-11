from logic import *

p = Symbol('P')
q = Symbol('Q')
r = Symbol('R')
sent0 = Not(Or(p,q))
sent1 = And(Not(p) ,Not(q))
Sent = Biconditional(sent0, sent1)

print(Sent.formula())
print(sent1.formula())

