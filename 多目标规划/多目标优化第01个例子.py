# Mar 1, 2022
# Modified by Dr. XU

from pyomo.environ import *
from pyomo.opt import SolverFactory

N = 4
I = range(1, N+1)

# 注意大小写
m = ConcreteModel()

# m.x = Var(I, domain=NonNegativeReals)
m.x = Var(I, domain=NonNegativeIntegers)

# Reals, PositiveReals, NonNegativeReals
# Integers,  PositiveIntegers, NegativeIntegers
# Binary

m.con1 = Constraint(expr= 5*m.x[1] + 10*m.x[2] + 3 * m.x[3] +  4 * m.x[4] <= 20 )

# m.con2 = Constraint(expr=100* m.x[1] + 80*m.x[2] + 127 * m.x[3] + 90 * m.x[4] >= 293 )

m.obj = Objective(expr= 100* m.x[1] + 80*m.x[2] + 127 * m.x[3] + 90 * m.x[4], sense = maximize)

# m.obj = Objective(expr= 0.7*m.x[1] + 0.6*m.x[2] + 0.5 * m.x[3] + m.x[4], sense = maximize)

# result = SolverFactory('cplex', executable='/Applications/CPLEX_Studio201/cplex/bin/x86-64_osx/cplex').solve(m)
result = SolverFactory('glpk').solve(m)
# gurobi, glpk, mosek
#
# opt = SolverFactory('gurobi' )
# opt.options['NonConvex'] = 2
# opt.solve(m, tee=True)


m.pprint()

m.display()

print('---------------------------')
print( f'The objective is {value(m.obj)}' )
print('---------------------------')